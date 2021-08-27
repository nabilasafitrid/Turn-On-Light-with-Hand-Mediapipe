
int led = 13;
int relay= 10;
String data;
void setup(){
   
  // Set the baud rate  
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(relay, OUTPUT);
  delay(10);
  digitalWrite(led, LOW); // matikan led 
  digitalWrite(relay, HIGH);
}
 
void loop(){

  data="";
  if(Serial.available() > 0) {
    delay(10);
    data = (char)Serial.read();

    Serial.println(data);

    if (data == "1"){
      digitalWrite(led, HIGH);
      digitalWrite(relay, LOW);
      Serial.println("on");
    }
    else if (data == "0"){
      digitalWrite(led, LOW); 
      digitalWrite(relay, HIGH);
      Serial.println("off");
    }
    else{
      digitalWrite(led, LOW);
      digitalWrite(relay, HIGH);
    }
//    Serial.flush();
  }
}
