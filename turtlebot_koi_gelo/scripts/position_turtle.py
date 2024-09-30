#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time

class position_turtle:
    def __init__(self) -> None:
        rospy.init_node("position_turtle", anonymous=True)
        self.pub = rospy.Publisher('/turtle_pos_xy', String, queue_size=10)
        rospy.Subscriber("/odom", Odometry, self.callback)
    
    def callback(self, position):
        x = position.pose.pose.position.x
        y = position.pose.pose.position.y
        message = f"Current position ({x},{y})"
        print(message)
        self.pub.publish(message)
        
        
    
if __name__=='__main__':
    node = position_turtle()
    rospy.spin()
    