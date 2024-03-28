#include <ESP32Servo.h>

#define buzzerPin 23
#define servoPin 21

Servo servoMotor;

void setup() {
  pinMode(buzzerPin, OUTPUT); 
  pinMode(LED_BUILTIN, OUTPUT);
  stopBuzzer();
  servoMotor.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char incomingByte = Serial.read();
    Serial.println(incomingByte); // Print the incoming byte to the serial monitor
    if (incomingByte == '1') {
      digitalWrite(LED_BUILTIN, HIGH);
      servoMotor.write(180);
      soundBuzzer();
      delay(200); // Delay for 200 milliseconds
      stopBuzzer();
      digitalWrite(LED_BUILTIN, LOW);
      servoMotor.write(0);
      delay(200); // Delay for 200 milliseconds
    } else {
      digitalWrite(LED_BUILTIN, LOW);
      stopBuzzer();
      servoMotor.write(0); // Stop servo motor immediately
    }
  }
}

void soundBuzzer() {
  digitalWrite(buzzerPin, LOW); // Power the buzzer
}

void stopBuzzer() {
  digitalWrite(buzzerPin, HIGH); // Turn off power to the buzzer
}
