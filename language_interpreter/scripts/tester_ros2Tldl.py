#!/usr/bin/env python
# license removed for brevity

__author__= 'Fereshta Yazdani'

import socket, pickle
import rospy
import roslib
from language_interpreter.msg import testmsg
import tf
import os
import geometry_msgs.msg
import std_msgs.msg

def tester():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ("yazdani",5678)
    sock.connect(server_address)
    pub1 = rospy.Publisher('multimodal_command',testmsg, queue_size=10)
    rospy.init_node('tf_xsens')
    listener = tf.TransformListener()
    rate = rospy.Rate(0.1) 

    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/RightHand', '/map', rospy.Time(1419931530.5))
            (trans1,rot1) = listener.lookupTransform('/RightForearm', '/map', rospy.Time(1419931530.5))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
 
        cmd1 = geometry_msgs.msg.Transform()
        cmd2 = geometry_msgs.msg.Transform()
        cmd3 = geometry_msgs.msg.Transform()
        cmd4 = geometry_msgs.msg.Transform()
        str1 = std_msgs.msg.String()
        str1 = "Go there!"
        str2 = std_msgs.msg.String()
        str2 = "Where are victims!"
        str3 = std_msgs.msg.String()
        str3 = "Look there!"
        str4 = std_msgs.msg.String()
        str4 = "Where are you?"
       
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
        cmd3.translation.x = 0
        cmd3.translation.y = 0
        cmd3.translation.z = 0
        cmd3.rotation.x = 0
        cmd3.rotation.y = 0
        cmd3.rotation.z = 0
        cmd3.rotation.w = 0
        cmd4.translation.x = 0
        cmd4.translation.y = 0
        cmd4.translation.z = 0
        cmd4.rotation.x = 0
        cmd4.rotation.y = 0
        cmd4.rotation.z = 0
        cmd4.rotation.w = 0

        iterator = ([str1, cmd1, cmd2])       
        data = pickle.dumps(iterator)
        sock.recv(1024)
        sock.send(data)
        pub1.publish(str1, cmd1, cmd2)
        rospy.loginfo(str1)
        iterator = ([])
        rate.sleep()
        iterator = ([str2, cmd3, cmd4])       
        data = pickle.dumps(iterator)
        sock.recv(1024)   
        sock.send(data)
        pub1.publish(str2, cmd3, cmd4)
        rospy.loginfo(str2)
        iterator = ([])
        rate.sleep()

        iterator = ([str3, cmd1, cmd2])       
        data = pickle.dumps(iterator)
        sock.recv(1024)
        sock.send(data)
        pub1.publish(str3, cmd1, cmd2)
        iterator = ([])
        rospy.loginfo(str3)
        rate.sleep()

        iterator = ([str4, cmd3, cmd4])       
        data = pickle.dumps(iterator)
        sock.recv(1024)
        sock.send(data)
        pub1.publish(str4, cmd3, cmd4)
        rospy.loginfo(str4)
        iterator = ([])
        rate.sleep()

    # while not rospy.is_shutdown():
    #     hello_str1 = "Go left!"
    #     hello_str002 = "Go there!"       
    #     hello_str3 = "Where are you?"
    #     hello_str4 = "Where do you see victims?"
    #     hello_str5 = "Where are you?" 
    #     hello_str6 = "What do you see?" 
    #     hello_str7 = "Where are victims?"
    #     hello_str8 = "Do you see victims?" 
    #     hello_str9 = "What do you see?"
    #     hello_str10 = "Go left!"
    #     hello_str11 = "Go there!"
    #     hello_str12 = "Go left!" 
    #     hello_str13 = "What have you seen?" 
    #     rospy.loginfo(hello_str002)
    #     pub.publish(hello_str002)
    #     rate.sleep()
    #     rospy.loginfo(hello_str10)
    #     pub.publish(hello_str10)
    #     rate.sleep()
    #     rospy.loginfo(hello_str7)
    #     pub.publish(hello_str7)
    #     rate.sleep()
    #     rospy.loginfo(hello_str4)
    #     pub.publish(hello_str4)
    #     rate.sleep()        
    #     rospy.loginfo(hello_str5)
    #     pub.publish(hello_str5)
    #     rate.sleep()        
    #     rospy.loginfo(hello_str6)
    #     pub.publish(hello_str6)
    #     rate.sleep()        
    #     rospy.loginfo(hello_str7)
    #     pub.publish(hello_str7)
    #     rate.sleep()        
    #     rospy.loginfo(hello_str8)
    #     pub.publish(hello_str8)
        # rate.sleep()        
        # rospy.loginfo(hello_str9)
        # pub.publish(hello_str9)
        # rate.sleep()        
        # rospy.loginfo(hello_str10)
        # pub.publish(hello_str10)
        # rate.sleep()        
        # rospy.loginfo(hello_str11)
        # pub.publish(hello_str11)
        # rate.sleep()        
        # rospy.loginfo(hello_str12)
        # pub.publish(hello_str12)
        # rate.sleep()       
        # rospy.loginfo(hello_str13)
        # pub.publish(hello_str13)
        # rate.sleep()

if __name__ == '__main__':
    try:
        tester()
    except rospy.ROSInterruptException:
        pass
