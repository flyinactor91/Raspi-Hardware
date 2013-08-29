#!/usr/bin/python

##--Michael duPont (flyinactor91.com)
##--Display increasing values on the seven-segment display

from Adafruit_7Segment import SevenSegment
import time

segment = SevenSegment(address=0x70)
num = 0
rest = float(raw_input('Step: '))
while True:
	segment.setColon((num / 10000)%2)
	segment.writeDigit(0 , (num / 1000)%10)
	segment.writeDigit(1 , (num / 100)%10)
	segment.writeDigit(3 , (num / 10)%10)
	segment.writeDigit(4 , num % 10)
	num += 1
	time.sleep(rest)
