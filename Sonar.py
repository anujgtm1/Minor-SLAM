#!/usr/bin/env python3
import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setwarnings(false)

ECHO=8
TRIG=10
SoundSpeed = 33000

io.setup(ECHO, io.in)
io.setup(TRIG, io.out)

io.output(TRIG, io.LOW)
time.sleep(0.0000005)
io.output(TRIG, io.HIGH)
time.sleep(0.000001)

if io.input(ECHO)==true:
	start = time.time()

if io.input(ECHO)==false:
	stop = time.time()

total=stop-start

distance = total*SoundSpeed

print distance

io.cleanup()

