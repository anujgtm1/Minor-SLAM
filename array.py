import numpy as np

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

np.concatenate((a,b))
x,y=4,5

np.concatenate((a,np.array([[x,y]])))


