class Bot():
	import numpy as np
	import plot as pt
	
	
	def __init__(self):
		self.Map = np.empty(shape=(0,2), dtype=np.float32)
		self.Pos = np.array([[0,0,0]], dtype=np.float32)
		self.Batch = np.empty(shape=(0,2), stype=np.float32)
		
	def plot(self):
		#plot the map
		pt.plotArray(self.Map)
		
	def survey(self):
		#send getData singal to the arduino and get the data back
		#get data into self.Batch
	
	def append(self):
		#manipulate the self.Batch array using the self.Pos array to use it in absolute map
		x = self.Batch[:,0] * np.cos(np.deg2rad(self.Pos[0,2])) - self.Batch[:,1] * np.sin(np.deg2rad(self.Pos[0,2]))
		self.Batch[:,1] = self.Batch[:,0] * np.sin(np.deg2rad(self.Pos[0,2])) + self.Batch[:,1] * np.cos(np.deg2rad(self.Pos[0,2]))

		self.Batch[:,0] = x + self.Pos[0,0]
		self.Batch[:,1] = self.Batch[:,1] + self.Pos[0,1]

		#append it to the self.Map
		self.Map = np.append(self.Map, self.Batch, axis=0)
		
	def reset(self):
		self.Map = np.empty(shape=(0,2), dtype=np.float32)
		self.Pos = np.array([[0,0,0]], dtype=np.float32)
		self.Batch = np.empty(shape=(0,2), stype=np.float32)
