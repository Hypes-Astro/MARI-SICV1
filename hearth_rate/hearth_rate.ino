#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Hanania";
const char* password = "handarumakmur";
const char* serverName = "http://192.168.0.111:5000/post_data";

#define LP 12
#define LM 13
#define PIN_AN 33

WiFiClient client;

String data_request;


void setup() {
  Serial.begin(9600);
  pinMode(LP, INPUT); // Setup for leads off detection LO +
  pinMode(LM, INPUT); // Setup for leads off detection LO -
  
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  if ((digitalRead(LP) == 1) || (digitalRead(LM) == 1)) {
    Serial.println('!');
  } else {
    int sensorValue = analogRead(PIN_AN);

    // Mengirimkan data melalui metode POST
    if (WiFi.status()== WL_CONNECTED) {
        WiFiClient client;
        HTTPClient http;

        http.begin(client, serverName);
        http.addHeader("Content-Type", "application/x-www-form-urlencoded");
        
        
        data_request = "data=";    
        data_request += String(sensorValue);       

        int respon = http.POST(data_request);

        Serial.print("HTTP Response code: ");
        Serial.println(respon);

        http.end();
     
    }else{
        Serial.println("Wifi ga nyambung");

    }

    delay(5000); // Delay 5 detik sebelum mengirimkan data lagi
  }

  delay(500); // Wait for a bit to keep serial data from saturating
}