import numpy as np

def corner(m1, c1, m2, c2):
	flag = True
	if m1*m2 == -1:
		x = (c1 - c2) / (m2 - m1)
		y = (m2*c1 - m1*c2) / (m2 - m1)
		a = [x, y]
		return flag, a
	tan = np.absolute( (m1 - m2) / (1 + m1*m2) )
	if tan <= 0.6:
		flag = False
		a = [0, 0]
		return flag, a
	x = (c1 - c2) / (m2 - m1)
	y = (m2*c1 - m1*c2) / (m2 - m1)
	a = [x, y]
	return flag, a
