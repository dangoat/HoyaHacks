import os, sys, inspect, thread, time, math
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append("/Users/kylem/Documents/LeapSDK/lib")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pymouse import PyMouse

class Action():

    THRESHOLD = 10
    MAXIMUM = 150
    controller = None
    m = PyMouse()

    def __init__(self, c):
       self.controller = c 

    def check(self, vec):
        x = math.fabs(vec.x)
        z = math.fabs(vec.z)
        if ( (x >= self.THRESHOLD or z >= self.THRESHOLD) and 
                x <= self.MAXIMUM and z <= self.MAXIMUM ): 
            return True 
        else:
            return False
            
    def mouse(self, vec, f):
        while (self.check(vec)):
            # move mouse
            x,z = self.m.position()
            
            # print -10 > vec.x
            # print vec.x > 10
            # print -10 > vec.z
            # print vec.z > 10
            if ( -10 > vec.x or vec.x > 10):
                x += math.copysign(math.fabs(vec.x) - self.THRESHOLD, vec.x)/7
            if ( -10 > vec.z or vec.z > 10):
                z += math.copysign(math.fabs(vec.z) - self.THRESHOLD, vec.z)/7
            print "x: %.3f" % x
            print "z: %.3f" % z
            self.m.move(x,z) 
            vec = f.frontmost.tip_position
             
    def click(self, vec):
        x, z = self.m.position()
        self.m.press(x, z, LEFT)
        
    def unclick(self, vec):
        x, z = self.m.position()
        self.m.release(x, z, LEFT)
