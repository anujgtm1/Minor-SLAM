import numpy as np
import math 

def line(a):
	x = a[:,0]
	y = a[:,1]
	A = np.vstack([x, np.ones(len(x))]).T
	m, c = np.linalg.lstsq(A, y)[0]
	return m,c

def inter(a):
	
	y = a[:,0]
	x = a[:,1]
	A = np.vstack([y, np.ones(len(x))]).T
	m, xc = np.linalg.lstsq(A, x)[0]

	x = a[:,0]
	y = a[:,1]
	A = np.vstack([x, np.ones(len(x))]).T
	m, yc = np.linalg.lstsq(A, y)[0]
	
	if abs(m)<1:
		return m, yc
        else:
		return m,xc

def perp(m,c,x,y):
	d = (-m*x + y -c)/np.sqrt(1 + m**2)
	return d

