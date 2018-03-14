#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

@file: test_interval_servo.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 Oct 10
@version: 1.0.0

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

# Value used to initialize each servo
VALUE =55

def main():
    # Creates a new board 
    board = pyfirmata.Arduino(PORT)
    
    # set up fingers as Servo Output
    thumb = board.get_pin('d:2:s')
    index = board.get_pin('d:3:s')
    middle = board.get_pin('d:4:s')
    ring = board.get_pin('d:5:s')
    pinky = board.get_pin('d:6:s') 
    wrist = board.get_pin('d:10:s')   


    beginning = time.time()

    # Wait 3 second to see the effects of the command
    print("Begin initialization")
    while(time.time() - beginning < 3):
        thumb.write(VALUE)
        index.write(VALUE)
        middle.write(VALUE)
        ring.write(VALUE)
        pinky.write(VALUE)
        wrist.write(VALUE)
    print("Initialization finished")


if __name__ == '__main__':
    main()
