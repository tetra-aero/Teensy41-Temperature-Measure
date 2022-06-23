// Ref. 1. https://github.com/TeensyUser/doc/wiki/Chip-Temperature
// Ref. 2. https://docs.platformio.org/en/latest/scripting/examples/override_package_files.html
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
