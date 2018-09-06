import sys
sys.path.insert(0,"../lib/x64")
import Leap
class SampleListener(Leap.Listener):
    def on_connect(self,controller):
        print "Connected"
    def on_frame(self,controler):
        frame = controler.frame()
        print "Frame id: %d, hands: %d,fingers: %d" %(frame.id,len(frame.hands),len(frame.fingers))
def main():
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    print "Press Enter to quit...."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)
if __name__=="__main__":
    main()