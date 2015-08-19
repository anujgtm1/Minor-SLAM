//code to sweep servo motor from 0 to 180 and 180 to 0 degree
#include <Servo.h>
Servo myservo; // creates servo object to control servo
int angle = 0; //variable to store servo position

// the setup routine runs once when reset is pressed:
void setup() {                
  // initialize the digital pin 6 as an output.
  myservo.attach(3);
}

// the loop routine runs over and over again forever:
void loop() {
  
  for(angle = 0; angle < 180; angle += 5)    // goes from 0 degrees to 180 degrees
  {                                          // in steps of 1 degree
    myservo.write(angle);                  // tell servo to go to position in variable 'angle'
    delay(15);                             // waits 15ms for the servo to reach the position
  }
  for(angle = 180; angle>=1; angle-=5)     // goes from 180 degrees to 0 degrees
  {                                
    myservo.write(angle);              // tell servo to go to position in variable 'angle'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
