#!/usr/bin/python

##--Test button input state

import RPi.GPIO as io
import time

io.setmode(io.BCM)
switch_pin = 18
io.setup(switch_pin, io.IN)

while True:
	print io.input(switch_pin)
	time.sleep(0.2)
