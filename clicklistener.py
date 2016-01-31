import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2 ** 32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append("/Users/kylem/Documents/LeapSDK/lib")
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Finger
from action import Action

class ClickListener(Leap.Listener):
    clicked = False
    action = None
    
    def on_init(self, controller):
        controller.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES)
        self.action = Action(controller)
        print "CL Initialized"
        
    def on_connect(self, controller):
        print "CL Connected"
    
    def on_frame(self, controller):
        frame = controller.frame();
        thumb = frame.fingers.finger_type(Finger.TYPE_THUMB)[0]
        index = frame.fingers.finger_type(Finger.TYPE_INDEX)[0]
        
        if(thumb.direction.x < 0):
            print "click %d", time.time()
            time.sleep(1)
        