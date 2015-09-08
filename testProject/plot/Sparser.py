#Code snippet supposed to remove very close points

import numpy as np

def sparse(x, distance):
	j = 0
	a = x.shape[0]
	b = []
	while j<a:
		#Take an element
		y = np.sqrt( np.sum( ((x[j+1:]-x[j])**2), axis = 1 ) )
		#Compare it with everything behind it.
		#Append the element index to a list
		for i in range(0,a-j-1):
			if y[i] <= distance :
				b.append(j+i+1)
				x[j] +=x[j+i+1]
		#Take the average of all the near values
		if b:
			x[j] = x[j] / (len(b) + 1)
		#Remove all the remaining elements
		while b:
			x = np.delete(x, (b.pop()), axis = 0)
		a = x.shape[0]
		j = j+1
	return x
	
#x = np.array([[1,2],[3,4],[1,3],[3,5],[5,6]])
