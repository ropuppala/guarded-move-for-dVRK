import sys
from dvrk.psm import * 
from sensor_msgs.msg import Joy
import rospy
import time
import random
import csv
import math

class controller_move:

    def __init__(self, robotName):
        self._robot_name = robotName
        self._robot = psm(self._robot_name)
        self._last_axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self._last_buttons = [0, 0]
        self.previous_mouse_buttons = [0, 0]
        rospy.Subscriber('/spacenav/joy', Joy, self.joy_callback)
        
    def joy_callback(self, data):
        self._last_axes[:] = data.axes
        self._last_buttons[:] = data.buttons

    def mouse_positions(self):
        return self._last_axes
        
    def mouse_buttons(self):
        return self._last_buttons
    
    def move(self):
        acceleration_counter = 1.0
        gripper_closed = True

        #move to the starting point
        self._robot.move_joint_list([0.0,0.0,0.1,0.0,0.0,0.0,0.0],[0,1,2,3,4,5,6])

        while True:
            if self._last_axes[0] != 0 or self._last_axes[1] != 0 or self._last_axes[2] != 0:
                acceleration_counter += 0.03
            else:
                acceleration_counter = 1.0
            scale = acceleration_counter / 3000.0
            x = self._last_axes[0] * scale
            y = self._last_axes[1] * scale
            z = self._last_axes[2] * scale

            #move based on current position
            self._robot.delta_move_cartesian_translation([y, -x, z], False)

            #if mouse button 1 is clicked print current position
            if self.mouse_buttons()[0] == 1 and self.previous_mouse_buttons[0] == 0:
                print 'Current Position : ', self._robot.get_current_cartesian_position().p

            #if mouse button 2 is clicked open and close gripper
            if self.mouse_buttons()[1] == 1 and self.previous_mouse_buttons[1] == 0:
                if gripper_closed == True:
                    self._robot.move_joint_list([1.0],[6])
                    gripper_closed = False
                elif gripper_closed == False:
                    self._robot.move_joint_list([0.0],[6])
                    gripper_closed = True

            self.previous_mouse_buttons[:] = self.mouse_buttons()
            time.sleep(0.03) # 0.03 is 30 ms, which is the spacenav's highest output frequency

if (len(sys.argv) != 2):
    print sys.argv[0] + ' requires one argument, i.e. name of dVRK arm'
else:
    robotName = sys.argv[1]
    app = controller_move(robotName)
    app.move()
