#!/usr/bin/env python3
import time
## Imports all Objects and Methods from the motor module
from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor


forward = MoveTank(OUTPUT_A,OUTPUT_D)
gyro = GyroSensor()
gyro.mode = 'GYRO-ANG'

def turn(x):
    gyro.reset()
    gyro.calibrate()
    angle = gyro.angle
    while angle < x:
        forward.on_for_seconds(-25,25,0.1)
        angle = gyro.angle
    forward.off

speed = 5.8783
#walk back for 12 inches
forward.on_for_seconds(SpeedPercent(25),SpeedPercent(25),10/speed)
time.sleep(1)

#turn right 90 degrees
turn(86)
time.sleep(1)

#go straight for 96 inches 
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),90/speed)
time.sleep(1)

# turn 270 degrees
turn(267)

# go straight for 12 inches
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),12/speed)
time.sleep(1)

forward.off
