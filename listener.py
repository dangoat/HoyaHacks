import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from action import Action

class ActionListener(Leap.Listener):

    AVG = 10
    count = 0
    Action action

    def __init__(self, a):
        self.action = a

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected" 

    def on_frame(self, controller):
        if (count == AVG):
            average = Leap.Vector()
            frame = controller.frame()
            if (!frame.fingers.is_empty()):
                valid_fingers = 0
                finger = frame.fingers.frontmost
                for i in range(0,AVG):
                    if (finger.is_valid):
                        average += finger.tip_position
                        valid_fingers++
                average /= valid_fingers
                        
        else:
            count++
