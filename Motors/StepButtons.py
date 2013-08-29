#!/usr/bin/python

##--Michael duPont (flyinactor91.com)
##--Turns a stepper motor in either direction depending on the button pressed. Resets to original position if both are pressed

import RPi.GPIO as GPIO
from StepperLib import *
import time

sevenseg = False

if sevenseg:
	from Adafruit_7Segment import SevenSegment
	segment = SevenSegment(address=0x70)

GPIO.setmode(GPIO.BCM)

#Setup Buttons
stepCWPin = 18
stepCCWPin = 25
GPIO.setup(stepCCWPin , GPIO.IN)
GPIO.setup(stepCWPin , GPIO.IN)

#Display Function
def setNumber(value):
	if value < 0: segment.setColon(True)
	else: segment.setColon(False)
	segment.writeDigit(0 , (abs(value) / 1000)%10)
	segment.writeDigit(1 , (abs(value) / 100)%10)
	segment.writeDigit(3 , (abs(value) / 10)%10)
	segment.writeDigit(4 , abs(value) % 10)

def setLetter(value):
	if not 9 < value < 16: return
	segment.clear()
	segment.writeDigit(4 , value)

num = 0

#Main Loop
while True:
	if (GPIO.input(stepCWPin) == False) and (GPIO.input(stepCCWPin) == True):
		forward(int(delay) / 1000.0, 1)
		num += 1
	elif (GPIO.input(stepCCWPin) == False) and (GPIO.input(stepCWPin) == True):
		backwards(int(delay) / 1000.0, 1)
		num = num - 1
	elif (GPIO.input(stepCCWPin) == False) and (GPIO.input(stepCWPin) == False):
		if num > 0:
			setLetter(11)
			backwards(int(delay) / 1000.0, num)
		elif num < 0:
			setLetter(15)
			forward(int(delay) / 1000.0, abs(num))
		else: time.sleep(.5)
		num = 0
	if sevenseg: setNumber(num)
