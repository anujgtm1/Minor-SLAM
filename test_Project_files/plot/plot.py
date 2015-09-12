import numpy as np 
import matplotlib.pyplot as plt
import toCart as tc
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def plotArray(x):
    ax1.clear()
  #  for i in range(0,len(x)-1):
    ax1.scatter(x[:,1],x[:,0],color = 'b',linewidth = 0.1)
        #ax.plot(x[:,1],x[:,0],color = 'r',linewidth=1)
        #ax.axis('off')
    ax1.grid(False)
    plt.show()
#plotArray(tc.toCartesian(x))

def update(i):
    pullData = open('test.txt','r').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig,update,interval=1000)
plt.show()
