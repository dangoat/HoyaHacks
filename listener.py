import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2 ** 32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append("/Users/kylem/Documents/LeapSDK/lib")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from action import Action

class ActionListener(Leap.Listener):

    AVG = 10
    count = 0
    action = None
    
    def on_init(self, controller):
        self.action = Action(controller)
        print "Initialized"

    def on_connect(self, controller):
        print "Connected" 

    def on_frame(self, controller):
        if (self.count == self.AVG):
            valid_fingers = 0
            average = Leap.Vector()

            for i in range(0, self.AVG - 1):
                finger = controller.frame(i).fingers.frontmost
                if (finger.is_valid):
                    average += finger.tip_position
                    valid_fingers += 1
                 
            average /= valid_fingers
            if not valid_fingers == 0:              
                self.action.mouse(average, finger)
            count = 0
              
        else:
            self.count += 1

