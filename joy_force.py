import sys
import rospy
from geometry_msgs.msg import Wrench

class joy_force():
    def callback(self, data):
        self._f_x = data.force.x
        self._f_y = data.force.z

    def __init__(self, ros_namespace = '/joystick1/wrench'):
        self._f_x = 0.0
        self._f_y = 0.0
        self.previous = 0
        rospy.Subscriber('/joystick1/wrench', Wrench, self.callback)

    def zero_force (self):
        if (self._f_x == 0.0 and self._f_y == 0.0 and self.previous == 0):
            return True
        else:
            self.previous = False
            print 'out'
            return False
