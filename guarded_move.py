from dvrk.psm import *
from joy_force import *

class guarded_move(arm):
    """Simple robot API wrapping around ROS messages
    """
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)

    def guarded_move_cartesian_translation(self, guarded_translation):
        a = joy_force()
        i = 0
        while (a.zero_force() and i < 100):
            #new_x = guarded_translation[0]/100
            #new_y = guarded_translation[1]/100
            #new_z = guarded_translation[2]/100
            #self.delta_move_cartesian(new_x, new_y, new_z)
            print "here"
            i = i +1
        print "done"#self.get_current_joint_position()
