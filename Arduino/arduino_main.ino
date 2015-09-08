#include <Servo.h>
#include <NewPing.h>
//Global Variables Declaration

#define TRIG 2
#define ECHO 4
#define SERVO 3
#define BAUD 9600

//***********************
#define aPwm 6
#define aIn1 8
#define aIn2 5

#define bPwm 11
#define bIn1 12
#define bIn2 13
//***********************

NewPing sonar(TRIG,ECHO);
unsigned int dist;
unsigned int pos; 
Servo myservo;

String inData;
int x;
int i;

void setup() {
  myservo.attach(SERVO);
  myservo.write(60);
  delay(300);
  Serial.begin(BAUD);
  //*****************
  pinMode(aPwm, OUTPUT);
  pinMode(aIn1, OUTPUT);
  pinMode(aIn2, OUTPUT);
  pinMode(bPwm, OUTPUT);
  pinMode(bIn1, OUTPUT);
  pinMode(bIn2, OUTPUT);
  //*****************
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
for(pos = 60; pos < 125; pos += 5)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 5 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(30);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm();
    Serial.print(pos);
    Serial.print(" ");
    Serial.println(dist);
  }
for(pos = 120; pos >= 60; pos -= 5)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 5 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(30);                       // waits 15ms for the servo to reach the position
    dist = sonar.ping_cm();
    Serial.print(pos);
    Serial.print(" ");
    Serial.println(dist);
  }
  Serial.println('#');
}

//***********************************

void reverse()
{
  digitalWrite(aIn1, HIGH);
  digitalWrite(aIn2, LOW);
  analogWrite(aPwm, 238);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, HIGH);
  digitalWrite(bIn2, LOW);
  analogWrite(bPwm, 187);
  delay(1000);
  Stop();
}

void forward()
{
  digitalWrite(aIn1, LOW);
  digitalWrite(aIn2, HIGH);
  analogWrite(aPwm, 238);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, LOW);
  digitalWrite(bIn2, HIGH);
  analogWrite(bPwm, 200);
  delay(1000);
  Stop();
}

void right()
{
  digitalWrite(aIn1, HIGH);
  digitalWrite(aIn2, LOW);
  analogWrite(aPwm,210);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, LOW);
  digitalWrite(bIn2, HIGH);
  analogWrite(bPwm, 148);
  delay(1000);
  Stop();
}

void left()
{
  digitalWrite(aIn1, LOW);
  digitalWrite(aIn2, HIGH);
  analogWrite(aPwm, 216);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, HIGH);
  digitalWrite(bIn2, LOW);
  analogWrite(bPwm, 137);
  delay(1000);
  Stop();
}

void Stop()
{
  digitalWrite(aIn1, LOW);
  digitalWrite(aIn2, LOW);  
  digitalWrite(bIn1, LOW);
  digitalWrite(bIn2, LOW);
}

//***************************************




