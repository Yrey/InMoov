# -*- coding: utf-8 -*-
"""

@file: ForceSense.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 Oct 10
@version: 1.0.0

Test of a force sense.
"""

import signal
import sys
import time
from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')
# analog_0 = board.get_pin('a:0:i')
it = util.Iterator(board)
it.start()

# Start reporting for defined pins
board.analog[0].enable_reporting()
finger = board.get_pin('d:3:s')

def signal_handler(signal, frame):
    board.exit()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def main():
    while True:
        beginning = time.time()
        nb = 0
        V = 0.0
        while(time.time() - beginning < 1):
            finger.write(70)
            st = board.analog[0].read()
            if(st != None):
                nb +=1
                V += 5000-5000*float(board.analog[0].read())

            board.pass_time(0.01)
        if(nb>0):
            V = V / (1000*float(nb))
            print([V, (10.8*V+0.208)/9.81])
    
if __name__ == '__main__':
    main()