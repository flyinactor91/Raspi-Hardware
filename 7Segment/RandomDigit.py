#!/usr/bin/python

##--Michael duPont (flyinactor91.com)
##--Display random digit to single-digit seven-segment display

from sevensegment import *
import random , time , sys

timestep = raw_input("Step: ")
try: timestep = float(timestep)
except: sys.exit("Not a number")
timestep = float(timestep)

s = sevensegment.SevenSegmentDisplay()
s.set(1)

try:
	while True:
		num = random.randint(0,9)
		s.set(num)
		#print num
		time.sleep(timestep)
except KeyboardInterrupt:
	1

s.off()
