#!/usr/bin/env python3
import Rpi.GPIO as io

#Using two pins for the control of wheels.
# SPD=>Speed control(set to PWM)
# DIR=>direction control(1 for forward and 0 for reverse)

DIR=0		#Pin for the PWM to control speed
SPD=0		#Pin for the direction
FREQ=25000	#25kHz(read somewhere that it's used above the hearing frequency) 
Speed=0		#Actual speed(duty_cycle) of the PWM.

# Speed is within values [0.0,100.0] 

def init(PIN1,PIN2):
	global SPD=PIN1
	global DIR=PIN2

	io.setup(SPD, io.out)
	io.setup(DIR, io.out)
	
	#starting p as PWM instance	
	global p= io.PWM(SPD,FREQ)
	p.start(Speed)

	return

#Change direction
def dir(D):
	io.output(DIR,D)
	return

#Change Speed
def speed(Speed):
	p.ChangeDutyCycle(Speed)
	return

def stop():
	p.stop()
	return
