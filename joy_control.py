#read in from a logitech gamepad F310
import rospy
from geometry_msgs.msg import Wrench
from sensor_msgs.msg import Joy
from std_msgs.msg import Bool

joystick1_wrench_pub = rospy.Publisher('/joystick1/wrench', Wrench)
joystick2_wrench_pub = rospy.Publisher('/joystick2/wrench', Wrench)


button_a_pub = rospy.Publisher('/button_a', Bool)
button_a_old = 0
button_b_pub = rospy.Publisher('/button_b', Bool)
button_b_old = 0
button_x_pub = rospy.Publisher('/button_x', Bool)
button_x_old = 0
button_y_pub = rospy.Publisher('/button_y', Bool)
button_y_old = 0

def callback(data):
	# data is a wrench
	wrench = Wrench()
	wrench.force.z = 0.0
	wrench.torque.x = 0.0
	wrench.torque.y = 0.0
	wrench.torque.z = 0.0
	# left joystick on gamepad
	wrench.force.x = data.axes[0]
	wrench.force.y = data.axes[1]
	joystick1_wrench_pub.publish(wrench)
	# right joystick on gamepad
	wrench.force.x = data.axes[3]
	wrench.force.y = data.axes[4]
	joystick2_wrench_pub.publish(wrench)

	# button a
	global button_a_old
        if data.buttons[0] != button_a_old:
		button_a_old = data.buttons[0]
		if button_a_old == 0:
			button_a_pub.publish(False)
		else:
			button_a_pub.publish(True)
	# button b
	global button_b_old
        if data.buttons[1] != button_b_old:
		button_b_old = data.buttons[1]
		if button_b_old == 0:
			button_b_pub.publish(False)
		else:
			button_b_pub.publish(True)
	# button x
	global button_x_old
        if data.buttons[2] != button_x_old:
		button_x_old = data.buttons[2]
		if button_x_old == 0:
			button_x_pub.publish(False)
		else:
			button_x_pub.publish(True)
	# button y
	global button_y_old
        if data.buttons[3] != button_y_old:
		button_y_old = data.buttons[3]
		if button_y_old == 0:
			button_y_pub.publish(False)
		else:
			button_y_pub.publish(True)

# init the node
rospy.init_node('Joy_teleop')

# subscribe to Logitech gamepad
rospy.Subscriber("/joy", Joy, callback)

# loop forever
rospy.spin()
