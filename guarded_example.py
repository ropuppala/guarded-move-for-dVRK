from guarded_move import *
from force_sensor import *

# run rosnode spacenav_node spacenav_node - to connect controller
# run rosrun joy joy_node - to connect sensor

if (len(sys.argv) != 2):
    print sys.argv[0] + ' requires one argument, i.e. name of dVRK arm'

else:
    robotName = sys.argv[1]
    r = guarded_move(robotName)
    r.move(Vector(0.0,0.0,-0.1))
    print "Start at Position : ", r.get_desired_position().p

    goal_trans = Vector(0.01,0.05,0.0)
    goal_rot = Rotation.Identity()
    goal = Frame(goal_rot, goal_trans)
    sensor = force_sensor()
    time.sleep(0.5)
    
    if (not r.guarded_dmove_frame(goal, sensor.zero_force)):
       print "Did not reach goal 1, guard triggered : ", r.get_desired_position().p
       
       goal2_trans = Vector(-0.01,-0.05,0.0)
       goal2_rot = Rotation.Identity()
       goal2 = Frame(goal2_rot, goal2_trans)
       if (not r.guarded_dmove_frame(goal2, sensor.not_zero_force)):
           print "Did not reach goal 2, guard triggered : ", r.get_desired_position().p
       else:
           print "Reached goal 2: ", r.get_desired_position().p
    else:
        print "Reached goal 1: ", r.get_desired_position().p
