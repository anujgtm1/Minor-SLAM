import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.pyplot as pt
import toCart as tc

a=0
b=0

def plotArray(x,a=0,b=0):
       # plt.plot(0,0)
        plt.ylim(-70,70)
	plt.xlim(-50,50)
        ax = plt.subplot()
        ax.scatter(a,b,color = 'b',linewidth = 1)
        ax.plot(x[:,0],x[:,1],color = 'r',linewidth=1)
	#ax.scatter(0,0,color = 'b',linewidth=4)
        #ax.plot(0,0,color = 'g',linewidth = 30)
	'''for i in range(0,len(x)-1):
		#ax.scatter(x[:,1],x[:,0],color = 'r',linewidth = 1)
                ax.plot(x[:,1],x[:,0],color = 'r',linewidth=1)
                ax.axis('off')'''
        ax.axis('off')
	ax.grid(False)
	plt.show()

def plotArrayl(x):
        plt.ylim(0,140)
	plt.xlim(0,100)
        ax = pt.subplot()
        data = np.array(x)
        #ax.scatter(a,b,color = 'b',linewidth = 1)
        ax.scatter(data[:,0],data[:,1],color = 'r',linewidth=1)
	#ax.scatter(0,0,color = 'b',linewidth=4)
        #ax.plot(0,0,color = 'g',linewidth = 30)
	'''for i in range(0,len(x)-1):
		#ax.scatter(x[:,1],x[:,0],color = 'r',linewidth = 1)
                ax.scatter(data[:,1],data[:,0],color = 'r',linewidth=1)
		#print(x)
           '''     
        #ax.axis('off')
	ax.grid(False)
	plt.show()
