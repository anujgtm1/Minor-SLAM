#!/usr/bin/env python3
import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setwarnings(false)

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
	
	io.setup(ECHO, io.in)
	io.setup(TRIG, io.in)
	
	return


def dist():
	#Applying 5us low and 10us high pulse to start measuring
	io.output(TRIG, io.LOW)
	time.sleep(0.0000005)


	io.output(TRIG, io.HIGH)
	time.sleep(0.000001)
	
	#ECHO pulse is proportional to the distance.

	if io.input(ECHO)==true:
		start = time.time()

	if io.input(ECHO)==false:
		stop = time.time()

	total=stop-start

	distance = total*SoundSpeed

	return distance

