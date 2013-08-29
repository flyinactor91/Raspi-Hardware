Raspi-Hardware
==============

My public repo of programs integrating the Raspberry Pi with various types of hardware. 

Found at [https://github.com/flyinactor91/Raspi-Hardware](https://github.com/flyinactor91/Raspi-Hardware)

These programs can be used with either a Model A or Model B Raspberry Pi, but I am using only a Model B. Some programs require [my fork](https://github.com/flyinactor91/Adafruit-Raspberry-Pi-Python-Code) of [Adafruit's Raspi Library](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code).

###Notes for each folder

**7Segment**

* Contains programs designed to use seven-segment displays.
* Currently it contains programs to run the following hardware:
	* Generic single-digit seven-segment display ([*RadioShack*](http://www.radioshack.com/product/index.jsp?productId=2062557))
	* Adafruit 0.56" 4-digit seven-segment display w/I2C backpack ([*Adafruit*](https://www.adafruit.com/products/881))

**bin**

* Use this folder to store files (like mp3 and jpg) used in your other programs

**Circuit Diagrams**

* Contains pictures to help conect hardware to the Pi
* Not every program has a diagram but every piece of hardware is represented

**Motors**

* Contains programs that control different types of motors
* The servo program requires a Pi running Occidentalis v0.2 or Raspian with PWM drivers installed
* Currently it contains programs to run the following hardware:
	* Parallax continuous-rotation servo ([*RadioShack*](http://www.radioshack.com/product/index.jsp?productId=12798725))
	* Generic low-volt DC motor ([*RadioShack*](http://www.radioshack.com/product/index.jsp?productId=2102822))
	* Small reduction stepper motor ([*Adafruit*](http://www.adafruit.com/products/858))
	* L293D: Dual H-Bridge Motor Driver for DC or Steppers([*Adafruit*](http://www.adafruit.com/products/807))
	* ULN2803: 8 Channel Darlington Driver (Solenoid/Unipolar Stepper)([*Adafruit*](http://www.adafruit.com/products/970))

**Network**

* Contains programs that connect to web services
* Currently it contains programs to run the following hardware:
	* Official Raspberry Pi Camera Board ([*Adafruit*](https://www.adafruit.com/products/1367))

**Sensors**

* Contains programs that read sensor data
* Currently it contains programs to run the following hardware:
	* DS18B20 Digital temperature sensor ([*Adafruit*](http://www.adafruit.com/products/374))

**Various**

* Contains programs that don't fit any other category

###Additional Notes

In addition to the hardware listed above, the following components are required (and easy to find): cable, LEDs, resistors, buttons/switches, capacitor, photoresistor.
