int aPwm=9;
int aIn1=8;
int aIn2=7;

int bPwm=11;
int bIn1=12;
int bIn2=13;

void setup() {
  pinMode(aPwm, OUTPUT);
  pinMode(aIn1, OUTPUT);
  pinMode(aIn2, OUTPUT);
  pinMode(bPwm, OUTPUT);
  pinMode(bIn1, OUTPUT);
  pinMode(bIn2, OUTPUT);
}

void loop() {
  

}

void forward()
{
  digitalWrite(aIn1, HIGH);
  digitalWrite(aIn2, LOW);
  analogWrite(aPwm, 150);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, HIGH);
  digitalWrite(bIn2, LOW);
  analogWrite(bPwm, 150);
  delay(1000);
  Stop();
}

void reverse()
{
  digitalWrite(aIn1, LOW);
  digitalWrite(aIn2, HIGH);
  analogWrite(aPwm, 150);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, LOW);
  digitalWrite(bIn2, HIGH);
  analogWrite(bPwm, 150);
  delay(1000);
  Stop();
}

void left()
{
  digitalWrite(aIn1, HIGH);
  digitalWrite(aIn2, LOW);
  analogWrite(aPwm, 150);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, LOW);
  digitalWrite(bIn2, HIGH);
  analogWrite(bPwm, 150);
  delay(1000);
  Stop();
}

void right()
{
  digitalWrite(aIn1, LOW);
  digitalWrite(aIn2, HIGH);
  analogWrite(aPwm, 150);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, HIGH);
  digitalWrite(bIn2, LOW);
  analogWrite(bPwm, 150);
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

