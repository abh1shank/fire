#include <ESP32Servo.h>

#define buzzerPin 23
#define servoPin 21
#define count 20
Servo servoMotor;
int deadline;
void setup() {
  pinMode(buzzerPin, OUTPUT); 
  pinMode(LED_BUILTIN, OUTPUT);
  stopBuzzer();
  servoMotor.attach(servoPin);
  servoMotor.write(0);
  deadline_restore(count);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char incomingByte = Serial.read();
    Serial.println(incomingByte); 
    if (incomingByte == 'f') 
    {
        deadline--;
        delayed_trips(150);
    } 
    else if (incomingByte == 'p') 
    {
        deadline--;
        delayed_trips(250);
    }
    else if(incomingbyte == 's')
    {
        deadline--;
        delayed_trips(500);
    }
    else 
    {
      deadline_restore();
      digitalWrite(LED_BUILTIN, LOW);
      stopBuzzer();
      servoMotor.write(0);
    }
  }
}
void deadline_restore()
{
    deadline=count;
}
void delayed_trips(int time)
{
      if
      digitalWrite(LED_BUILTIN, HIGH);
      soundBuzzer();
      delay(time); 
      digitalWrite(LED_BUILTIN, LOW);
      stopBuzzer();
      delay(time);  
}
void trip_MCB()
{
      deadline_restore();
      digitalWrite(LED_BUILTIN, LOW);
      stopBuzzer();
      servoMotor.write(180);
}
void soundBuzzer() {
  digitalWrite(buzzerPin, LOW); // Power the buzzer
}

void stopBuzzer() {
  digitalWrite(buzzerPin, HIGH); // Turn off power to the buzzer
}
