import numpy as np 
import matplotlib.pyplot as plt
import toCart as tc
#x = np.array([[0,15],[10,15],[20,30],[30,30],[40,30],[50,15],[60,15],[70,30],[80,30],[90,40]]) 
#tc.toCartesian(x)
#ax = plt.subplot()
#for i in range(0,9):
#	ax.plot(x[:,1],x[:,0],color = 'r',linewidth = 1)
#ax. grid (True)
#plt.show()
def plotArray(x):
	ax = plt.subplot()
	#ax.plot(0,0,color = 'g',linewidth = 30)
	for i in range(0,len(x)-1):
		ax.scatter(x[:,1],x[:,0],color = 'r',linewidth = 1)
	ax.grid(True)
	plt.show()
#plotArray(tc.toCartesian(x))

