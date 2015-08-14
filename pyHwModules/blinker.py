import RPi.GPIO as io
import time

io.setmode(io.BOARD)

io.setwarnings(False)

io.setup(8,io.OUT)
io.setup(10,io.OUT)

for i in range(1,30):
	io.output(8,io.HIGH)
	time.sleep(2)
	io.output(8,io.LOW)
	time.sleep(2)

io.cleanup()

