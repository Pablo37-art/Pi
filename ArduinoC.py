import serial

def Ardu_On():
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	return abs(int(ser.readline()))
