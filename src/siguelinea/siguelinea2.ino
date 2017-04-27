int pinReceptorA = 12; //Establecemos el pin a leer
int pinReceptorB = 13; //Establecemos el pin a leer
int sensorValA, sensorValB; //Declaramos una variable para almacenar el valor de la lectura

void setup(){
Serial.begin(9600); // Abrimos comunicación Serial
}

void loop(){
sensorValA = digitalRead(pinReceptorA); //Guardamos la lectura del pin Analógico
sensorValB = digitalRead(pinReceptorB);

Serial.println(sensorValA); //Sacamos la lectura por serial
//Serial.println(sensorValB);
//delay(1000);  //Pequeña pausa de medio segundo

//sensorVal = digitalRead(pinReceptorB); //Guardamos la lectura del pin Analógico
//Serial.println(sensorVal); //Sacamos la lectura por serial
delay(100);  //Pequeña pausa de medio segundo
}
