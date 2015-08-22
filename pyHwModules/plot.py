Import numpy as np 
import matplotlib.pyplot as plt

r = np.arange(0,3,0.1)
theta = 2 * np.pi * r 

ax = plt.subplot(111,polar = True)
ax.plot(theta , r ,color = 'r' , linewidth = 3)
ax.set_rmax(2.0)
ax. grid (True)

ax.set_title("A line plot on a polar axis",va = 'bottom')
plt.show()
