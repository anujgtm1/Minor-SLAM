import numpy as np
import numpy as npp
import plot as p
x = np.array([[0,0]],dtype = np.uint16)
for i in range(1,128):
    if (i<42):
        y = [[-10,i/2]]
        x = np.append(x,y,axis=0)
    elif (i<84):

        y = [[(i-58)/2,20]]
        x = np.append(x,y,axis=0)
    else:
        y = [[16,(125-i)/2]]
        x = np.append(x,y,axis=0)
x = np.delete(x,(0),axis=0)
p.plotArray(x)
