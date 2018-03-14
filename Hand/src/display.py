#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

@file: display.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 March 15
@version: 1.0.0
Use wxPython 4.0

"""


##
# Imports
##

# General
import math
import wx
import wx.lib.stattext as ST
from wx.lib.masked import NumCtrl
import sys
import argparse


from multiprocessing import Process, Lock, Array
from testDisplay import com



##
# This class manages the window and the events for the software
class Visualizer(wx.Frame):
  
    def __init__(self, parent, title):
        super(Visualizer, self).__init__(parent, title=title, 
            size=(390, 350))
        self.lock = Lock()
        self.cmd = Array('i', range(6))
        #self.parent_conn, child_conn = Pipe()
        p = Process(target=com, args=(self.cmd, self.lock,))
        p.start()
            
        self.InitUI()
        self.SetSizeHints(550, 250, 550, 250)
        self.Centre()
        self.Show()
        
    def InitUI(self):
    
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(20)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        vboxThumb = wx.BoxSizer(wx.VERTICAL)
        stThumb = wx.StaticText(panel, label='Thumb')
        self.stThumbAngle = wx.StaticText(panel, label='Angle : 90')
        stThumb.SetFont(font)
        self.stThumbAngle.SetFont(font)
        vboxThumb.Add(stThumb, flag=wx.CENTER|wx.TOP, border=20)
        vboxThumb.Add((-1, 10))
        vboxThumb.Add(self.stThumbAngle)

        vboxIndex = wx.BoxSizer(wx.VERTICAL)
        stIndex = wx.StaticText(panel, label='Index')
        self.stIndexAngle = wx.StaticText(panel, label='Angle : 90')
        stIndex.SetFont(font)
        self.stIndexAngle.SetFont(font)
        vboxIndex.Add(stIndex, flag=wx.CENTER|wx.TOP, border=20)
        vboxIndex.Add((-1, 10))
        vboxIndex.Add(self.stIndexAngle)

        vboxMiddle = wx.BoxSizer(wx.VERTICAL)
        stMiddle = wx.StaticText(panel, label='Middle')
        self.stMiddleAngle = wx.StaticText(panel, label='Angle : 90')
        stMiddle.SetFont(font)
        self.stMiddleAngle.SetFont(font)
        vboxMiddle.Add(stMiddle, flag=wx.CENTER|wx.TOP, border=20)
        vboxMiddle.Add((-1, 10))
        vboxMiddle.Add(self.stMiddleAngle)

        hbox1.Add(vboxThumb, flag=wx.LEFT|wx.RIGHT|wx.CENTER, border=20)
        hbox1.Add(vboxIndex, flag=wx.LEFT|wx.RIGHT|wx.CENTER, border=20)
        hbox1.Add(vboxMiddle, flag=wx.LEFT|wx.RIGHT|wx.CENTER, border=20)

        vboxRing = wx.BoxSizer(wx.VERTICAL)
        stRing = wx.StaticText(panel, label='Ring')
        self.stRingAngle = wx.StaticText(panel, label='Angle : 90')
        stRing.SetFont(font)
        self.stRingAngle.SetFont(font)
        vboxRing.Add(stRing, flag=wx.CENTER|wx.TOP, border=20)
        vboxRing.Add((-1, 10))
        vboxRing.Add(self.stRingAngle)

        vboxPinky = wx.BoxSizer(wx.VERTICAL)
        stPinky = wx.StaticText(panel, label='Pinky')
        self.stPinkyAngle = wx.StaticText(panel, label='Angle : 90')
        stPinky.SetFont(font)
        self.stPinkyAngle.SetFont(font)
        vboxPinky.Add(stPinky, flag=wx.CENTER|wx.TOP, border=20)
        vboxPinky.Add((-1, 10))
        vboxPinky.Add(self.stPinkyAngle)

        vboxWrist = wx.BoxSizer(wx.VERTICAL)
        stWrist = wx.StaticText(panel, label='Wrist')
        self.stWristAngle = wx.StaticText(panel, label='Angle : 90')
        stWrist.SetFont(font)
        self.stWristAngle.SetFont(font)
        vboxWrist.Add(stWrist, flag=wx.CENTER|wx.TOP, border=20)
        vboxWrist.Add((-1, 10))
        vboxWrist.Add(self.stWristAngle)

        hbox2.Add(vboxRing, flag=wx.LEFT|wx.RIGHT|wx.CENTER, border=20)
        hbox2.Add(vboxPinky, flag=wx.LEFT|wx.RIGHT|wx.CENTER, border=20)
        hbox2.Add(vboxWrist, flag=wx.LEFT|wx.RIGHT|wx.CENTER, border=20)
        
        vbox.Add(hbox1, flag=wx.ALL|wx.CENTER, border=10)
        vbox.Add(hbox2, flag=wx.ALL|wx.CENTER, border=10)

        panel.SetSizer(vbox)

        self.timer = wx.Timer(self)
        self.timer.Start(500)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)

    def Update(self, event):
        self.lock.acquire()
        self.stThumbAngle.SetLabel("Angle : " + str(self.cmd[0]))
        self.stIndexAngle.SetLabel("Angle : " + str(self.cmd[1]))
        self.stMiddleAngle.SetLabel("Angle : " + str(self.cmd[2]))
        self.stRingAngle.SetLabel("Angle : " + str(self.cmd[3]))
        self.stPinkyAngle.SetLabel("Angle : " + str(self.cmd[4]))
        self.stWristAngle.SetLabel("Angle : " + str(self.cmd[5]))
        self.lock.release()
        self.timer.Start(500)


if __name__ == '__main__':
  
    app = wx.App()
    Visualizer(None, title='Angle values')
    app.MainLoop()