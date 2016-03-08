from dvrk.arm import *

class guarded_move(arm):
    """Simple robot API wrapping around ROS messages
    """
    # initialize the robot
    def __init__(self, guarded_name, ros_namespace = '/dvrk/'):
        # first call base class constructor
        self._arm__init_arm(guarded_name, ros_namespace)
        # publishers
        self.set_jaw_position_publisher = rospy.Publisher(self._arm__full_ros_namespace
                                                          + '/set_jaw_position',
                                                          Float32, latch=True, queue_size = 1)

    def guarded_move_cartesian_translation(self, guarded_translation):
        while (joy_force.zero_force()):
            #new_x = guarded_translation[0]/100
            #new_y = guarded_translation[1]/100
            #new_z = guarded_translation[2]/100
            #self.delta_move_cartesian(new_x, new_y, new_z)
            print "here"
        print "done"#self.get_current_joint_position()
