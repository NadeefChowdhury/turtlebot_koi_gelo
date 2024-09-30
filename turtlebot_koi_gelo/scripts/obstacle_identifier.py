#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
class obstacle_identifier:
    def __init__(self) -> None:
        rospy.init_node("obstacle_identifier", anonymous=True)
        self.pub = rospy.Publisher('/obstacle', String, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, self.callback)
    
    def callback(self, obstacle):
        for range in obstacle.ranges:
            if(abs(range)<30):
                print(obstacle.ranges)
                self.pub.publish("Obstacle Found")
if __name__=='__main__':
    node = obstacle_identifier()
    rospy.spin()