#!/usr/bin/env python3
import time
import servo

servo.init(18)
while(1):
	for i in range(20,40,1):
		servo.ang(i)
		time.sleep(0.5)


