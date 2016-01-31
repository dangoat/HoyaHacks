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

    debug = True
    SCROLL_THRESHOLD = 5
    AVG = 10
    count = 0
    action = None
    use_vertscroll = True
    roll_offset = math.pi/2 - .8
    vert_scroll_limit = math.pi/8
    last_click = 0
    clicked = False
    
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
                index_finger = controller.frame(i).fingers.finger_type(Finger.TYPE_INDEX)[0]
#                index_finger = indexFingerList[0]
                 
#===============================================================================
#                 pinky_finger = controller.frame(i).fingers.finger_type(Finger.TYPE_PINKY)[0]
#                 #pinky_finger = pinky_fingerList[0]                 
# 
#                 if(pinky_finger.is_valid and pinky_finger.direction.z < 0):
#                     if(time.time() - self.last_click > 1):
#                         print "last %d" , self.last_click
#                         print "this %d" , time.time()
#                         self.action.click(index_finger)
#                         self.clicked = True
#                         self.last_click = time.time()
#                         
#                 if(not pinky_finger.is_valid or not pinky_finger.direction.z < 0):
#                     if(self.clicked == True):
#                         self.clicked = False
#                         self.action.unclick(index_finger)        
#===============================================================================
                 
                if (index_finger.is_valid and index_finger.direction.z < 0):
                    average += index_finger.tip_position
                    valid_fingers += 1

#===============================================================================
#                 if(self.use_vertscroll): 
#                     prev_finger = controller.frame(i+1).fingers.finger_type(Finger.TYPE_INDEX)[0]
#                     if (prev_finger.is_valid and index_finger.is_valid):
#                         diff = prev_finger.tip_position.y - index_finger.tip_position.y
#                        # print diff
#        
#                         if ( math.fabs(diff) > self.SCROLL_THRESHOLD ):
#                             self.action.scroll(math.copysign(1,-diff))
# 
#                 elif index_finger.is_valid and index_finger.type == Leap.Finger.TYPE_INDEX:
#                     roll = finger.direction.roll + self.roll_offset
#                     if math.fabs(roll) > self.vert_scroll_limit:
#                         self.action.scroll(self.vert_scroll_limit-roll)
#                         print roll
#===============================================================================
                  
            average /= valid_fingers
            if not valid_fingers == 0:              
                self.action.point(average)
            count = 0
              
        else:
            self.count += 1

