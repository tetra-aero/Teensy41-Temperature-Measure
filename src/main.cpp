// Ref. 1. https://github.com/TeensyUser/doc/wiki/Chip-Temperature
#include <Arduino.h>
extern float tempmonGetTemp(void);

void setup() {
  while (!Serial);
}

void loop() {
  tempmon_Start();
  Serial.print( tempmonGetTemp() );
  tempmon_Stop();
  Serial.println("°C");
  delay(500);
}
