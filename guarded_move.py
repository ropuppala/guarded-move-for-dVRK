from dvrk.psm import *
import time

class guarded_move(arm):
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)

    #Guarded Move using Vector/List
    def guarded_move_cartesian_translation(self, guarded_translation, condition_method):
        if(type(guarded_translation) is list):
            if (len(guarded_translation) == 3):
                # convert into a Vector
                guarded_vector = Vector(guarded_translation[0], guarded_translation[1], guarded_translation[2])
            else:
                print "needs be in Cartesian Coordinate System [x,y,z]"
                return
        elif (type(guarded_translation) is Vector):
            guarded_vector = guarded_translation
        else:
            print "Error: Not a list or a vector"
        # convert into a Frame
        guarded_rotation = Rotation.Identity()
        guarded_frame = Frame(guarded_rotation, guarded_vector)
        print guarded_frame
        # move accordingly
        self.guarded_move_cartesian_frame(guarded_frame, condition_method)

    #Guarded Move using PyKDL Frame on default
    #velocity = 0.00001 and time_step = 0.01
    def guarded_move_cartesian_frame (self, guarded_frame, condition_method):
        #intitalizing and declaring variables needed
        velocity = 0.00001 #m/s
        time_step = 0.01  #rate in Hertz
        displacement = math.sqrt(dot(guarded_frame.p, guarded_frame.p))
        #total_time = displacement / velocity
        nb_points = (displacement / velocity) * time_step
        #delta_translation = guarded_frame.p * (1/nb_points)
        #delta_rotation = Rotation.Identity()
        delta_frame = Frame (Rotation.Identity(), guarded_frame.p * (1 / nb_points))
        i = 0
        while (condition_method() and i < nb_points):
            self.delta_move_cartesian_frame(delta_frame, True)
            i = i+1
        if (i < nb_points):
            return True
            #print "Found at Position : ", self.get_desired_cartesian_position().p
        else:
            return False
            #print "NOT Found at Position : ", self.get_desired_cartesian_position().p
