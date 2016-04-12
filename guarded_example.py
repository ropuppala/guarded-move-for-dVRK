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
    r.move_cartesian_translation([0.0,0.0,-0.1])
    print "Start at Position : ", r.get_desired_cartesian_position().p
    time.sleep(1)
    
    A = Vector(0.01,0.05,0.0)
    B = Rotation.Identity()
    move = Frame(B,A)
    if (r.guarded_move_cartesian_frame(move, joy_condition().zero_force)):
        print "Found : ", r.get_desired_cartesian_position().p
        time.sleep(1)
        next = Vector(0.01,0.0,0.0)
        r.guarded_move_cartesian_translation(next, joy_condition().zero_force)
    else:
        print "Not Found : ", r.get_desired_cartesian_position().p
        time.sleep(1)
        third = [0.0,-0.01,0.0]
        r.guarded_move_cartesian_translation(third, joy_condition().zero_force)
        print "Done : ", r.get_desired_cartesian_position().p
