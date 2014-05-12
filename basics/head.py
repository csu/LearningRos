#!/usr/bin/env python
import roslib
roslib.load_manifest('rospy')
roslib.load_manifest('actionlib')
roslib.load_manifest('actionlib_msgs')
roslib.load_manifest('control_msgs')
import rospy
from control_msgs.msg import PointHeadAction
from control_msgs.msg import PointHeadActionGoal
from actionlib import SimpleActionClient
from actionlib_msgs.msg import GoalStatus

if __name__ == "__main__":
    rospy.init_node('gripper_test_node', anonymous=True)

    name_space = '/r_gripper_controller/gripper_action'
    head_client = SimpleActionClient(name_space, PointHeadAction)
    head_client.wait_for_server()

    head_goal = PointHeadActionGoal()
    head_goal.command.position = 0.05 #Opens the gripper, use 0.0 to close it.
    head_goal.command.max_effort = 30.0

    head_client.send_goal(head_goal)
    head_client.wait_for_result(rospy.Duration(10.0))
    if (head_client.get_state() != GoalStatus.SUCCEEDED):
        rospy.logwarn('Gripper action unsuccessful.')
