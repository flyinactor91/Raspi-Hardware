#!/usr/bin/python

##--Michael duPont (flyinactor91.com)
##--Test digits on single-digit seven-segment display

from sevensegment import *
import time
s=sevensegment.SevenSegmentDisplay()
s.set(1)
for i in range(0, 10):
	print("Displaying %d" % i)
	s.set(i)
	time.sleep(1)
s.off()
