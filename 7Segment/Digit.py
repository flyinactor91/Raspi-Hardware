#!/usr/bin/python

from sevensegment import *
import time
s=sevensegment.SevenSegmentDisplay()
s.set(1)
for i in range(0, 10):
	print("Displaying %d" % i)
	s.set(i)
	time.sleep(1)
s.off()
