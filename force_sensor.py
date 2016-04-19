#the condition in which the dVRK robot is to stop, in
#this case it is when the force presented on joy_stick1
#is no longer zero

import sys
import rospy
from geometry_msgs.msg import Wrench

class force_sensor():
    def __init__(self, ros_namespace = '/joystick1/wrench'):
        self._f_x = 0.0
        self._f_y = 0.0
        rospy.Subscriber('/joystick1/wrench', Wrench, self.wrench_callback)

    def wrench_callback(self, data):
        self._f_x = data.force.x
        self._f_y = data.force.y

   #if the force is still zero return true
    def zero_force (self):
        if ((self._f_x == 0.0) and (self._f_y == 0.0)):
            return True
        else:
            return False

    def not_zero_force (self):
        if ((self._f_x != 0.0) or (self._f_y != 0.0)):
            return True
        else:
            return False
