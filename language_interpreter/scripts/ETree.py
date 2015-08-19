#!/usr/bin/env python
# license removed for brevity

__author__= 'Fereshta Yazdani'

import socket, pickle
import rospy
import roslib
import xml.etree.ElementTree as ET 
from language_interpreter.msg import StringMultiArrays
from language_interpreter.msg import StringMultiArray
from geometry_msgs.msg import Vector3
import tf
import os
import geometry_msgs.msg
import std_msgs.msg
import language_interpreter.msg

array = []
var = ''
iterator = []

def main():
    global pub1
    # sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # server_address = ("yazdani",5678)
    # sock.connect(server_address)
    rospy.init_node('HRI_command')
    rate = rospy.Rate(0.1) 
    pub1 = rospy.Publisher('internal_call',language_interpreter.msg.StringMultiArrays , queue_size=10)
    rospy.Subscriber("HRIOut", std_msgs.msg.String, callback)
    rospy.spin()

def callback(data):
    ar2 = StringMultiArrays()
    ar1 = StringMultiArray()
    vec = Vector3()
    array = []
    #Reading the data from a string
    root = ET.fromstring(data.data)

    for child in root:
        for child2 in child:
                child3 = child2.tag
                child4 = child3.split("}")
                array.append([child4[1], child2.text])
   
    if len(array) == 4:
        array.append(["command", "red hawk"])

    for pointer in array:
        if pointer[0] == "command":
            var = pointer[1]
            print var
        else if pointer[0] == "gesture":
            print "you have to split first"
            vec_array = pointer[1].split(" ")
            vec.x = float(vec_array[0])
            vec.y = float(vec_array[1])
            vec.z = float(vec_array[2])
            
    ar1.str1 = array[0]
    ar1.str2 = array[1]
    ar1.str3 = array[2]
    ar1.str4 = array[3]
    ar1.str5 = array[4]
    ar2.multi.append(ar1)
    # print array[2][1]
    # iterator = ([var,vec])
    # data = pickle.dumps(iterator)
    # sock.recv(1024)
    # sock.send(data)
    pub1.publish(ar2)
    #iterator = ([])
  
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
