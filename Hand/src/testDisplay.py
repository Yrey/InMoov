#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@file: testDisplay.py
@author: Pierre Schegg & Yann Briançon
@date: 2017 March 15
@version: 1.0.0

"""

import os, sys, inspect, math, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

from multiprocessing import Process, Array, Lock


def com(cmd, lock):
    while True:
        lock.acquire()
        for i in range(len(cmd)):
            cmd[i] = cmd[i]+1
        lock.release()
        time.sleep(0.01)