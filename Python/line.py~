import numpy as np


def line(a):
	x = a[:,0]
	y = a[:,1]
	A = np.vstack([x, np.ones(len(x))]).T
	m, c = np.linalg.lstsq(A, y)[0]
	return m,c
