#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def hello_callback(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

rospy.init_node('hello_listener', anonymous=True)
rospy.Subscriber("/hello", String, hello_callback)
rospy.spin()
