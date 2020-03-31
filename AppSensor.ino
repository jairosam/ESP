#include <WiFiClient.h>
#include <ESP8266WiFi.h>

int mq2=A0;
int data;

void setup() {
  Serial.begin(115200);
}

void loop() {
  data = analogRead(mq2);
  Serial.println(data);
  delay(5000);

}
