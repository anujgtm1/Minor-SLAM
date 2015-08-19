import serial
import numpy as np

#x= np.array([])

ser = serial.Serial('/dev/ttyACM0',9600)
for i in range(1,30):
	print(i)
	data = ser.readline()
	print(data)
	
	x = np.fromstring(data, dtype = int , sep = ' ')
	print(x)
#	print(data.strip('\r\n'))
#np.append(x, np.fromstring(data, dtype=float, sep=' '))

#print(x)

