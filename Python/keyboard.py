import curses,serial
import Bot
import Sparser as sp
import plot as pt
import numpy as np
import iqd
import corner 
ser = serial.Serial('/dev/ttyACM0',9600)
a = Bot.Bot() #creates bot object
xycor = np.empty(shape = (0,2),dtype = np.float32)
# get the curses screen window
screen = curses.initscr()
# turn off input echoing
curses.noecho()
   
# respond to keys immediately (don't wait for enter)
curses.cbreak()
    
# map arrow keys to special values
screen.keypad(True)
     
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break

        elif char == ord('o'):
            a.observe()
            a.append()

        elif char == ord('i'):
		for i in range(0, len(a.m)-1):
			[flag, corner3] = corner.corner(a.m[i],a.c[i],a.m[i+1],a.c[i+1])
                        if flag == True:
				xycor = np.append(xycor,np.array(corner3),axis=0)
		xycor = np.append(xycor,[xycor[0]],axis=0)

        elif char == ord('r'):
            a.reset()

        elif char == ord('p'):
            a.plot()
            
        elif char == ord('k'):
            pt.plotArray(xycor)

        elif char == ord('s'):
            np.savetxt('test.txt', a.Map, delimiter=',') 

        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(0, 0, 'right')
            a.right()

        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left')
            a.left()

        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up')
            a.fwd()

        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down')
            a.back()
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
