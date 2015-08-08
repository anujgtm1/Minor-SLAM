#!/usr/bin/env python3
import Rpi.GPIO as io

SRV=18
FRQ=100
CYC=0

MAX_DTY=40.0
MIN_DTY=20.0

MAX_ANG=0
MIN_ANG=170

ANG=0
DTY=ANG*(MAX_DTY-MIN_DTY)/(MAX_ANG-MIN_ANG)

def init(PIN):
	global SRV=PIN
	global p = io.PWM(SRV,FRQ)
	p.start(DTY)

	return

def ang(A):
	global ANG=A	
	global DTY=ANG*(MAX_DTY-MIN_DTY)/(MAX_ANG-MIN_ANG)
	p.ChangeDutyCycle(DTY)
	return

