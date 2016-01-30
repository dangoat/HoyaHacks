import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2 ** 32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append("/Users/kylem/Documents/LeapSDK/lib")
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Finger
from action import Action
import math

class ActionListener(Leap.Listener):

    debug = False
    SCROLL_THRESHOLD = 5
    AVG = 10
    count = 0
    action = None
    
    def on_init(self, controller):
        controller.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES)
        self.action = Action(controller)
        print "Initialized"

    def on_connect(self, controller):
        print "Connected" 

    def on_frame(self, controller):
        if (self.count == self.AVG):
            valid_fingers = 0
            average = Leap.Vector()

            for i in range(0, self.AVG - 1):
                indexFingerList = controller.frame(i).fingers.finger_type(Finger.TYPE_INDEX)
                indexFinger = indexFingerList[0]
                 
                pinkyFingerList = controller.frame(i).fingers.finger_type(Finger.TYPE_PINKY)
                pinkyFinger = pinkyFingerList[0]
                 
                if(not pinkyFingerList.is_empty and pinkyFinger.direction.z < 0):
                    self.action.click(indexFinger)
                 
                else:
                     self.action.unclick(indexFinger)
                 
                if (not indexFingerList.is_empty and indexFinger.direction.z < 0):
                    average += indexFinger.tip_position
                    valid_fingers += 1
                  
            average /= valid_fingers
            if not valid_fingers == 0:              
                self.action.mouse(average, indexFinger)
            count = 0
              
        else:
            self.count += 1

