#include<ESP32Servo.h>
#define buzzerPin 23
Servo servomotor;
 void setup() {
  pinMode(buzzerPin, OUTPUT); 
  pinMode(LED_BUILTIN, OUTPUT);
  servomotor.attach(21);
  Serial.begin(9600);
 }

 void loop() {
  bool f=0;
  if (Serial.available()) {
    char incomingByte = Serial.read();
    if (incomingByte == '1') {
        if(!f)
        {
          servomotor.write(90);
          f=1;
        }
        digitalWrite(LED_BUILTIN, HIGH);
        soundBuzzer();
        delay(100);
        stopBuzzer();
        digitalWrite(LED_BUILTIN, LOW);
        delay(100);
      
    }
    else digitalWrite(LED_BUILTIN, LOW),stopBuzzer(),f=0;
  }
 }
 void soundBuzzer() {
  digitalWrite(buzzerPin, HIGH); 
}
void stopBuzzer() {
  digitalWrite(buzzerPin, LOW); 
}
