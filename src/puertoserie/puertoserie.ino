const int ledPin = 10;

void setup()
{
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0) {
    if (Serial.read() == 's') {
      digitalWrite(ledPin, HIGH);
      delay(2000);
    }
  } else {
    digitalWrite(ledPin, LOW);
  }
  
}


