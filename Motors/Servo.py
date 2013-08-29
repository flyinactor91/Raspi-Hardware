#!/usr/bin/python

##--Adafruit tutorials -- http://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor
##--Continuously turns servo its full turn radius

# Servo Control
# GPIO Pin 18

import time

def set(property, value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
		f.write(value)
		f.close()	
	except:
		print("Error writing to: " + property + " value: " + value)

def setServo(angle):
	set("servo", str(angle))

set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")

delay_period = 0.005

while True:
	for angle in range(0, 180):
		setServo(angle)
		time.sleep(delay_period)
	for angle in range(0, 180):
		setServo(180 - angle)
		time.sleep(delay_period)
