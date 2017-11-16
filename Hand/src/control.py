#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@file: control.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 Oct 10

"""

import Leap   #, sys, thread, time
import serial

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)




controller=Leap.Controller()
while(not controller.is_connected):
    print("Waiting for connection")
print controller.is_connected
#frame = 0
distThumb_max=1
distThumb_min=100000

SERIAL = serial.Serial("/dev/ttyACM1", 9600, timeout=1)


while(controller.is_connected):
    #k+=1
    #print(k)
    #if(controller.is_connected): #controller is a Leap.Controller object
    frame = controller.frame() #The latest frame
    #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
    #          frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

    
    hand = controller.frame().hands.rightmost
    handPosition = hand.palm_position
    MatHand = [ handPosition[0] , handPosition[1] , handPosition[2] ]
    #print(MatHand)
    
    fingers = hand.fingers
    thumbTip=fingers[0].joint_position(3)
    MatThumb = [ fingers[0].joint_position(3)[0], fingers[0].joint_position(3)[1], fingers[0].joint_position(3)[2] ]
    #print(MatThumb)
    
    
    distThumb = ((MatHand[0] - MatThumb[0])**2 + (MatHand[1] - MatThumb[1])**2 + (MatHand[2] - MatThumb[2])**2 )
    print(distThumb)
    
    if distThumb>distThumb_max:
        distThumb_max=distThumb
    if distThumb<distThumb_min:
        distThumb_min=distThumb
    AngleThumb = translate(distThumb,distThumb_min,distThumb_max,0,180)
    print(AngleThumb)
    strAngleThumb = str(AngleThumb)
    SERIAL.write(strAngleThumb)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
