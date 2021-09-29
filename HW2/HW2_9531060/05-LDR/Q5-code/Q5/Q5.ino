
  int sensor = 0 ;
  void setup() {
    Serial.begin(9600);    

  }
  
  void loop() {
   sensor = analogRead(A1);
   Serial.println(sensor);
   delay(1000);
  }
  
   
   
