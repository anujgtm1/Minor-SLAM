import numpy as np
import plot as pt
import interact
import toCart


class Bot():
	
	def __init__(self):
		self.Map = np.empty(shape=(0,2), dtype=np.float32)
		#Position : x, y, theta
		self.Pos = np.array([[0,0,0]], dtype=np.float32)
		self.Batch = np.empty(shape=(0,2), dtype=np.float32)
		self.a =  10
		#measured practical distance travelled upon single pulse forward movement
		return
		
	def plot(self):
		#plot the map
		pt.plotArray(self.Map)
		return
		
	def observe(self):
		#send getData signal to the arduino and get the data back
		#get data into self.Batch
		#Cartesian conversion from Polar coordinates.
		self.Batch = interact.observe()
                toCart.toCartesian(self.Batch)
                print(self.Batch)
		self.transform()
		return
	
	def transform(self):
		#manipulate the self.Batch array using the self.Pos array to use it in absolute map
		#first rotation in xy plane and then translation to the required point(current position)
		sinTheta = np.sin(np.deg2rad(self.Pos[0,2]))
		cosTheta = np.cos(np.deg2rad(self.Pos[0,2]))
		x = self.Batch[:,0] * cosTheta - self.Batch[:,1] * sinTheta
		self.Batch[:,1] = self.Batch[:,0] * sinTheta + self.Batch[:,1] * cosTheta

		self.Batch[:,0] = x + self.Pos[0,0]
		self.Batch[:,1] = self.Batch[:,1] + self.Pos[0,1]
		return
		
	def append(self):
		#append self.Batch to the self.Map
		self.Map = np.append(self.Map, self.Batch, axis=0)
		return
	
	def fwd(self):
		interact.mov_forward()
		self.Pos[0,0] += self.a*np.cos(np.deg2rad(self.Pos[0,2]))
		self.Pos[0,1] -= self.a*np.sin(np.deg2rad(self.Pos[0,2]))
		return
		
	def back(self):
		interact.mov_back()
		self.Pos[0,0] -= self.a*np.cos(np.deg2rad(self.Pos[0,2]))
		self.Pos[0,1] += self.a*np.sin(np.deg2rad(self.Pos[0,2]))
		return
	
	def left(self):
		interact.mov_left()
		#Does moving left have any effect on position?
		
		self.Pos[0,2] -= 90
		return
		
	def right(self):
		interact.mov_right()
		#Does moving right have any effect on position?
		
		self.Pos[0,2] += 90
		return
	
	def reset(self):
		self.Map = np.empty(shape=(0,2), dtype=np.float32)
		self.Pos = np.array([[0,0,0]], dtype=np.float32)
		self.Batch = np.empty(shape=(0,2), dtype=np.float32)
		return
