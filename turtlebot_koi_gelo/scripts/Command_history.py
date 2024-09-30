#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Command_history:
    def __init__(self) -> None:
        rospy.init_node("Command_history", anonymous=True)
        rospy.Subscriber("/nadeef_command", String, self.callback)
    global commands
    commands = []
    def callback(self, command):
        global commands
        print(command)
        commands.append(command)
if __name__=='__main__':
    node = Command_history()
    rospy.spin()