import serial
from tools import *

TEMPERATURE_THRESHOLD = 28.0

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

alarm_sent = False
count = 0
while True:
	line = ser.readline().strip()
	count += 1
	print line
	if count > 5 and float(line) > TEMPERATURE_THRESHOLD:
		print "ALERT! High temperature in bed 14."
		if not alarm_sent:
			send_sms()
			alarm_sent = True