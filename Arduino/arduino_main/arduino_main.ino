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

String inData;
int x;
int i;



void setup() {
  myservo.attach(SERVO);
  Serial.begin(BAUD);
}

void loop() {
  wait();
}


void wait()
{
  while (Serial.available() > 0)
    {
        char recieved = Serial.read();
        inData += recieved; 

        // Process message when # character is recieved
        if (recieved == '#')
        {
            x=inData.toInt();
            //Serial.print("Arduino Received: ");
            //Serial.println(x);
            switch (x)
            {
              case 000:
                //Serial.println("Read data");
                Sweep();
              break;

              case 10:
                Serial.println("Move forward");
              break;

              case 11:
                Serial.println("Move back");
              break;

              case 12:
                Serial.println("Turn left");
              break;

              case 13:
                Serial.println("Turn right");
              break;

              case 20:
                dummydata();
            }
            inData = ""; // Clear recieved buffer
        }
    }
}

void dummydata() {
  for(i=0;i<=30;i++)
  {
    Serial.print(i);
    Serial.print(" ");
    Serial.println(i+30);
    delay(5);
  }
  wait();
}

void Sweep(){
for(pos = 10; pos < 170; pos += 10)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 5 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(1000);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm();
    Serial.print(pos);
    Serial.print(" ");
    Serial.println(dist);
  }
for(pos = 170; pos >= 10; pos -= 10)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 5 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(1000);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm();
    Serial.print(pos);
    Serial.print(" ");
    Serial.println(dist);
  }
}

