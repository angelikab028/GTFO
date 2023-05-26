#include <Servo.h>

Servo trigger;
enum State { WAITING, INTRUDER_DETECTED };

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  while (!Serial) {
    ;
  }
  trigger.attach(9);
  trigger.write(0);
}

void loop() {
  static char buffer[16];
  static State state = WAITING;
  
  switch (state) {
    case WAITING:
      if (Serial.available() > 0) {
        int size = Serial.readBytesUntil('\n', buffer, 12);
        state = INTRUDER_DETECTED;
      }
      break;
      
    case INTRUDER_DETECTED:
      if (buffer[0] == 'Y') {
        digitalWrite(LED_BUILTIN, HIGH);
        trigger.write(180);
      }
      else if (buffer[0] == 'N') {
        digitalWrite(LED_BUILTIN, LOW);
        trigger.write(0);
      }
      state = WAITING;
      break;
  }
}