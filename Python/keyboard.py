import curses,serial
ser = serial.Serial('/dev/ttyACM0',9600)
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
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(0, 0, 'right')
            ser.write('13#')
        elif char == curses.KEY_LEFT:                                                                 
            screen.addstr(0, 0, 'left')
            ser.write('12#')
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up')
            ser.write('10#')
            
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down')
            ser.write('11#')
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
