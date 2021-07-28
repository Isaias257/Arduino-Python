void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT);

}
void loop() {
  int pushed = digitalRead(2);
  if (pushed == LOW){
    Serial.println("1");
  }else{
    Serial.println("0");
  }
}
