#include <Servo.h>

Servo trigger;

bool shot = false;

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  while (!Serial) {
    ; // wait for serial port to connect.
  }
  trigger.attach(9);
  trigger.write(50);

}

void loop() {
  char buffer[16];
  // if we get a command, turn the LED on or off:
  if (Serial.available() > 0) {
    int size = Serial.readBytesUntil('\n', buffer, 12);
    if (buffer[0] == 'Y') {
      digitalWrite(LED_BUILTIN, HIGH);
      if(!shot){
        trigger.write(102);
        shot = true;
      }else{
        trigger.write(0);
        shot = false;
      }
    }
    if (buffer[0] == 'N') {
      digitalWrite(LED_BUILTIN, LOW);
      trigger.write(50);
    }
  }
}
