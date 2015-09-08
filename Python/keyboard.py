import curses,serial
import Bot

ser = serial.Serial('/dev/ttyACM0',9600)
a = Bot.Bot() #creates bot object

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
        elif char == ord('r'):
            a.reset()

        elif char == ord('p'):
            
            a.plot()

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
