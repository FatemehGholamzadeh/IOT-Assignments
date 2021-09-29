int led_pin = 6; 
int ldr_pin = A0;
int output;
int led_value;
void setup() {
  pinMode(led_pin, OUTPUT);
}
void loop() {
  //Reading from ldr
  output = analogRead(ldr_pin);
  
  //Mapping the Values between 0 to 255 because we can give output
  //from 0 -255 using the analogwrite funtion
  led_value = map(output, 0, 1023, 0, 255);
  
  led_value = 255 - led_value ;
  analogWrite(led_pin, led_value);
  delay(1);
}
