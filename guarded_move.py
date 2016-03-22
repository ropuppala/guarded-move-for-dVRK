from dvrk.psm import *
import time

#for the sensor there should be a function in that class called zero_force()
#zero_force() must return False if force is not zero and True if force is zero
class guarded_move(arm):
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)

    def delta_guarded_move_cartesian_translation(self, guarded_translation, force_class):
        #intitalizing and declaring variables needed
        new_x = 0
        new_y = 0
        new_z = 0
        delta_x = guarded_translation[0]/1000
        delta_y = guarded_translation[1]/1000
        delta_z = guarded_translation[2]/1000

        #keep going until force is no longer zero, if force is no longer
        #zero
        while (force_class.zero_force()):
            new_x = delta_x + new_x
            new_y = delta_y + new_y
            new_z = delta_z + new_z

            self.delta_move_cartesian_translation([new_x, new_y, new_z])
        print "Found at Position : ", self.get_current_cartesian_position().p
