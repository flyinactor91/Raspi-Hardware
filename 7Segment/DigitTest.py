#!/usr/bin/python

##--Michael duPont (flyinactor91.com)
##--Seven-segment gpio test without using 7Segment library

import RPi.GPIO as GPIO
import time

segments = {'a': 24, 'b': 23, 'c': 18, 'd': 22, 'e': 25, 'f': 4, 'g': 17 }

GPIO.setmode(GPIO.BCM)
for s in segments:
	GPIO.setup(segments[s], GPIO.OUT)

for s in segments:
	print s , segments[s]
	GPIO.output(segments[s], True)
	time.sleep(.5)
	GPIO.output(segments[s], False)

time.sleep(1)

for i in range(3):
	for s in segments:
		GPIO.output(segments[s], True)
	time.sleep(.5)
	for s in segments:
		GPIO.output(segments[s], False)
	time.sleep(.5)
