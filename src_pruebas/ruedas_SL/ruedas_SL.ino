
//control de los motores

const int IN1 = 4;
const int IN2 = 5;
const int IN3 = 6;
const int IN4 = 7;

const int ENA = 9;
const int ENB = 3;

//siguelinea

const int SLA = 12;
const int SLB = 13;
int sensorValA, sensorValB;


void setup() {

  pinMode (IN1, OUTPUT);
  pinMode (IN2, OUTPUT);
  pinMode (IN3, OUTPUT);
  pinMode (IN4, OUTPUT);
  pinMode (ENA, OUTPUT);
  pinMode (ENB, OUTPUT);
  //pinMode (SLA, INPUT);
  pinMode (SLB, INPUT);
  // put your setup code here, to run once:
  Serial.begin(9600); 

}

void loop() {

  //sensorValA = digitalRead(SLA); //Guardamos la lectura del pin Analógico
  //sensorValB = digitalRead(SLB);

  analogWrite(ENA, 255);
  analogWrite(ENB, 255); 

  //high para delante y low para atrás

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
 
  sensorValB = digitalRead(SLB); 
  // put your main code here, to run repeatedly:

  Serial.println(sensorValB); //Sacamos la lectura por serial

}
