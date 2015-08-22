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
		#append it to the self.Map
		
	def reset(self):
		self.Map = np.empty(shape=(0,2), dtype=np.float32)
		self.Pos = np.array([[0,0,0]], dtype=np.float32)
		self.Batch = np.empty(shape=(0,2), stype=np.float32)