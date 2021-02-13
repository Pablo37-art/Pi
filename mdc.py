import RPi.GPIO as GPIO
import sys
import time

def dc_motor_on(time_on=5):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(31,GPIO.OUT)
	GPIO.setup(32,GPIO.OUT)
	GPIO.setup(33,GPIO.OUT)

	GPIO.setup(37,GPIO.OUT)
	GPIO.setup(38,GPIO.OUT)
	GPIO.setup(35,GPIO.OUT)

	GPIO.output(31, GPIO.HIGH)
	GPIO.output(32, GPIO.HIGH)
	GPIO.output(37, GPIO.HIGH)
	GPIO.output(35, GPIO.HIGH)
	try:
		time.sleep(time_on)
		GPIO.output(31, GPIO.LOW)
		GPIO.output(37, GPIO.LOW)
		GPIO.cleanup()
	except KeyboardInterrupt:
		GPIO.cleanup()
		exit()
