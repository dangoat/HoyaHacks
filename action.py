import os, sys, inspect, thread, time, math
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from pymouse import PyMouse

class Action():

    THRESHOLD = 30
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
            
    def mouse(self, vec):
        while (check(vec)):
            # move mouse
            x,z = m.position()
            if (vec.x < 0):
                x -= 5
            else:
                x += 5
            if (vec.z < 0):
                z -= 5
            else:
                z += 5
            m.move(x,z)
            vec = controller.frame.fingers.frontmost.tip_position 
