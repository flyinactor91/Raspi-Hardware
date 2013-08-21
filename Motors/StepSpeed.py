#!/usr/bin/python

import RPi.GPIO as GPIO
import time

sevenseg = False

if sevenseg:
	from Adafruit_7Segment import SevenSegment
	segment = SevenSegment(address=0x70)

GPIO.setmode(GPIO.BCM)

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
stepUpPin = 25
stepDownPin = 18
GPIO.setup(stepUpPin , GPIO.IN)
GPIO.setup(stepDownPin , GPIO.IN)

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

delay = [0,20,17,14,12,10,8,7,6,5,4,3,2]  #milliseconds
gear , count = 0 , 0
update = True

#Main Loop
while True:
	if (GPIO.input(stepUpPin) == False) and (GPIO.input(stepDownPin) == True):
		if gear < 12 and count == 15:
			gear += 1
			count = 0
			update = True
	elif (GPIO.input(stepDownPin) == False) and (GPIO.input(stepUpPin) == True):
		if gear > -12 and count == 15:
			gear = gear - 1
			count = 0
			update = True
	elif (GPIO.input(stepUpPin) == False) and (GPIO.input(stepDownPin) == False):
		gear , count = 0 , 0
		update = True
	if count < 15: count += 1
	#print gear
	if sevenseg and update:
		setNumber(gear)
		update = False
	if gear > 0: forward(int(delay[gear]) / 1000.0, 1)
	elif gear < 0: backwards(int(delay[abs(gear)]) / 1000.0, 1)
	else: time.sleep(0.1)
