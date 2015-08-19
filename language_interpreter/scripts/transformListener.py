#!/usr/bin/env python 

import rospy
import roslib
from language_interpreter.msg import transformListener
import tf
import geometry_msgs.msg
import std_msgs.msg
#from std_msgs.msg import String

#transformListener is publishing the transformation of two frames

if __name__ == '__main__':
    rospy.init_node('tf_xsens')

    listener = tf.TransformListener()
 
    pub1 = rospy.Publisher('tf_command', transformListener,queue_size=10)
    # pub2 = rospy.Publisher('tf_ForeArm', transformListener,queue_size=10)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/RightHand', '/map', rospy.Time(1419931530.5))
            (trans1,rot1) = listener.lookupTransform('/RightForearm', '/map', rospy.Time(1419931530.5))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
 
        cmd1 = geometry_msgs.msg.Transform()
        cmd2 = geometry_msgs.msg.Transform()
        str1 = std_msgs.msg.String()
        str1 = "Go there!"
        cmd1.translation.x = trans[0]
        cmd1.translation.y = trans[-1]
        cmd1.translation.z = trans[-2]
        cmd1.rotation.x = rot[0]
        cmd1.rotation.y = rot[-1]
        cmd1.rotation.z = rot[-2]
        cmd1.rotation.w = rot[-3]
        cmd2.translation.x = trans1[0]
        cmd2.translation.y = trans1[-1]
        cmd2.translation.z = trans1[-2]
        cmd2.rotation.x = rot1[0]
        cmd2.rotation.y = rot1[-1]
        cmd2.rotation.z = rot1[-2]
        cmd2.rotation.w = rot1[-3]
        test1 = str1
        test1 = cmd1
        test1 = cmd2
        
        pub1.publish(str1, cmd1, cmd2)
        rate.sleep()


