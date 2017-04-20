//sensor PIR en analog 2
int pirPin = A2;

//datos para interpretar a posteriori
char con[]= { '0', '0' ,'0'};
char option = 'a';
int aux = 0;

void setup(){
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  digitalWrite(pirPin, LOW);
}

void loop() {
       //tiempo de espera de inicio nuevo
       delay(900);

      //si hay presencia = 1
       if(digitalRead(pirPin) == HIGH){
          Serial.print("1-"); 
          option = '1';
          delay(500);
          aux++;
     
       }
       else{
          Serial.print("0-"); 
          option = '0';
          delay(500);
          aux++;
          
       }

    if(aux == 3 ){    
          Serial.print("\nEL array registrado es: ");
          Serial.print(con[0]);
          Serial.print(con[1]);
          Serial.print(con[2]);
          Serial.print("\n");
         
          aux = 0; 
    }

}
