#!/usr/bin/env python3
import time
import servo

servo.init(18)
while(1):
	for i in range(20.0,40.0,0.5):
		servo.ang(i)
		time.sleep(0.05)


