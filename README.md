# Teensy41-Temperature-Measure
By Teensy 4.1 it measure internal CPU temperature.

## make patch file
```
diff ~/.platformio/packages/framework-arduinoteensy/cores/teensy4/tempmon.c ./patch/packages/framework-arduinoteensy/cores/teensy4/tempmon.c > ./patch/1-tempmon-add-isr.patch
```
