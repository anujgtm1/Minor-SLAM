import serial

ser = serial.Serial('/dev/ttyACM0',9600)
ser.open()
for i in range(1,30):
	serial_data=ser.readline()
	print(serial_data)
