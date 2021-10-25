#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PointStamped

global x,y,z
def callback(msg): 
    rospy.loginfo("coordinates:x=%f y=%f" %(msg.point.x,msg.point.y))

def listener():
    rospy.init_node('goal_publisher', anonymous=True)
    rospy.point_pub = rospy.Subscriber('/clicked_point', PointStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
