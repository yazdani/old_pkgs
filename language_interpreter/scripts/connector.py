#!/usr/bin/env python

import socket, pickle
import rospy
import roslib
import xml.etree.ElementTree as ET 
from language_interpreter.msg import connect
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64
import tf
import sys
import os
import geometry_msgs.msg
import std_msgs.msg
import language_interpreter.msg


str2 = 0
str1 = 0
c = 0
sock = 0
c_test = 0
tr1 = 0
tr2 = 0
pub = 0
vec = 0
digit = 0
array = []
var = ''
select = ''
tmp = ''

def callback(data):
    get_Etree(data)
    socket_conTest()
    pub.publish(str1, str2, tr3, tr1, tr2)

def get_Etree(data):
    global vec
    global digit
    global select
    global var
    global tmp 
    digit = Vector3()
    digit.x = 0
    digit.y = 0
    digit.z = 0
    vec = Vector3()
    vec.x = 0.0
    vec.y = 0.0
    vec.z = 0.0
    array = []
    #Reading the data from a string
    root = ET.fromstring(data.data)
    
    for child in root:
        
        for child2 in child:
            child3 = child2.tag
            child4 = child3.split("}")
            array.append([child4[1], child2.text])
    
    #preliminary add
    for pointer in array:
        if pointer[0] == "command":
            if pointer[1] == "there":
                var = "go " + pointer[1]
            else:
                var = pointer[1]
        if pointer[0] == "direction":
            vec_array = pointer[1].split(" ")
            vec.x = float(vec_array[0])
            vec.y = float(vec_array[1])
            vec.z = float(vec_array[2])
        if pointer[0] == "selected":
            select = pointer[1]
            
        
        if pointer[0] == "data":
            tmp = var.split(" ")          
            temp = tmp[-1]
            if temp == "off" or temp == "up":
                digit.z = float(pointer[1])
                digit.x = 0.0
                digit.y = 0.0
            if temp == "down":
                digit.z = (-1) * float(pointer[1])
                digit.x = 0.0
                digit.y = 0.0
            if temp == "right":
                digit.y = float(pointer[1])
                digit.x = 0.0
                digit.z = 0.0
            if temp == "left":
                digit.y = (-1) * float(pointer[1])
                digit.x = 0.0
                digit.z = 0.0
            if temp == "there":
                digit.x = float(pointer[1])
                digit.y = 0.0
                digit.z = 0.0
      
def socket_conTest():
    global tr1
    global tr2   
    global tr3
    tr3 = select
    tr1 = vec 
    tr2 = digit
    socket_con(var)   
    check_command_type(var)

def socket_con(date):  
    global str2
    tmp = date + '\n'
    if digit:
        c.send(tmp)
        sys.stdout.flush()
        str2 = c.recv(1024)
    else:
        print("")
        
  
def check_command_type(date):
    global str1
    str1 = date 
    data = str1.split(" ")
    a = ''.join(['a', 'r', 'e'])
    b = ''.join(['d', 'o'])
    c = ''.join(['d', 'o', 'e', 's'])
    d = ''.join(['h', 'a', 'v', 'e'])
    e = ''.join(['h', 'a', 's'])
    f = ''.join(['h', 'o', 'w'])
    g = ''.join(['w', 'h', 'a', 't'])
    h = ''.join(['w', 'h', 'i', 'c', 'h'])
    i = ''.join(['w', 'h', 'e', 'r', 'e'])
    j = ''.join(['w', 'h', 'o'])
    k = ''.join(['w', 'h', 'o', 's', 'e'])
    l = ''.join(['w', 'h', 'y'])
    
    
    if data[0] == a or data[0] == b or data[0] == c or data[0] == d or data[0] == e or data[0] == f or data[0] == g or data[0] == h or data[0] == i or data[0] == j or data[0] == k or data[0] == l:
        str1 = "ask"
    else:
        str1 = "order"
        

    

    
    
def connector():
    global c
    global c_test
    global pub
    rospy.init_node('tf_transforms')
    pub = rospy.Publisher('interpreted_command',connect, queue_size=10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("yazdani", 1234))
    s.listen(1)
    server = "yazdani"
    c, address = s.accept()
    # while True:
    #     callback()
    rospy.Subscriber("HRIOut", std_msgs.msg.String, callback)
    rospy.spin()
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    # s_test.shutdown(socket.SHUT_RDWR)
    # s_test.close()  
    
if __name__ == '__main__':
    connector()
 
