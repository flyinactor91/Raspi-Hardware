import RPi.GPIO as GPIO

##--This exception is thrown for numbers that are outside the range of values that a 7 segment display can display.

class NumberOutOfRange(Exception):

	def __init__(self, number):
		self.number = number

	def __str__(self):
		return repr("The number %d is outside the range of your 7 segment display" % self.number)

	def __unicode__(self):
		return u"The number %d is outside the range of your 7 segment display" % self.number


##--This is a class that controls a seven segment display attached to a Raspberry Pi's GPIO headers.
##--By default, it's assumed that the pins are wired up in the following way:
##--	- pin 11 controls segment a (the top one)
##--	- pin 12 controls segment b (the top right one)
##--	- pin 13->c, 15->d, 16->e, 18->f, 22->g.
##--These outputs are assumed to be active low, i.e. the segment lights up when the pin is turned OFF.

class SevenSegmentDisplay():

	# Mapping numbers to segments needed for displaying that number
	numbers = [
	"abcdef", #0
	"bc", #1
	"baged", #2
	"abgcd", #3
	"bcgf", #4
	"afgcd", #5
	"afgcde", #6
	"abc", #7
	"abcdefg", #8
	"abcdfg", #9
	]
	current_state = None # which means off

	##--Init with default pin mapping
	def __init__(self, segments = {'a': 24, 'b': 23, 'c': 18, 'd': 22, 'e': 25, 'f': 4, 'g': 17 }):

	GPIO.setmode(GPIO.BCM)
	self.segments = segments
	for s in self.segments:
		GPIO.setup(self.segments[s], GPIO.OUT)
	self.off()

	##--Turns the 7 segment display off
	def off(self):
		for s in self.segments: GPIO.output(self.segments[s], False)
		self.current_state = None

	##--Show some number on the 7 segment display
	def set(self, number_to_display):
		if not (0 <= number_to_display <= 9): raise NumberOutOfRange(number_to_display)
		self.off()
		segments_to_turn_on = self.numbers[number_to_display]
		for s in segments_to_turn_on: GPIO.output(self.segments[s], True)
		self.current_state = number_to_display
