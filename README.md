# Teensy41-Temperature-Measure
By Teensy 4.1 it measure internal CPU temperature.

## shell script that delete patched flag and make new patch file
```
./patch/patch-debug.sh
```

- make patch file
```
diff ~/.platformio/packages/framework-arduinoteensy/cores/teensy4/tempmon.c ./patch/packages/framework-arduinoteensy/cores/teensy4/tempmon.c > ./patch/1-tempmon-add-isr.patch
```

## Reference
1. https://github.com/TeensyUser/doc/wiki/Chip-Temperature
2. https://docs.platformio.org/en/latest/scripting/examples/override_package_files.html
