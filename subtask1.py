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

x = 30
speed = 5.8783

#walk straight for 36 inches
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),35/speed)
time.sleep(1)
#turn right 90 degrees
turn(86)
#go straight for x inches given during check in
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),x/speed)
# stop for 5 seconds
time.sleep(5)
# go straight for 96-x inches
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),(89-x)/speed)
time.sleep(1)
# turn right 90 degrees
turn(89)
# go straight for 36 inches
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),30/speed)
time.sleep(5)
forward.off
