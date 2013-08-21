#!/usr/bin/python

from time import sleep
import os
import RPi.GPIO as GPIO

song1 = '' #ex  bin/clink.mp3
song2 = ''
song3 = ''

GPIO.setmode(GPIO.BCM)
GPIO.setup(23 , GPIO.IN)
GPIO.setup(24 , GPIO.IN)
GPIO.setup(25 , GPIO.IN)

while True:
	if (GPIO.input(23) == False):
		os. system('mpg321 '+song1+' &')
	if (GPIO.input(24) == False):
		os. system('mpg321 '+song2+' &')
	if (GPIO.input(25) == False):
		os. system('mpg321 '+song3+' &')
	sleep(0.2);
