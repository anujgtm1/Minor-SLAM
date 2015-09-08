#final version yet to come.will modify (might be replaced by particle filter)
#Kalman nai ho huna lai matrix bina ko.
#simple gaussian error correcting code for correcting errors in position parameters (x,y,theta)/


# initial postition(x,y) and orientation(theta) with corresponding uncertainties
mux=0.
sigmax=100.
muy=0.
sigmay=100.
mutheta=0.
sigmatheta=100.

def measurementupdate(mu1,sigma1,mu2,sigma2):
    mu=(mu1*sigma1+mu2*sigma2)/(sigma1+sigma2)
    sigma=1/(1/sigma1+1/sigma2)
    return[mu,sigma]

def motionupdate(mu1,sigma1,mu2,sigma2):
    mu=mu1+mu2
    sigma=sigma1+sigma2
    return[mu,sigma]
    
while(1):
   
    #get motion parameters i.e by how much robot has moved and turned
    [x,y,theta]=motion()
    [mux,sigmax]=motionupdate(mux,sigmax,x,sigmax1)
    [muy,sigmay]=motionupdate(muy,sigmay,y,sigmay1)
    [mutheta,sigmatheta]=motionupdate(mutheta,sigmatheta,theta,sigmatheta1)

    #get measurement results and update 
    [x,y,theta,sigmax1,sigmay1,sigmatheta1]=measure()                          
    [mux,sigmax]=measurementupdate(mux,sigmax,x,sigmax1)
    [muy,sigmay]=measurementupdate(muy,sigmay,y,sigmay1)
    [mutheta,sigmatheta]=measurementupdate(mutheta,sigmatheta,theta,sigmatheta1)
