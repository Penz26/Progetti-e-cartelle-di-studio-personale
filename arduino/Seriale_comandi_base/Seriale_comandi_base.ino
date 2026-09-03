int pinInNum = 2;   //pinInNum è dove è collegato il bottone
int switchstate = 0;  //inizializzazione variabile che contiene il valore del bottone (0 spento, 1 acceso)
int pinInLed = 11; //pinInLed è dove è collegato il led

void setup() {
  // put your setup code here, to run once:
  pinMode(pinInNum, INPUT); //diciamo a questo pin (bottone) che corrisponde a un input
  pinMode(pinInLed, OUTPUT); //diciamo a questo pin (led) che corrisponde a un output
  Serial.begin(9600);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  switchstate = digitalRead(pinInNum); //switchstate prende il valore di digitalRead(pinInNum), quindi diventa 1 se è premuto, altrimenti rimane 0
  if (switchstate == LOW){
    digitalWrite(pinInLed, LOW);
  }
  else{
    digitalWrite(pinInLed, HIGH);
  }
  Serial.print("Il valore del pulsante è: "); //Messaggio di debug, solo per dare una stringa che dà meglio l'idea
  Serial.println(switchstate);  //Ci dice il valore del pulsante 0 se non è premuto, 1 se è premuto
  delay(100);                   // NON OBBLIGATORIO solo per dare un attimo di dealy per il messaggio di valore
}

