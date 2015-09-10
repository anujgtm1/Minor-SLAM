# Code snippet that is supposed to remove outliers in the data.
# Not tested or verified

import numpy as np

def clearOutlier(x, window_size, n, max_votes):
	vote_array = np.zeros(window_size)
	j = 0
	
	if max_votes > window_size:
		max_votes = window_size
	
	while j <= (x.shape[0] - window_size):
		#Take the window from the main array
		window = x[j: (j + window_size)]
		#Find the mean and standard deviation of the window
		mean = np.mean(window, axis = 0)
		std = np.std(window, axis = 0)
		
		#Boolean matrix for votes
		y = np.sum((x[j: (j + window_size)] > (mean + n*std)) |
			((x[j: (j + window_size)]) < (mean - n*std)), axis = 1) 
		#Increase vote
		vote_array += y
		
		#Shift the vote_array left to coincide with the right shifting window
		vote_array = np.roll(vote_array, -1)
		#If the element leaving the voting is voted out, then delete it.
		if vote_array[window_size] > max_votes :
			x = np.delete(x, (j), axis = 0)
			#element deleted changes the index
			j-=1
		
		#New element must start with 0 votes
		vote_array[window_size] = 0
		#Next Element
		j+=1
	
	return x