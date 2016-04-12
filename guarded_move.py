from dvrk.psm import *
import time

class guarded_move(arm):
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)

    def guarded_move_cartesian_translation(self, guarded_translation, condition_method):
        if(self.__check_input_type(guarded_translation, [list, Vector])):
            if(type(guarded_translation) is list):
                if (self.__check_list_length(guarded_translation, 3)):
                    # convert into a Vector
                    guarded_vector = Vector(guarded_translation[0], guarded_translation[1], guarded_translation[2])
                else:
                    return
            else:
                guarded_vector = guarded_translation
            # convert into a Frame
            guarded_rotation = Rotation.Identity()
            guarded_frame = Frame(guarded_rotation, guarded_vector)
            # move accordingly
            self.guarded_move_cartesian_frame(guarded_frame, condition_method)

    def guarded_move_carteisian_frame (self, guarded_frame, condition_method):
        #intitalizing and declaring variables needed
        velocity = 0.00001 #m/s
        time_step = 0.01  #rate in Hertz
        displacement = math.sqrt(dot(guarded_frame.p, guarded_frame.p))
            #math.pow(guarded_translation[0],2) + math.pow(guarded_translation[1],2)
             #                    +math.pow(guarded_translation[2],2))
        total_time = displacement / velocity
        nb_points = total_time * time_step
        delta_translation = guarded_translation / nb_points
        i = 0
        while (condition_method() and i < nb_points):
            self.delta_move_cartesian_translation(delta_translation, False)
            i = i+1
        if (i < nb_points):
            return True
            #print "Found at Position : ", self.get_desired_cartesian_position().p
        else:
            return False
            #print "NOT Found at Position : ", self.get_desired_cartesian_position().p
