import numpy as np

def Corner(x, window_size):
	#The angle range [cos60, cos120]
	angle = [0.49, -0.49]
	#Window size must be even(number of elements in the window are odd)
	if window_size % 2 !=0:
		window_size +=1
	mid_point = window_size / 2
	Corners = np.empty(shape = (1,2))
	j = 0
	#Here we go sliding the window again
	while j <= x.shape[0]-window_size:
		corner = 0
		#Get the window
		window = x[j: (j + window_size)]
		corner = 0
		a = window[0]
		b = window[window_size-1]
		c = window[mid_point]
		#The vectors
		A = a - c
		B = b - c
		mA = np.sqrt(A[0]**2 + A[1]**2)
		mB = np.sqrt(B[0]**2 + B[1]**2)
		#Angle between the vectors
		cos = (A[0]*B[0] + A[1]*B[1])/(mA * mB)
		if cos >= angle[1] and cos <= angle[0] :
			a = window[mid_point - 1]
			b = window[mid_point + 1]
			c = window[mid_point]
			#The vectors
			A = a - c
			B = b - c
			mA = np.sqrt(A[0]**2 + A[1]**2)
			mB = np.sqrt(B[0]**2 + B[1]**2)
			cos1 = (A[0]*B[0] + A[1]*B[1])/(mA * mB)
			# Are the two angles measured within 30degrees of each other?
			if (np.arccos(cos) - np.arccos(cos1)) < np.sqrt((np.pi/6)**2):
				a = window[mid_point - 2]
				b = window[mid_point + 2]
				c = window[mid_point]
				#The vectors
				A = a - c
				B = b - c
				mA = np.sqrt(A[0]**2 + A[1]**2)
				mB = np.sqrt(B[0]**2 + B[1]**2)
				cos2 = (A[0]*B[0] + A[1]*B[1])/(mA * mB)
				# Are the two angles measured within 15degrees of each other?
				if (np.arccos(cos1) - np.arccos(cos2)) < np.sqrt((np.pi/12)**2):
					corner = 1
		if corner :
			Corners = np.append(Corners, window[[mid_point],:], axis = 0)
		j+=1
	Corners = np.delete(Corners, (0), axis = 0)
	return Corners
		
''' 
Test Code:
import numpy as np
import Corner
x = np.array([[5,0],[5,1][5,2],[5,3],[5,4],[5,5,][4,5],[3,5],[2,5],[1,5][0,5]])
Corner.Corner(x)
'''


