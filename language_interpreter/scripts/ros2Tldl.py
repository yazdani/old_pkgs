#!/usr/bin/env python

import socket
import rospy
#from language_interpreter.msg import ros2Tldl 
from language_interpreter.msg import testmsg
from language_interpreter.msg import checkmsg
import sys
import std_msgs.msg 
import geometry_msgs.msg

iterator = []
transform = []

def cchecker(data):
    str1 = data.str
    tr1 = data.transform1
    tr2 = data.transform2
    transform.pop(0)
    transform.pop(0)
    transform.pop(0)
 
    data = str1.split(" ")
    a = ''.join(['A', 'r', 'e'])
    b = ''.join(['D', 'o'])
    c = ''.join(['D', 'o', 'e', 's'])
    d = ''.join(['H', 'a', 'v', 'e'])
    e = ''.join(['H', 'a', 's'])
    f = ''.join(['H', 'o', 'w'])
    g = ''.join(['W', 'h', 'a', 't'])
    h = ''.join(['W', 'h', 'i', 'c', 'h'])
    i = ''.join(['W', 'h', 'e', 'r', 'e'])
    j = ''.join(['W', 'h', 'o'])
    k = ''.join(['W', 'h', 'o', 's', 'e'])
    l = ''.join(['W', 'h', 'y'])

    #TODO: This is a really ugly solution!
    if data[0] == a or data[0] == b or data[0] == c or data[0] == d or data[0] == e or data[0] == f or data[0] == g or data[0] == h or data[0] == i or data[0] == j or data[0] == k or data[0] == l:
        transform.append("ask")
    else:
        transform.append("order")

    transform.append(tr1)
    transform.append(tr2)
    
def buffer(data):
    #TODO: Really bad solution
    digit = data.str
    iterator.append(digit)
    if digit:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = ("yazdani",1234)
        # print >>sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)
        sock.send(iterator[0])
        iterator.pop(0)
        sock.shutdown(socket.SHUT_RDWR)
        # print >>sys.stderr, 'closing socket'      
        sock.close()
    else:
        print("")

def callback(data):
    pub1 = rospy.Publisher('internal_call',checkmsg, queue_size=10)
    buffer(data) 
    cchecker(data)
    pub1.publish(transform[0],transform[-1],transform[-2])
   # rospy.loginfo(data)
   
  
def listener():   
    transform.append(0)
    transform.append(0)
    transform.append(0)
    rospy.init_node('tf_transforms')
    rospy.Subscriber("multimodal_command", testmsg, callback)
    rospy.spin()
    
  

if __name__ == '__main__':
    listener()
