#Inter-Quartile Deviation for outlier removal
import numpy as np

def outlierRemoval(x, n):
	# x <- numpy array for given values
	# n <- tuning quantity for iqd. (float). typically 1~2.5
	x_q1 = np.percentile(x[:,0],25)
	x_q3 = np.percentile(x[:,0],75)
	y_q1 = np.percentile(x[:,1],25)
	y_q3 = np.percentile(x[:,1],75)
	x_iqd = x_q3 - x_q1
	y_iqd = y_q3 - y_q1

#	print(x_q1 - n * x_iqd)
#	print(x_q3 + n * x_iqd)
#	print(y_q1)
#	print(y_q3)
#	print(y_iqd)
#	print(n * y_iqd)
#	print(y_q1 - n * y_iqd)
#	print(y_q3 + n * y_iqd)	

	b = []
	for i in range(0,x.shape[0]-1):
		if ((x[i,0] < (x_q1 - n * x_iqd)) or (x[i,0] > (x_q3 + n * x_iqd))):
			b.append(i)
	
	while b:
		x = np.delete(x, (b.pop()), axis = 0)
	
	for i in range(0,x.shape[0]-1):
		if ((x[i,1] < y_q1 - n * y_iqd) or 
			(x[i,1] > y_q3 + n * y_iqd)):
				b.append(i)
	
	while(b):
		x = np.delete(x, (b.pop()), axis = 0)
		
	return x
	
'''
Test Code
import iqd
x = #some numpy array
x = iqd.outlierRemoval(x,2)
'''