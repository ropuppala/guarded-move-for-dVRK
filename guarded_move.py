from dvrk.psm import *
from joy_force import *
import time

class guarded_move(arm):
    """Simple robot API wrapping around ROS messages
    """
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)

    def guarded_move_cartesian_translation(self, guarded_translation):
        force = joy_force()
        self._delta_guarded_move_cartesian_translation(guarded_translation, force)

    def _delta_guarded_move_cartesian_translation(self, guarded_translation, force):
        i = 0
        new_x = 0
        new_y = 0
        new_z = 0
        delta_x = guarded_translation[0]/1000
        delta_y = guarded_translation[1]/1000
        delta_z = guarded_translation[2]/1000

        while (force.zero_force() and i < 100):
            new_x = delta_x + new_x
            new_y = delta_y + new_y
            new_z = delta_z + new_z

            self.delta_move_cartesian_translation([new_x, new_y, new_z])
            i = i + 1
            #time.sleep (0.01)
        print "Found :", self.get_current_joint_position()
