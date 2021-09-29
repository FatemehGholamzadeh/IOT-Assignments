#include <LiquidCrystal.h>

const int rs = 12;
const int en = 11;
const int d4 = 5;
const int d5 = 4;
const int d6 = 3;
const int d7 = 2;

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
 
 
  void setup() {
    lcd.begin(16, 2);
    Serial.begin(9600);
    Serial.println("hello");
       
  }
  
  void loop() {
    if(Serial.available() > 0 ){
    lcd.write(Serial.read());
    }
  }
