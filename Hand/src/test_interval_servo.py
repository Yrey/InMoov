#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@file: test_interval_servo.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 Oct 10
@version: 1.0.0

Write the values of the interval [0, 180] on a defined pin
"""

import os, sys, inspect, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import pyfirmata

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/ttyACM0'

# Set the pin of the servo to test
PIN = 2


def main():
    # Creates a new board 
    board = pyfirmata.Arduino(PORT)
    
    # set up finger as Servo Output
    servo = board.get_pin('d:' + str(PIN) + ':s')  

    for i in range(0, 190, 10):
        print(i)
        beginning = time.time()

        # Wait 1 second to see the effects of the command
        while(time.time() - beginning < 1):
            servo.write(i)

if __name__ == '__main__':
    main()
