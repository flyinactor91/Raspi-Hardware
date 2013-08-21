#!/usr/bin/python

import RPi.GPIO as GPIO
import time

sevenseg = False

if sevenseg:
	from Adafruit_7Segment import SevenSegment
	segment = SevenSegment(address=0x70)

GPIO.setmode(GPIO.BCM)

delay = 5  #milliseconds

#Setup Stepper Motor
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#Setup Buttons
stepCWPin = 18
stepCCWPin = 25
GPIO.setup(stepCCWPin , GPIO.IN)
GPIO.setup(stepCWPin , GPIO.IN)

#Stepper Motor Functions
def forward(delay, steps):
	for i in range(0, steps):
		setStep(1, 0, 0, 1)
		time.sleep(delay)
		setStep(0, 1, 0, 1)
		time.sleep(delay)
		setStep(0, 1, 1, 0)
		time.sleep(delay)
		setStep(1, 0, 1, 0)
		time.sleep(delay)

def backwards(delay, steps):
	for i in range(0, steps):
		setStep(1, 0, 1, 0)
		time.sleep(delay)
		setStep(0, 1, 1, 0)
		time.sleep(delay)
		setStep(0, 1, 0, 1)
		time.sleep(delay)
		setStep(1, 0, 0, 1)
		time.sleep(delay)
 
def setStep(w1, w2, w3, w4):
	GPIO.output(coil_A_1_pin, w1)
	GPIO.output(coil_A_2_pin, w2)
	GPIO.output(coil_B_1_pin, w3)
	GPIO.output(coil_B_2_pin, w4)

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
