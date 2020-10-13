#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def converter(data):
    pub = rospy.Publisher('speed_out', Twist, queue_size=10)
    rospy.loginfo('Speed in meters/second [%0.2f %0.2f %0.2f]',
                  data.linear.x, data.linear.y, data.linear.z)
    feet_hour = Twist()
    feet_hour.linear.x = 11811 * data.linear.x
    feet_hour.linear.y = 11811 * data.linear.y
    feet_hour.linear.z = 11811 * data.linear.z
    rospy.loginfo('Speed in feet/hour [%0.2f %0.2f %0.2f]',
                  feet_hour.linear.x, feet_hour.linear.y, feet_hour.linear.z)
    pub.publish(feet_hour)


def listener():
     rospy.init_node('listener', anonymous=True)
     rospy.Subscriber('speed_in', Twist, converter)
     rospy.spin()


if __name__ == '__main__':
     listener()
