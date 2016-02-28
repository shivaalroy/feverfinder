import time
import serial
from tools import Tool

TEMPERATURE_THRESHOLD = 28.0

t = Tool('feverfinder','Shivaal')
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

alarm_sent = False
count = 0
while True:
	line = ser.readline().strip()
	count += 1
	print line
	if count > 5:
		t.addTemperature(float(line),int(time.time() * 1000))
		if not alarm_sent and float(line) > TEMPERATURE_THRESHOLD:
			print "ALERT! High temperature in bed 14."
			t.send_sms()
			alarm_sent = True