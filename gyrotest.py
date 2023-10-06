#!/usr/bin/env python3
import time
## Imports all Objects and Methods from the motor module
from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor


forward = MoveTank(OUTPUT_A,OUTPUT_D)

speed = 5.8783
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),60/speed)
time.sleep(1)

forward.off
