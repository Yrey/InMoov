#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@file: control.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 Oct 10

"""

import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import pyfirmata

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/ttyACM0'

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMax - (valueScaled * rightSpan)

def getPosHand(hand):
    pos = hand.palm_position
    return [ pos[0] , pos[1] , pos[2] ]

def getPosFinger(fingers, indice):
    tip = fingers[indice].joint_position(3)
    return [ tip[0], tip[1], tip[2]]

def getDistFinger(matHand, matFinger):
    return ((matHand[0] - matFinger[0])**2 + (matHand[1] - matFinger[1])**2 + (matHand[2] - matFinger[2])**2 )

def correctionMinMax(distance, MinMax):
    min = MinMax[0]
    max = MinMax[1]
    if distance>max:
            max=distance
    if distance<min:
        min=distance
    return [min, max]
    


def main():
    # Creates a new board 
    board = pyfirmata.Arduino(PORT)
    
    # set up fingers as Servo Output
    thumb = board.get_pin('d:6:s')
    index = board.get_pin('d:5:s')
    middle = board.get_pin('d:8:s')
    ring = board.get_pin('d:3:s')
    pinky = board.get_pin('d:2:s')  

    controller=Leap.Controller()
    while(not controller.is_connected):
        print("Waiting for connection")
    print(controller.is_connected)

    distThumb_minmax = [float("inf"), 1]
    distIndex_minmax = [float("inf"), 1]
    distMiddle_minmax = [float("inf"), 1]
    distRing_minmax = [float("inf"), 1]
    distPinky_minmax = [float("inf"), 1]


    while(controller.is_connected):
        ###initialisation
        frame = controller.frame()
        hand = frame.hands.rightmost
    
        ###Recuperation des objets
        MatHand = getPosHand(hand)
        #print(MatHand)
        MatThumb = getPosFinger(hand.fingers,0)
        #print(MatThumb)
        MatIndex = getPosFinger(hand.fingers,1)
        MatMiddle = getPosFinger(hand.fingers,2)
        MatRing = getPosFinger(hand.fingers,3)
        MatPinky = getPosFinger(hand.fingers,4)
    
        ###Calcul distances
        distThumb = getDistFinger(MatHand,MatThumb)
        distThumb_minmax = correctionMinMax(distThumb,distThumb_minmax)
        #print(distThumb)
        distIndex = getDistFinger(MatHand,MatIndex)
        distIndex_minmax = correctionMinMax(distIndex,distIndex_minmax)
        distMiddle = getDistFinger(MatHand,MatMiddle)
        distMiddle_minmax = correctionMinMax(distMiddle,distMiddle_minmax)
        distRing = getDistFinger(MatHand,MatRing)
        distRing_minmax = correctionMinMax(distRing,distRing_minmax)
        distPinky = getDistFinger(MatHand,MatPinky)
        distPinky_minmax = correctionMinMax(distPinky,distPinky_minmax)
    
        ###Calcul commande
        AngleThumb = translate(distThumb,distThumb_minmax[0],distThumb_minmax[1],30,120)
        AngleIndex = translate(distIndex,distIndex_minmax[0],distIndex_minmax[1],0,110)
        AngleMiddle = translate(distMiddle,distMiddle_minmax[0],distMiddle_minmax[1],0,120)
        AngleRing = translate(distRing,distRing_minmax[0],distRing_minmax[1],20,170)
        AnglePinky = translate(distPinky,distPinky_minmax[0],distPinky_minmax[1],30,180)

        commande = [AngleThumb, AngleIndex, AngleMiddle, AngleRing, AnglePinky]
        print(commande)
        thumb.write(AngleThumb)
        index.write(AngleIndex)
        middle.write(AngleMiddle)
        ring.write(AngleRing)
        pinky.write(AnglePinky)

if __name__ == '__main__':
    main()
