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
    FACTOR = 6
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
        # move mouse
        x,z = self.m.position()
        
        # print -10 > vec.x
        # print vec.x > 10
        # print -10 > vec.z
        # print vec.z > 10
        if ( -self.THRESHOLD > vec.x or vec.x > self.THRESHOLD):
            x += math.copysign(math.fabs(vec.x) - self.THRESHOLD, vec.x)/self.FACTOR
        if ( -self.THRESHOLD > vec.z or vec.z > self.THRESHOLD):
            z += math.copysign(math.fabs(vec.z) - self.THRESHOLD, vec.z)/self.FACTOR
        x_dim, y_dim = self.m.screen_size()
        if(x < 0): x = 0
        if(z < 0): z = 0
        if(x > x_dim): x = x_dim
        if(z > y_dim): z = y_dim
        self.m.move(int(x),int(z)) 
        if f.type == Leap.Finger.TYPE_INDEX:
            vec = f.tip_position
             
    def click(self, vec):
        x, z = self.m.position()
        self.m.press(x, z)
        
    def unclick(self, vec):
        x, z = self.m.position()
        self.m.release(x, z)

    def singleclick(self, vec):
        x, z = self.m.position()
        self.m.click(x, z, 1)
           
