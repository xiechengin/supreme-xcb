#! /usr/bin/env python
# coding:utf-8

import rospy 
import math

from time import sleep

from geometry_msgs.msg import Pose2D
from waypoint_follower.msg import Waypoint, WaypointList
from waypoint_follower.msg import RunCmd

if __name__ == "__main__":
    rospy.init_node("waypoint_follower_test")

    # ros publisher
    waypoints_pub = rospy.Publisher("/follower_waypoints", WaypointList, queue_size=10)
    runcmd_pub = rospy.Publisher("/follower_run_cmd", RunCmd, queue_size=10)
    robotpose_pub = rospy.Publisher("/robot_pose", Pose2D, queue_size=1)

    # waypoints
    waypoints_list = WaypointList()
    waypoints_list.id = "id-6666"
    # UNDEFINE = 0 FORWARD = 1 BACKWARD = 2
    waypoints_list.direction = 1

    s_1100 = Waypoint()
    s_1100.index = 1100
    s_1100.pose.x = -1.82176220417
    s_1100.pose.y = 1.93016588688
    s_1100.pose.theta = -1.7

    s_1101 = Waypoint()
    s_1101.index = 1101
    s_1101.pose.x = 3
    s_1101.pose.y = 0
    s_1101.pose.theta = math.pi / 2

    s_1102 = Waypoint()
    s_1102.index = 1102
    s_1102.pose.x = 3
    s_1102.pose.y = 3
    s_1102.pose.theta = -math.pi / 2

    s_1103 = Waypoint()
    s_1103.index = 1103
    s_1103.pose.x = 5
    s_1103.pose.y = 3
    s_1103.pose.theta = math.pi / 2

    # waypoints list 1
    waypoints_list.waypoints.append(s_1100)
    #waypoints_list.waypoints.append(s_1101)
    #waypoints_list.waypoints.append(s_1102)
    #waypoints_list.waypoints.append(s_1103)

    send = False 
    rate = rospy.Rate(1)
    sleep(2)
    while not rospy.is_shutdown():
        if not send:
            send = True
            # robot_pose = Pose2D()
            # robot_pose.x = 0.
            # robot_pose.y = 0.
            # robot_pose.theta = math.pi / 2.
            # robotpose_pub.publish(robot_pose)
            # sleep(1)

            waypoints_pub.publish(waypoints_list)
            sleep(1)

            cmd = RunCmd()
            # START = 0  PAUSE = 1  CONTINUE = 2  CANCEL= 3
            cmd.cmd = 0
            cmd.max_velocity.linear.x = 0.5
            cmd.max_velocity.angular.z = 0.3
            runcmd_pub.publish(cmd)
        rate.sleep()
