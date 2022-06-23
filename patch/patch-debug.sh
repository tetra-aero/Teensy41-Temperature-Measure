#!/bin/bash

rm -f ~/.platformio/packages/framework-arduinoteensy/.patching-done
diff ~/.platformio/packages/framework-arduinoteensy/cores/teensy4/tempmon.c ./patch/packages/framework-arduinoteensy/cores/teensy4/tempmon.c > ./patch/1-tempmon-add-isr.patch
