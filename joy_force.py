import sys
import rospy
from geometry_msgs.msg import Wrench

class joy_force():
    def callback(self, data):
        self._f_x = data.force.x
        self._f_y = data.force.y

    def __init__(self, ros_namespace = '/joystick1/wrench'):
        self._f_x = 0.0
        self._f_y = 0.0
        global previous 
        self.previous = 0
        rospy.Subscriber('/joystick1/wrench', Wrench, self.callback)
    
    def zero_force (self):
        print 'x', self._f_x
        print 'y' , self._f_y
        #global previous
        if (self.previous == 0):
            if(not self._f_x == 0.0 or not self._f_y == 0.0):
                global previous
                self.previous = 1
            return True
        else:
            self.previous = 1
            print 'out'
            return False
