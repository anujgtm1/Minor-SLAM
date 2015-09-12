from math import*
import random

landmarks = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]...]

clas particle:
    
    #constructor that randomly creates the  particles
    def _init_(self):
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.theta = random.random() * 2.0 * pi
        self.fwd_noise = 0.0;
        self.turn_noise    = 0.0;
        self.sense_noise   = 0.0;
        
    def set(self,xnew,ynew,thetanew):
        self.x=xnew;
        self.y=ynew;
        self.theta=thetanew;
        
    def set_noise( self,fwd_noise,turn_noise,sense_noise):
        self.fwd_noise=float(fwd_noise);
        self.turn_noise=float(turn_noise);
        self.sense_noise=float(sense_noise);
        
    #
    def sense(self):
           Z = []
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z
          
          
          
   def move(self,forward,turn)
       theta = (self.theta +float(turn) + random.gauss(0.0,turn_noise))%(2*pi)
       dist = float(forward)+random.gauss(0.0,fwd_noise)
       x = self.x + (cos(theta)*dist)
       y = self.y + (sin(theta)*dist) 
       
       p=particle()
       p.set(x,y,theta)
       p.set_noise(self.fwd_noise, self.turn_noise, self.sense_noise)
       return p
       
    def Gaussian(self,mu,sigma,x):
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))
    
    def measurement_prob(self,measurement):
        prob=1.0;
        for i in range(len(landmarks)):
             dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
             prob *= self.Gaussian(dist,self.sense_noise,measurement[i])
        return prob     
       
        
   #will add some further function definitions if required
   
   
N=500
p = []
for i in range(N):   #creation of particles
     r = particle()
     r.set_noise(0.05, 0.05, 5.0)
     p.append(r)

#plot the particles     

while(1):
       
    #get the distance and turn by which the robot has moved
    [forward,turn] = getmotionparameter();
       
    p2=[]
    for i in range(N):
        p2.append(p[i].move(forward,turn))
    p=p2
       
    w = []
    for i in range(N):
      w.append(p[i].measurement_prob(Z))  
      
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
    #plot the particles
      
      
           
            
            
            
            
            
            
            
            