import numpy as np
import serial

x = np.array([[0,0]],dtype=np.uint16)
ser = serial.Serial('/dev/ttyACM0',9600)

for i in range(1,30):
	data = ser.readline()
	#stores data in the shape [[a,b]]. a=x[0,0]. b=x[0,1]
	y = np.fromstring(data, dtype = np.uint16 , sep = ' ').reshape((1,2))
	if y.shape == (1,2):
		x = np.append(x, y, axis=0)
#delete the initialised row [[0,0]]
x=np.delete(x,(0), axis=0)

ser.close()
print(x)