#include <Servo.h>
#include <NewPing.h>

//Global Variables Declaration
#define TRIG=
#define ECHO=
#define SERVO=
#define BAUD=


NewPing sonar(TRIG,ECHO);
Servo myservo;


void setup() {
  myservo.attach(SERVO);
  Serial.begin(BAUD);
}

void Sweep(){
  for(pos = 0; pos < 180; pos += 5)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 5 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm(); 
    Serial.print(dist);
  } 
  for(pos = 180; pos>=1; pos-=5)     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm(); 
    Serial.print(dist);
  }
}
void loop() {
  Sweep();
}
