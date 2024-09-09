#!/usr/bin/env python3

import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math

class UR5PathPlanner:
    def __init__(self):
        rospy.init_node('ur5_path_planner', anonymous=True)
        self.client = actionlib.SimpleActionClient('/eff_joint_traj_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        self.client.wait_for_server()
        self.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

    def plan_path(self):
        goal = FollowJointTrajectoryGoal()
        goal.trajectory = JointTrajectory()
        goal.trajectory.joint_names = self.joint_names

        # Example waypoints
        waypoints = [
            [0, -math.pi/2, 0, -math.pi/2, 0, 0],
            [0, -math.pi/4, math.pi/4, -math.pi/2, -math.pi/4, 0],
            [math.pi/4, -math.pi/3, math.pi/3, -math.pi/2, -math.pi/6, 0],
            [0, -math.pi/2, 0, -math.pi/2, 0, 0]
        ]

        for i, waypoint in enumerate(waypoints):
            point = JointTrajectoryPoint()
            point.positions = waypoint
            point.time_from_start = rospy.Duration(2.0 * (i + 1))
            goal.trajectory.points.append(point)

        self.client.send_goal(goal)
        self.client.wait_for_result()

if __name__ == '__main__':
    try:
        planner = UR5PathPlanner()
        planner.plan_path()
    except rospy.ROSInterruptException:
        pass
