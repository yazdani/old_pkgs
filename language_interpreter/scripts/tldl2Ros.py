#!/usr/bin/env python

__author__= 'Fereshta Yazdani'

import socket
import rospy
from language_interpreter.msg import tldl2Ros
from language_interpreter.msg import checkmsg
import os
import string

SERVER = 'yazdani'
BUFSIZE = 4096
iterator = []

def callback(data):
    
    iterator.pop(0)
    iterator.pop(0)
    iterator.pop(0)
    iterator.append(data.str)
    iterator.append(data.transform1)
    iterator.append(data.transform2)

def TLDL_publisher():
    
    iterator.append(0)
    iterator.append(0)
    iterator.append(0)
    pub = rospy.Publisher('tldl2Ros', tldl2Ros, queue_size=10)
    rospy.init_node('tldl2Ros')
    msg= tldl2Ros()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("yazdani", 4321))
    s.listen(1)
    
    server = "yazdani"
    try: 
         conn = s.accept()
         daty = conn[0]
         while not rospy.is_shutdown():
              data = daty.recv(4096)
              if data:
                rospy.Subscriber("internal_call", checkmsg, callback)
                pub.publish(iterator[0], data, iterator[-1], iterator[-2])
              else:
                break
         # getch()
    except Exception, e:
         alert("Something strange happened with the connection")

    s.shutdown(socket.SHUT_RDWR)
    s.close()

if __name__ == '__main__':
    TLDL_publisher()
