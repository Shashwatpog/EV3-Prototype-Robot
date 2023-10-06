#!/usr/bin/env python3
import time 
from ev3dev2.motor import *
from ev3dev2.wheel import EV3Tire
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.display import *


forward = MoveTank(OUTPUT_A,OUTPUT_D)
x = 30
speed = 5.8783

display = Display()
color_sensor = ColorSensor(INPUT_4)
given_box_type = "BOX TYPE 1"
barcode = []

def read_color():
    color_sensor.mode = 'COL-REFLECT'
    val = color_sensor.color
    barcode.append(val)



read_color()
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),0.5/speed)
time.sleep(1)
read_color()
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),0.5/speed)
time.sleep(1)
read_color()
forward.on_for_seconds(SpeedPercent(-25),SpeedPercent(-25),0.5/speed)
time.sleep(1)
read_color()

if (barcode[0] == 1) and (barcode[1] == 6) and (barcode[2] ==6) and (barcode[3] == 6):
    box_type = "BOX TYPE 1"
elif (barcode[0] == 1) and (barcode[1] == 6) and (barcode[2] == 1) and (barcode[3] == 6):
    box_type = "BOX TYPE 2"
elif (barcode[0] == 1) and (barcode[1] == 1) and (barcode[2] == 6) and (barcode[3] == 6):
    box_type = "BOX TYPE 3"
elif (barcode[0] == 1) and (barcode[1] == 6) and (barcode[2] == 6) and (barcode[3] == 1):
    box_type = "BOX TYPE 4"
else:
    box_type = ""
if box_type == given_box_type:
    message = "THE BARCODE MATCHES"
elif box_type != given_box_type:
    message = "BARCODE DOES NOT MATCH"

code_read = str(barcode[0]) + " " + str(barcode[1]) + " " + str(barcode[2]) + " " + str(barcode[3])
display.text_pixels(box_type, clear_screen=True, x=0, y=80, text_color='black', font=None)
display.update()
display.text_pixels(message, clear_screen = False,x = 0, y = 110, text_color='black',font = None)
display.update()
display.text_pixels(code_read, clear_screen = False, x = 0, y = 70, text_color='black',font = None)
display.update()
time.sleep(10)