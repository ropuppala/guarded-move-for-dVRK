from guarded_move import *
from joy_condition import *

# run rosnode spacenav_node spacenav_node - to connect controller
# run rosrun joy joy_node - to connect sensor

if (len(sys.argv) != 2):
    print sys.argv[0] + ' requires one argument, i.e. name of dVRK arm'

else:
    robotName = sys.argv[1]
    r = guarded_move(robotName)
    r.home()
    #r.move_cartesian_translation([0.0,0.0,-0.1])
    print "Start at Position : ", r.get_desired_cartesian_position().p
    time.sleep(2)
    r.delta_guarded_move_cartesian_translation([0.1,0.0,0.0], joy_condition().zero_force)
