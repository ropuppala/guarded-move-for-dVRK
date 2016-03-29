from dvrk.psm import *
import time

#for the sensor there should be a function in that class called zero_force()
#zero_force() must return False if force is not zero and True if force is zero
class guarded_move(arm):
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)

    def delta_guarded_move_cartesian_translation(self, guarded_translation, condition_method):
        #intitalizing and declaring variables needed
        velocity = 0.001 #m/s^2
        rate = 20 #rate Hertz
        delta_x = (velocity * guarded_translation[0])/rate 
        delta_y = (velocity * guarded_translation[1])/rate 
        delta_z = (velocity * guarded_translation[2])/rate
        new_x = 0
        new_y = 0
        new_z = 0

        #keep going until force is no longer zero, if force is no longer
        #zero
        while (condition_method()):
            new_x = delta_x + new_x
            new_y = delta_y + new_y
            new_z = delta_z + new_z

            self.delta_move_cartesian_translation([new_x, new_y, new_z])
        print "Found at Position : ", self.get_current_cartesian_position().p
