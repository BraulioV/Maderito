const int EchoPin = 8;
const int TriggerPin = 2;

//control de los motores

const int IN1 = 4;
const int IN2 = 5;
const int IN3 = 6;
const int IN4 = 7;

const int ENA = 9;
const int ENB = 3;

//distancia
int pirPin = A2;

//siguelinea
bool avanza = true;

const int SLA_2 = 10;
const int SLB_2 = 11;
const int SLA = 12;
const int SLB = 13;

int sensorValA, sensorValB, 
    sensorValC, sensorValD;

void avanzar(){
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
}

void retroceder(){
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
}

void girar_izquierda(){
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
}

void girar_derecha(){
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
}

void cambia_velocidad(int v){
  analogWrite(ENA, v); 
  analogWrite(ENB, v); 
}

// mide la distancia que hay entre nosotros y el
// robot enemigo usando el sensor de distancia
int ping(int TriggerPin, int EchoPin) {
   long duration, distanceCm;
   
   digitalWrite(TriggerPin, LOW);  //para generar un pulso limpio ponemos a LOW 4us
   delayMicroseconds(4);
   digitalWrite(TriggerPin, HIGH);  //generamos Trigger (disparo) de 10us
   delayMicroseconds(10);
   digitalWrite(TriggerPin, LOW);
   
   duration = pulseIn(EchoPin, HIGH);  //medimos el tiempo entre pulsos, en microsegundos
   
   distanceCm = duration * 10 / 292/ 2;   //convertimos a distancia, en cm
   return distanceCm;
}

void escapar(){
  Serial.println("Girando");
  delay(20);
  girar_izquierda();
  delay(500);
  Serial.println("Retrocediendo");
  cambia_velocidad(255);
  delay(20);
  retroceder();
  Serial.println("Acelerando");
  delay(100);
  cambia_velocidad(0);
}

void setup() {
    pinMode (IN1, OUTPUT);
    pinMode (IN2, OUTPUT);
    pinMode (IN3, OUTPUT);
    pinMode (IN4, OUTPUT);
    pinMode (ENA, OUTPUT);
    pinMode (ENB, OUTPUT);
    pinMode (SLA, INPUT);
    pinMode (SLB, INPUT);
    pinMode (SLA_2, INPUT);
    pinMode (SLB_2, INPUT);
    pinMode(TriggerPin, OUTPUT);
    pinMode(EchoPin, INPUT);
    Serial.begin(9600); 
    cambia_velocidad(127);
    avanzar();

}

void loop() {
 
    /*
    
    //high para delante y low para atrás
    //variables de los siguelinea
    sensorValA = digitalRead(SLA);
    sensorValB = digitalRead(SLB);
    sensorValC = digitalRead(SLB_2);
    sensorValD = digitalRead(SLA_2);
    
    //muestra por serial de los valores (0 o 1)
    Serial.println("Sensor A: ");
    Serial.println(sensorValA);
    Serial.println("Sensor B: " + sensorValB);
    Serial.println("Sensor C: " + sensorValC);
    Serial.println("Sensor D: " + sensorValD);
    
    
    if( sensorValC == 0 || sensorValD == 0 ) //linea negra delante derehca
    {   
      avanza = false;
      //mover maderito hacia atrás
      retroceder();
      delay(100);
    }
    else if( sensorValA == 0 || sensorValB == 0 )
    {
        avanza = true;
        //mover maderito hacia delante
        avanzar();
        delay(100);
    } 
    else {
      if (avanza){
        avanzar();
      }
      else{
        retroceder();
      }
    }*/
    int cm = ping(TriggerPin, EchoPin);
    Serial.println(cm);
    delay(200);
    if (cm < 15) escapar();
}


