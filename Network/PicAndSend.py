#!/usr/bin/python

##--Michael duPont (flyinactor91.com)
##--This program uses the official Raspberry Pi camera module to take a picture and send to the given email address

import os
from SendEmail import *

yourEmail = 'you@email.com'
emailPW = 'your_email-password'
picNum = 0

msg = """
We like it when you press our buttons.

Taken and sent with a Raspberry Pi."""

while True:
	sendTo = raw_input('Enter an email to take a picture: ')
	os.system('/opt/vc/bin/raspistill -o Picture{0}.jpg -t 0'.format(picNum))
	send_mail(yourEmail , emailPW , sendTo , 'Picture{0} Attached'.format(picNum) , msg , 'Picture{0}.jpg'.format(picNum))
	os.system('rm Picture{0}.jpg'.format(picNum))
	picNum += 1
