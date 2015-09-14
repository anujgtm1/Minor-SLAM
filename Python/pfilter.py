import math
from math import *
import random
import numpy as np
import plot as pt

landmarks  = [[0.,0.,120.,0.],[0.,90.,120.,90.],[0.0,0.0,0.0,90.0],[120.0,0.,120.,90.]]
landmark_intercept = [0.,90.,0.,120.]
world_sizex= 120
world_sizey= 90


class particle:
    def __init__(self):
        self.x = random.random() * world_sizex
        self.y = random.random() * world_sizey
        self.theta = random.random() * 2.0 * pi
        self.forward_noise = 0.5;
        self.turn_noise    = 0.05;
        self.sense_noise   = 0.5;
    
    def set(self, new_x, new_y, new_theta):
        self.x = float(new_x)
        self.y = float(new_y)
        self.theta = float(new_theta)
     
    def move(self, turn, forward):
        theta = self.theta + float(turn) + random.gauss(0.0, self.turn_noise)
        theta %= 2 * pi
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(theta) * dist)
        y = self.y + (sin(theta) * dist)
        x %= world_sizex   
        y %= world_sizey
        
        # set particle
        res = particle()
        res.set(x, y, theta)
        return res
    
    def Gaussian(self, mu, sigma, x):
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))
    
    def measurement_prob(self, measurement,lno):
        
        # calculates how likely a measurement should be
        if(lno==0):
           dist=abs(landmark_intercept[0]-self.y)
        elif(lno==1):
           dist=abs(landmark_intercept[1]-self.y) 
        elif(lno==2):
           dist=abs(landmark_intercept[2]-self.x)
        else:
           dist=abs(landmark_intercept[3]-self.x)      
        prob = self.Gaussian(dist, self.sense_noise, measurement)
        return prob
    
    def __repr__(self):
        return '[x=%.6s y=%.6s theta=%.6s]' % (str(self.x), str(self.y), str(self.theta))

#landmark_intercept stores the y-interceprt of lines 0 and 1 and x-intercept of
#line 2 and 3

def associate(m,c):
    if(math.floor(m)==0): 
        if(abs(c-landmark_intercept[0])<10):
            landmark_number=0
        else:
            landmark_number=1
    else:
        if(abs(c-landmark_intercept[2])<10):
            landmark_number=2
        else:         
            landmark_number=3
    return landmark_number  


N = 500



def particlefilterupdate(p,slope,intercept,perpendicular,forward,turn):
 p = []
 for i in range(N):
     x = particle()
     p.append(x)
 p2 = []
 
 for i in range(N):
     p2.append(p[i].move(turn, forward))
 p = p2

 w=[]
 landmark_number=associate(slope,intercept)
 for i in range(N):
    w.append(p[i].measurement_prob(perpendicular,landmark_number))


         
 p3 = []
 index = int(random.random() * N)
 beta = 0.0
 mw = max(w)
 for i in range(N):
        beta += random.random() * 2.0 * mw
        while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % N
        p3.append(p[index])
 p = p3
 #print p
 printData = []
 for i in range(len(p)):
	printData.append([p[i].x,p[i].y])
	#print(printData)	
 pt.plotArrayl(printData)
  
 return p


def duichoti():
 q=[]
 q=particlefilterupdate(q,1, 120, 20, 5, 0)
 q=particlefilterupdate(q,0,90,10,5,0)
 
   
#update(1.,0,20,10,pi)
#particlefilterupdate(1.,50,20,10,pi/2)




