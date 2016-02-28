import serial

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
while True:
	line = ser.readline()
	if (float(line) > 28.0):
		print "FUCK"