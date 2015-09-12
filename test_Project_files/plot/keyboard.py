import curses,serial
import Bot
import Sparser as sp
import plot as pt
import numpy as np
import iqd
import corner 
ser = serial.Serial('/dev/ttyACM1',9600)
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
            [dum,dum1] = corner.corner(a.m[0],a.c[0],a.m[1],a.c[1])
            xycor = np.append(xycor,dum1,axis=0)

            [dum,dum1] = corner.corner(a.m[1],a.c[1],a.m[2],a.c[2])
            xycor = np.append(xycor,dum1,axis=0)

            [dum,dum1] = corner.corner(a.m[2],a.c[2],a.m[3],a.c[3])
            xycor = np.append(xycor,dum1,axis=0)
            
            [dum,dum1] = corner.corner(a.m[3],a.c[3],a.m[0],a.c[0])
            xycor = np.append(xycor,dum1,axis=0)
            
            [dum,dum1] = corner.corner(a.m[0],a.c[0],a.m[1],a.c[1])
            xycor = np.append(xycor,dum1,axis=0)

        elif char == ord('r'):
            a.reset()

        elif char == ord('p'):
            #a.plot()
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
