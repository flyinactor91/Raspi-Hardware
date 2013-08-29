#!/usr/bin/python

##--Michael duPont (flyinactor91.com)
##--Test program to put numbers and letters onto a seven-segment display

from Adafruit_7Segment import SevenSegment
import RPi.GPIO as io

segment = SevenSegment(address=0x70)

while True:
	position = raw_input('Position: ')
	if position == 'end': break
	elif position == 'clear':
		position = raw_input('Position: ')
		if position == 'all': segment.clear()
		else: segment.clear(int(position))
	else:
		number = raw_input('Number: ')
		'if len(number) == 1:'
		segment.writeDigit(int(position) , int(number))
		'else: print ''Must be digit'
	print segment.getBuffer()
segment.clear()
