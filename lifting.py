#!/usr/bin/env python3
import time 
from ev3dev2.sensor import *
from ev3dev2.display import *
from ev3dev2.display import Display
from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import UltrasonicSensor

forward = MoveTank(OUTPUT_A,OUTPUT_D)
small_motor = Motor(OUTPUT_B)

gyro = GyroSensor()
gyro.mode = 'GYRO-ANG'
display = Display()
speed = 5.8783

def turn(x):
    gyro.reset()
    gyro.calibrate()
    angle = gyro.angle
    while angle > x:
        forward.on_for_seconds(25,-25,0.1)
        angle = gyro.angle
    forward.off


small_motor.on_for_seconds(SpeedPercent(80),1.5)
forward.on_for_seconds(SpeedPercent(10),SpeedPercent(10),0.5)
turn(-87)
time.sleep(1)
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),4/speed)
time.sleep(1)
small_motor.on_for_seconds(SpeedPercent(80),1.5)
turn(-178)
time.sleep(1)
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),1.5/speed)
small_motor.on_for_seconds(SpeedPercent(-50),1)
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),2.3/speed)
time.sleep(1)
time.sleep(1)
forward.on_for_seconds(SpeedPercent(10),SpeedPercent(10),2)
time.sleep(1)
turn(-85)
time.sleep(1)
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),21/speed)
time.sleep(1)
small_motor.on_for_seconds(SpeedPercent(-50),1)
forward.on_for_seconds(SpeedPercent(10),SpeedPercent(10),2)
