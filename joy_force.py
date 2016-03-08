from joy_control import *

class joy_force():
    def callback(self, data):
        self._force_x = data.force.x
        self._force_y = data.force.z

    def __init__(self, ros_namespace = '/joystick1/wrench'):
        self._force_x = 0.0
        self._force_y = 0.0
        rospy.Subscriber('/joystick1/wrench', Joy, self.callback)

    def zero_force (self):
        if (self._force_x == 0 and self._force.y == 0):
            return True
        else:
            print 'out'
            return False
