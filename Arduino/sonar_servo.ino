#include <Servo.h>
#include <NewPing.h>
//Global Variables Declaration

#define TRIG 2
#define ECHO 4
#define SERVO 3
#define BAUD 9600

NewPing sonar(TRIG,ECHO);
unsigned int dist;
unsigned int pos; 
Servo myservo;

void setup() {
  myservo.attach(SERVO);
  Serial.begin(BAUD);
}

void Sweep(){
for(pos = 0; pos < 180; pos += 3)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 5 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(50);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm();
    Serial.print(pos);
    Serial.print(" ");
    Serial.println(dist);
  }
for(pos = 180; pos >= 1; pos -= 3)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 5 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(50);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm();
    Serial.print(pos);
    Serial.print(" ");
    Serial.println(dist);
  }
}
void loop() {
  Sweep();
}
