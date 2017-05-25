//control de los motores

const int IN1 = 4;
const int IN2 = 5;
const int IN3 = 6;
const int IN4 = 7;

const int ENA = 9;
const int ENB = 3;

//siguelinea


const int SLA_2 = 10;
const int SLB_2 = 11;
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
  pinMode (SLA, INPUT);
  pinMode (SLB, INPUT);
  Serial.begin(9600); 

}

void loop() {
  analogWrite(ENA, 255);
  analogWrite(ENB, 255); 

  //high para delante y low para atrás
/*
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  */

  //variables de los siguelinea
  sensorValA = digitalRead(SLA);
  sensorValB = digitalRead(SLB);
  sensorValC = digitalRead(SLB_2);
  sensorValD = digitalRead(SLA_2);

  //muestra por serial de los valores (0 o 1)
  Serial.println(sensorValA);
  Serial.println(sensorValB);
  Serial.println(sensorValC);
  Serial.println(sensorValD);

  
  if( sernsorValA == 0) //linea negra delante derehca
  {
      //mover maderito hacia atrás
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
  }
  if( sensorValB == 0) //línea negra detrás izquierda
  {
      //mover maderito hacia atrás
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
  }
  if( sensorValC == 0) //línea negra detrás derecha
  {
      //mover maderito hacia delante
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
  }
  if( sensorValD == 0) //línea negra detrás izquierda
  {
      //mover maderito hacia delante
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
  }
  
    //girar a la derecha
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  //girar a la izquierda
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  
}
