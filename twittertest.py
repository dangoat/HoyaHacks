import os, sys, inspect, thread, time, json

from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append("/Users/kylem/Documents/LeapSDK/lib")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)



    def on_frame(self, controller):
        frame = controller.frame()
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_SWIPE:
                print "swiped"
                o = TwitterOAuth.read_file('creds')
                api = TwitterAPI(o.consumer_key,
                    o.consumer_secret,
                    auth_type='oAuth2')
                t = api.request('trends/place', {'id':'1'})
                print t.json()

def main():
    controller = Leap.Controller()
    listener = SampleListener()
 
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
