from jetson_inference import detectNet
from jetson_utils import gstCamera, glDisplay
import serial 

isPerson = False
counter = 0
counter_two = 0
authorized = True

#arduino serial communication
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=10)

#detectnet setup
net = detectNet("ssd-mobilenet-v2", threshold = 0.5)
camera = gstCamera(1280 ,720 , "/dev/video0")
display = glDisplay()

#gcloud pubsub setup
from concurrent.futures import TimeoutError
from google.api_core import retry
from google.cloud import pubsub_v1

project_id = "sentry-387903"
subscription_id = "authCom-sub"
topic_id = "appNoitif"
timeout = 0.5

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)
NUM_MESSAGES = 20

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

stored = 'hi'
while not 'go' in stored:
	response = subscriber.pull(
	request={"subscription": subscription_path, "max_messages": NUM_MESSAGES},
	retry=retry.Retry(deadline=10),
	)

	if len(response.received_messages) != 0:
		ack_ids = []
		for received_message in response.received_messages:
			stored = received_message.message.data.decode("utf-8")
			print(f"Received: {stored}.")
			ack_ids.append(received_message.ack_id)
		subscriber.acknowledge(
		request={"subscription": subscription_path, "ack_ids": ack_ids}
		)

		print(
		f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}."
		)
		print(stored)

while display.IsOpen():
	img, width, height = camera.CaptureRGBA()
	detections = net.Detect(img, width, height)
	display.RenderOnce(img, width, height)
	display.SetTitle("Object Detectioon | Network {:.0f} FPS".format(net.GetNetworkFPS()))

	counter+=1
	if counter >= 15:
		if len(detections) == 0:
			isPerson = False;
			#arduino.write(bytes('NO\n','utf-8'))
		else:
			for x in detections:
				print(x.ClassID)
				if(x.ClassID == 1) and authorized:
					isPerson = True;
					#arduino.write("Person Detected")
					#arduino.write(bytes('YES\n','utf-8'))
				else:
					isPerson = False;
					#arduino.write("Person Not Detected")
					#arduino.write(bytes('NO\n','utf-8'))
		if isPerson:
			print("Person detected. Writing to serial")
			arduino.write(bytes('YES\n','utf-8'))

			data_str = f"Shot fired."
			data = data_str.encode("utf-8")
			future = publisher.publish(topic_path, data)
			print(future.result())
		else:
			print("Person not detected. Writing to serial")
			arduino.write(bytes('NO\n','utf-8'))
		counter = 0

	counter_two += 1
	if counter_two >= 900:
		response = subscriber.pull(
		request={"subscription": subscription_path, "max_messages": NUM_MESSAGES},
		retry=retry.Retry(deadline=10),
		)

		if len(response.received_messages) != 0:
			ack_ids = []
			for received_message in response.received_messages:
				stored = received_message.message.data.decode("utf-8")
				print(f"Received: {stored}.")
				ack_ids.append(received_message.ack_id)
			subscriber.acknowledge(
			request={"subscription": subscription_path, "ack_ids": ack_ids}
			)

			print(
			f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}."
			)
			print(stored)
		if 'go' in stored:
			authorized = True
			print("Authorized")
		else:
			authorized = False
			print("Not authorized")
		counter_two = 0

