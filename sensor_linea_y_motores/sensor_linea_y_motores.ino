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

// velocidad de giro
int v_angular = 255;

//siguelinea
bool avanza = true;

const int SLA_2 = 10;
const int SLB_2 = 11;
const int SLA = 12;
const int SLB = 13;

int sensorValA, sensorValB, 
    sensorValC, sensorValD;

void retroceder(){
    //Serial.write('m');
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
}

void avanzar(){
    //Serial.write('m');
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
}

void girar_izquierda(){
    //Serial.write('m');
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
}

void girar_derecha(){
    //Serial.write('m');
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
  // indicamos a la pi que el robot se mueve
  Serial.write('m');
  cambia_velocidad(0);
  delay(20);
  girar_izquierda();
  cambia_velocidad(255);
  delay(600);
  cambia_velocidad(0);
  delay(20);
  retroceder();
  cambia_velocidad(100);
  delay(100);
  cambia_velocidad(60);
  Serial.write('s');
}

void reconoce_linea_negra() {
  //variables de los siguelinea
  sensorValA = digitalRead(SLA);
  sensorValB = digitalRead(SLB);
  sensorValC = digitalRead(SLB_2);
  sensorValD = digitalRead(SLA_2);
  
  /*
  //muestra por serial de los valores (0 o 1)
  Serial.println("Sensor A: " + sensorValA);
  Serial.println("Sensor B: " + sensorValB);
  Serial.println("Sensor C: " + sensorValC);
  Serial.println("Sensor D: " + sensorValD);
  */
  
  if( sensorValC == 0 || sensorValD == 0 ) //linea negra delante derecha
  {   
    Serial.write('m');
    avanza = false;
    //mover maderito hacia atrás
    retroceder();
    cambia_velocidad(255);
    delay(100);
    cambia_velocidad(0);
    Serial.write('s');
  }
  else if( sensorValA == 0 || sensorValB == 0 )
  {
      Serial.write('m');
      avanza = true;
      //mover maderito hacia delante
      avanzar();
      cambia_velocidad(255);
      delay(100);
      cambia_velocidad(0);
      Serial.write('s');
  } 
  else {
    if (avanza){
      Serial.write('m');
      avanzar();
      cambia_velocidad(255);
      delay(100);
      cambia_velocidad(0);
      Serial.write('s');
      
    }
    else{
      Serial.write('m');
      retroceder();
      cambia_velocidad(255);
      delay(100);
      cambia_velocidad(0);
      Serial.write('s');
    }
  } 
}

void setup() {
    Serial.begin(9600);
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
    
    // el robot debe estar tres segundos quieto al comenzar.
    //indica a la pi que está quieto para que reconozca al robot enemigo
    Serial.write('s');
    delay(3000);
    

}

void loop() {
    // el serial debe estar disponible para comunicarse con la pi
    if (Serial.available() > 0) {
      // medimos distancia con el sensor de distancia
      int cm = ping(TriggerPin, EchoPin);
      if (cm < 15) 
        escapar();
      
      else{
        // leemos la dirección hacia la que se mueve el robot
        char dir = Serial.read();
        //Serial.println(dir);
        if (dir == 'r'){
          //Serial.flush();
          // Serial.println("Giro a la derecha");
          // el robot enemigo ha girado a la derecha        
          Serial.write('m');
          cambia_velocidad(0);
          delay(20);
          girar_derecha();
          cambia_velocidad(v_angular);
          delay(200);
          cambia_velocidad(0);
          // Serial.write('a');
          delay(1000);
          //Serial.write('s');
        
        } else if (dir == 'l') {
          // Serial.println("Giro a la izquierda");
          // el robot enemigo ha girado a la izquierda
          //Serial.flush();
          Serial.write('m');
          cambia_velocidad(0);
          delay(20);
          girar_izquierda();
          cambia_velocidad(v_angular);
          delay(200);
          cambia_velocidad(0);
          // Serial.write('b');
          delay(1000);
          //Serial.write('s');
        } else if (dir == 'q')
        {
          Serial.write('s');
          cambia_velocidad(0);
          //Serial.flush();
          // delay(100);
        }
        
  
        
        // Serial.println(cm);
      }      
      // Serial.write('s');
      
      // comprobamos que el robot no va a salirse de la línea negra
      //reconoce_linea_negra();
    }
}


