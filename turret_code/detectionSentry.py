from jetson_inference import detectNet
from jetson_utils import gstCamera, glDisplay
import serial 

isPerson = False
counter = 0

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=10)

net = detectNet("ssd-mobilenet-v2", threshold = 0.5)
camera = gstCamera(1280 ,720 , "/dev/video0")
display = glDisplay()

while display.IsOpen():
	img, width, height = camera.CaptureRGBA()
	detections = net.Detect(img, width, height)
	display.RenderOnce(img, width, height)
	display.SetTitle("Object Detectioon | Network {:.0f} FPS".format(net.GetNetworkFPS()))

	counter+=1
	if counter == 15:
		if len(detections) == 0:
			isPerson = False;
			#arduino.write(bytes('NO\n','utf-8'))
		else:
			for x in detections:
				print(x.ClassID)
				if(x.ClassID == 1):
					isPerson = True;
					#arduino.write("Person Detected")
					#arduino.write(bytes('YES\n','utf-8'))
				else:
					isPerson = False;
					#arduino.write("Person Not Detected")
					#arduino.write(bytes('NO\n','utf-8'))
		if isPerson:
			arduino.write(bytes('YES\n','utf-8'))
		else:
			arduino.write(bytes('NO\n','utf-8'))
		counter = 0

