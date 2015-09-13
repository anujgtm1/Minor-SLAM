import numpy as np 
import matplotlib.pyplot as plt
import toCart as tc
def plotArray(x):
        plt.plot(0,0)
        plt.ylim(-100,100)
	plt.xlim(-100,100)
        ax = plt.subplot()
	#ax.scatter(0,0,color = 'b',linewidth=4)
        #ax.plot(0,0,color = 'g',linewidth = 30)
	for i in range(0,len(x)-1):
		#ax.scatter(x[:,1],x[:,0],color = 'r',linewidth = 1)
                ax.plot(x[:,1],x[:,0],color = 'r',linewidth=1)
                ax.axis('off')
	ax.grid(False)
	plt.show()
