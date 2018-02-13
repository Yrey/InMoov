#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@file: control.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 Oct 10
@version: 1.0.0

"""

import os, sys, inspect, math
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import pyfirmata

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/ttyACM0'

# Set angle interval for each servo-motor
THUMB_ANGLES = [0, 180]
INDEX_ANGLES = [0, 180]
MIDDLE_ANGLES = [0, 180]
RING_ANGLES = [0, 180]
PINKY_ANGLES = [0, 180]
WRIST_ANGLES = [0, 180]
WRIST_MINMAX_rad = [-math.pi/2, math.pi/2]

def translate(value, leftMinMax, rightMinMax, inverse):
    if(value < leftMinMax[0]):
        value = leftMinMax[0]

    # Figure out how 'wide' each range is
    leftSpan = leftMinMax[1] - leftMinMax[0]
    rightSpan = rightMinMax[1] - rightMinMax[0]
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMinMax[0]) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.

    if(inverse == True):
        return 180 - rightMinMax[1] + (valueScaled * rightSpan)
    else:
        return rightMinMax[1] - (valueScaled * rightSpan)

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
    if (distance<min) and (distance > 200):
        min=distance
    return [min, max]
    

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

    controller=Leap.Controller()
    while(not controller.is_connected):
        print("Waiting for connection")
    print(controller.is_connected)

    ### Initialization
    distThumb_minmax = [5000, 5001]
    distIndex_minmax = [5000, 5001]
    distMiddle_minmax = [5000, 5001]
    distRing_minmax = [5000, 5001]
    distPinky_minmax = [5000, 5001]
    distThumb = 0
    distIndex = 0
    distMiddle = 0
    distRing = 0
    distPinky = 0
    roll = 0

    while(controller.is_connected):
        nb_values_average = 3
        count = 0

        while(controller.is_connected and count < nb_values_average):
            ###initialization
            frame = controller.frame()
            hand = frame.hands.rightmost
            if(hand.palm_normal.roll < math.pi/2 and hand.palm_normal.roll > -math.pi/2):
                roll += hand.palm_normal.roll

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
            distThumb += getDistFinger(MatHand,MatThumb)
            #print(distThumb)
            distIndex += getDistFinger(MatHand,MatIndex)
            distMiddle += getDistFinger(MatHand,MatMiddle)
            distRing += getDistFinger(MatHand,MatRing)
            distPinky += getDistFinger(MatHand,MatPinky)

            count += 1
            
        distThumb /= count
        #print(distThumb)
        distIndex /= count
        distMiddle /= count
        distRing /= count
        distPinky /= count
        roll /= count

        ### Update min max values
        distThumb_minmax = correctionMinMax(distThumb,distThumb_minmax)
        distIndex_minmax = correctionMinMax(distIndex,distIndex_minmax) 
        distMiddle_minmax = correctionMinMax(distMiddle,distMiddle_minmax)
        distRing_minmax = correctionMinMax(distRing,distRing_minmax)
        distPinky_minmax = correctionMinMax(distPinky,distPinky_minmax)
        print distIndex_minmax
        
        ###Calcul commande
        AngleThumb = translate(distThumb,distThumb_minmax,THUMB_ANGLES, True)
        AngleIndex = translate(distIndex,distIndex_minmax,INDEX_ANGLES, True)
        AngleMiddle = translate(distMiddle,distMiddle_minmax,MIDDLE_ANGLES, True)
        AngleRing = translate(distRing,distRing_minmax,RING_ANGLES, True)
        AnglePinky = translate(distPinky,distPinky_minmax,PINKY_ANGLES, True)
        AngleWrist = translate(roll,WRIST_MINMAX_rad,WRIST_ANGLES, True)

        commande = [AngleThumb, AngleIndex, AngleMiddle, AngleRing, AnglePinky, AngleWrist]
        print(commande)
        thumb.write(AngleThumb)
        index.write(AngleIndex)
        middle.write(AngleMiddle)
        ring.write(AngleRing)
        pinky.write(AnglePinky)
        wrist.write(AngleWrist)


if __name__ == '__main__':
    main()
