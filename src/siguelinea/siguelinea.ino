int pinReceptor = 12; //Establecemos el pin a leer
int sensorVal; //Declaramos una variable para almacenar el valor de la lectura

void setup(){
Serial.begin(9600); // Abrimos comunicación Serial
}

void loop(){
sensorVal = digitalRead(pinReceptor); //Guardamos la lectura del pin Analógico
Serial.println(sensorVal); //Sacamos la lectura por serial
delay(50);  //Pequeña pausa de medio segundo
}
