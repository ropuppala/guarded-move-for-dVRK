from dvrk.psm import *
import time

class guarded_move(arm):
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)

    #Guarded Move using PyKDL Frame on default
    #velocity = 0.00001 and time_step = 0.01
    def guarded_dmove_frame(self, guarded_frame, condition_method,
                            percent_velocity = 0.1):
        max_velocity = 0.0001 #in m/s

        # check percentage
        if (percent_velocity > 0.0 and percent_velocity <= 1.0):
            velocity = percent_velocity * max_velocity
            time_step = 0.01  #rate in Hertz
            displacement = math.sqrt(dot(guarded_frame.p, guarded_frame.p))
            nb_points = (displacement / velocity) * time_step
            delta_frame = Frame (Rotation.Identity(), guarded_frame.p * (1.0 / nb_points))
            i = 0
            while (condition_method() and i < nb_points):
                self.dmove_frame(delta_frame, True)
                i = i + 1
            if (i < nb_points):
                print "Guard triggered : ", self.get_desired_position().p
                return False
            else:
                print "Goal reached : ", self.get_desired_position().p          
                return True

        else:
            print "Invalid velocity percentage"
            return False
