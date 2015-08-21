import numpy as np
import serial
import plot as pt
x = np.array([[0,0]],dtype=np.uint16)
ser = serial.Serial('/dev/ttyACM0',9600)
ser.write('0#')
for i in range(1,40):
	data = ser.readline()
	#print(data)
	#stores data in the shape [[a,b]]. a=x[0,0]. b=x[0,1]
	y = np.fromstring(data, dtype = np.uint16 , sep = ' ')
	if y.size == 2:
		if y[1]!=0:
			y = y.reshape(1,2)
			x = np.append(x, y, axis=0)
			print(y)
#delete the initialised row [[0,0]]
x=np.delete(x,(0), axis=0)
pt.plotArray(x)
ser.close()
print(x)
