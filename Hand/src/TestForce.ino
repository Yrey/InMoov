/**
 * Script arduino to approximate the force applied
 */

#include <Servo.h>

Servo myservo; 

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  myservo.attach(3);
}

// the loop routine runs over and over again forever:
void loop() {
  float sensorValue;
  myservo.write(90);
  
  float start = millis();
  int count = 0;
  double average = 0.0;
  while(millis() - start < 100){
    count++;
    sensorValue = analogRead(A0);
    sensorValue = map(sensorValue, 0, 1023, 0, 5000);
    average+=(5000 - sensorValue)/1000.0;
  }
  average/=count;
  Serial.println((10.8*average+0.208)/9.81);
}
