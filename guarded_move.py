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
        velocity = 0.0001 #m/s^2
        rate = 50  #rate Hertz
        displacement = math.sqrt(math.pow(guarded_translation[0],2) + math.pow(guarded_translation[1],2)
                                 +math.pow(guarded_translation[2],2))
        total_time = displacement / velocity
        nb_points = total_time / rate
        delta_x = guarded_translation[0] / nb_points 
        delta_y = guarded_translation[1] / nb_points
        delta_z = guarded_translation[2] / nb_points
        #keep going until force is no longer zero, if force is no longer
        #zero
        i = 0
        while (condition_method() and i < nb_points):
            self.delta_move_cartesian_translation([delta_x, delta_y, delta_z])
            i = i+1
        if (i < nb_points):
            print "Found at Position : ", self.get_current_cartesian_position().p
        else:
            print "NOT Found at Position : ", self.get_current_cartesian_position().p
