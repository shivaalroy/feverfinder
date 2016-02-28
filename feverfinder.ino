float tempC;
int reading;
int tempPin = 0;
//boolean alarm = false;

void setup() {
  // put your setup code here, to run once:
  analogReference(INTERNAL);
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  reading = analogRead(tempPin);
  tempC = reading / 9.31;
  Serial.println(tempC);
  delay(1000);

  if (tempC > 28.0) { //ideal 38 (real-world threshold)
    digitalWrite(13, HIGH);
    //alarm = true;
  }

  /*if (alarm) {
    digitalWrite(13, HIGH);
    delay(10);
    digitalWrite(13, LOW); 
    delay(10); 
  }*/
}
