#include <Servo.h>

Servo lockServo;

void setup() {
  Serial.begin(9600);
  lockServo.attach(9);
  lockServo.write(0); // Locked position
}

void loop() {

  if (Serial.available()) {

    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "UNLOCK") {
      lockServo.write(90);
      delay(5000);
      lockServo.write(0);
    }
  }
}

