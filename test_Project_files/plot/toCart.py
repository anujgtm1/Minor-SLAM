import numpy as np

def toCartesian(x):
	y = x[:,1]*np.sin(np.deg2rad(x[:,0]))
	x[:,0] = x[:,1]*np.cos(np.deg2rad(x[:,0]))
	x[:,1] = y
	return x