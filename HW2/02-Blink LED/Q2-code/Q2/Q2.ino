  char c;
  void setup() {
    Serial.begin(9600);
    pinMode(7,OUTPUT);
  }
  
  void loop() {
  
   while ( Serial.available()>0 ){
  
   c = Serial.read();
   if(c =='1')
   {digitalWrite(7,HIGH
   );}
   else if(c =='0')
   {digitalWrite(7,LOW);}
   }
  }
  
   
   
