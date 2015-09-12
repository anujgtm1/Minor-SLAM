import numpy as np
import serial
import plot as pt

def observe():
	x = np.empty(shape = (0,2), dtype=np.float32)
	ser = serial.Serial('/dev/ttyACM1',9600)
	ser.write('0#')
	for i in range(1,24):
		data = ser.readline()
		#if data == '0#':
			#break
		y = np.fromstring(data, dtype = np.float32 , sep = ' ')
		#print(data)
		if y.size == 2:
			if y[1]!=0:
				y = y.reshape(1,2)
                                x = np.append(x, y, axis=0)
                                print(y)
	ser.flushInput()
	ser.close()
        x[:,0] = 90 - x[:,0]
        x[:,1] = x[:,1]/np.cos(np.deg2rad(x[:,0]))
	return x
'''
	for i in range(1,40):
		data = ser.readline()
		#print(data)
		#stores data in the shape [[a,b]]. a=x[0,0]. b=x[0,1]
		y = np.fromstring(data, dtype = np.uint16 , sep = ' ')
		if y.size == 2:
			if y[1]!=0:
				y = y.reshape(1,2)
				x = np.append(x, y, axis=0)
				#print(y)
	#pt.plotArray(x)
	ser.close()
	#print(x)
	return x
'''

def command(s):
	ser = serial.Serial('/dev/ttyACM1',9600)
	ser.write(s)
	ser.close()
	return
	
def mov_forward():
	ser = serial.Serial('/dev/ttyACM1',9600)
	ser.write('10#')
	ser.close()
	return 
	
def mov_back():
	ser = serial.Serial('/dev/ttyACM1',9600)
	ser.write('11#')
	ser.close()
	return 

def mov_left():
	ser = serial.Serial('/dev/ttyACM1',9600)
	ser.write('12#')
	ser.close()
	return
	
def mov_right():
	ser = serial.Serial('/dev/ttyACM1',9600)
	ser.write('13#')
	ser.close()
	return 
