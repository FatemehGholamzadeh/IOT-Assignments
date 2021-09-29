    #include <LiquidCrystal.h>
    
    LiquidCrystal lcd (13,12,11,10,9,8);
    int sensor = 0 ;
    float v = 0.0 ;
    int ledPin = 0;
  
    void setup() {
      lcd.begin(16,2);
      pinMode(ledPin, OUTPUT);
    }
    void loop() {
      sensor = analogRead(A1);
      v = sensor * (100.0f /1024.0f) ;
      lcd.setCursor(0,0);
      lcd.print(v);
      if(v > 50){
        digitalWrite(ledPin, HIGH);
        delay(1000);
        }
      else{
        digitalWrite(ledPin, LOW);
        delay(1000);
        }
      
    
    }
