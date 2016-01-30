import os, sys, inspect, thread, time, json
sys.path.append("/Users/kylem/Documents/LeapSDK/lib")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class RudeListener(Leap.Listener):

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)


    def on_frame(self, controller):
    	# print "all fingers: " +  controller.frame().fingers.get_iterator()
    	# print "extended: " + controller.frame().fingers.extended()
    	# print "middle: " + controller.frame().fingers.extended().finger_type(Leap.Finger.TYPE_MIDDLE)
        fingers = controller.frame().fingers.extended().finger_type(Leap.Finger.TYPE_MIDDLE)
        if not fingers.is_empty:
        	# print "has fingers"
        	# print "should be happening"
        	# for finger in fingers:
        	# 	print finger.type
        	with open("imnotsurehowthisgotintherepo.txt") as f:
    			for line in f:
    				print line

def main():
    controller = Leap.Controller()
    listener = RudeListener()
 
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    time.sleep(1)
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()