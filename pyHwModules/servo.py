#!/usr/bin/env python3
import RPi.GPIO as io

SRV=18
FRQ=100
CYC=0

MAX_DTY=40.0
MIN_DTY=20.0

MAX_ANG=0
MIN_ANG=170


ANG=0
DTY=(ANG-MIN_ANG)*(MAX_DTY-MIN_DTY)/(MAX_ANG-MIN_ANG)+MIN_DTY

def init(PIN):
	io.setmode(io.BOARD)
	io.setwarnings(0)
	global SRV
	SRV=PIN
	io.setup(SRV,io.OUT)
	global p
	p=io.PWM(SRV,FRQ)
	p.start(DTY)

	return

def ang(A):
	global ANG
	ANG=A
	global DTY
	DTY=(ANG-MIN_ANG)*(MAX_DTY-MIN_DTY)/(MAX_ANG-MIN_ANG)+MIN_DTY
	p.ChangeDutyCycle(DTY)
	return

