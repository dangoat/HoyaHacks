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
                finger = controller.frame(i).fingers.frontmost
                
                pointed_fingers = controller.frame(i).fingers.extended()
                
                if(pointed_fingers.rightmost.type == Finger.TYPE_PINKY):
                    self.action.singleclick(finger)
                
                else:
                    self.action.unclick(finger)

                
                prev_finger = controller.frame(i+1).fingers.frontmost 
                if (prev_finger.is_valid and finger.is_valid):
                    diff = prev_finger.tip_position.y - finger.tip_position.y
                    print diff
   
                    if ( math.fabs(diff) > self.SCROLL_THRESHOLD ):
                        self.action.scroll(math.copysign(1,-diff))   
                
                if (finger.is_valid):
                    average += finger.tip_position
                    valid_fingers += 1
                 
            average /= valid_fingers
            if ( self.debug ):
                print "x: {0:.3f} y: {1:.3f} z: {2:.3f}".format(average.x, average.y, average.z)
            if not valid_fingers == 0:              
                self.action.mouse(average, finger)
            count = 0
              
        else:
            self.count += 1

