#!/usr/bin/env python3
import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setwarnings(0)

ECHO=8
TRIG=10
SoundSpeed = 33000

#Using pin ECH for Echo input from ultrasonic module
#Using pin TRIG for Trigger output to the ultrasonic module

def init(ECH,TRG):
	global ECHO
	ECHO=ECH
	global TRIG	
	TRIG=TRG
	global io	
	io.setup(ECHO, io.IN)
	io.setup(TRIG, io.OUT)
	
	return


def dist():
	#Applying 5us low and 10us high pulse to start measuring
	global io
	io.output(TRIG, io.LOW)
	time.sleep(0.0000005)


	io.output(TRIG, io.HIGH)
	time.sleep(0.000001)
	
	#ECHO pulse is proportional to the distance.

	while io.input(ECHO)==0:
		start=time.time()

	while io.input(ECHO)==1:
		stop=time.time()

	total=stop-start

	distance = total*SoundSpeed

	return distance

