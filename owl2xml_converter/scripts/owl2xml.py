#!/usr/bin/python
" author: Fereshta Yazdani"

import os, sys
import os.path

inFile = sys.argv[1]
outFile = sys.argv[2]
array = []
map_name = []
position = []
orientation = []
temp_array = []
temp_array2 = []
temp_array3 = []
count = 0
iss = 1
j = 0
iterator3 = -4
iterator2 = -1
iterator1 = -2
    
# Path to be created
path = "./defs"

if os.path.exists(path):
    print "directory already exist"
else:
    os.mkdir( path, 0755 );

with open(inFile,'r') as i:
    lines = i.readlines()

###FOR THE PATHS
for line in lines:
    if iterator2 == -1 or iterator1 == -2 or iterator1 == -1:
        iterator2 = iterator2+1
        iterator1= iterator1+1
    else:
        temp2= lines[iterator2]
        temp3= lines[iterator1]
        if "owl:NamedIndividual rdf:about=\"&knowrob;" in temp3 and "rdf:type rdf:resource=\"&knowrob;" in temp2 and "knowrob:heightOfObject rdf:datatype=" in line:
            so = temp3.split(";")
            so1 = so[1].split("\"")
            to = temp2.split(";")
            to1 = to[1].split("\"")
            temp_array.append(so1[0])
            temp_array.append(to1[0])
        iterator2 = iterator2+1
        iterator1 = iterator1+1

for line in lines:
    if iterator3 == -4 or iterator3 == -3 or iterator3 == -2 or iterator3 == -1:
        iterator3 = iterator3+1
    else:
        tempo= lines[iterator3]
        if "rdf:Description rdf:about=" in tempo and "owl:hasValue rdf:datatype" in line:
            ao = tempo.split(";")
            ao1 = ao[1].split("\"")
            bo = line.split(">")
           # print bo
            bo1 = bo[1].split("</")
           # print bo1
            temp_array2.append(ao1[0])
            temp_array2.append(bo1[0])
        iterator3 = iterator3+1
#print len(temp_array)
#print iss
while (iss < len(temp_array) ):
    j = 0
    z = 0
    y = iss -1
    while (j < len(temp_array2)):
        if temp_array[iss] == temp_array2[j]:
            temp_array3.append(temp_array[y])
            z=j+1
            temp_array3.append(temp_array2[z])
        j = j + 2
    iss = iss +2
#print temp_array
#print temp_array2
#print temp_array3

with open(path+"/"+outFile,'w') as o:
    for line in lines:
        if line == "<?xml version=\"1.0\"?>\n":
            o.write(line+"\n")
        #if "<owl:NamedIndividual rdf:about=\"http://knowrob.org/kb/ias_semantic_map.owl#SemanticEnvironmentMap_PM582j\">" in line:
            o.write("<robot name=\"map\" xmlns:xacro=\"http://www.ros.org/wiki/xacro\">\n\n")           
        if "<owl:NamedIndividual rdf:about=\"&knowrob;" in line:
            tmp2 = line.split(";")
            tmp3 = tmp2[1].split("\"")
            array.append(tmp3[0])
        if "<knowrob:m03 rdf:datatype=" in line:
            tester1 = line.split(">")
            tester2 = tester1[1].split("<")
            position.append(tester2[0])
        if "<knowrob:m13 rdf:datatype=" in line:
            tester1 = line.split(">")
            tester2 = tester1[1].split("<")
            position.append(tester2[0])
        if "<knowrob:m23 rdf:datatype=" in line:
            tester1 = line.split(">")
            tester2 = tester1[1].split("<")
            position.append(tester2[0])
            

    for pointer in array:
        if pointer == "VectorX" or pointer == "VectorXneg" or pointer == "VectorTable" or "SemanticMapPerception" in pointer or "RotationMatrix3D" in pointer:
            temp = "test"
        else:
            o.write("<xacro:include filename=\"./defs/"+pointer+".xml\"/>\n")
    o.write("\n<link name=\"map_link\">\n")
    o.write("</link>\n\n")
    for pointer2 in array:
        if pointer2 == "VectorX" or pointer2 == "VectorXneg" or pointer2 == "VectorTable" or "SemanticMapPerception" in pointer2 or "RotationMatrix3D" in pointer2:
            temp ="test2"
        else:
            o.write("<"+pointer2+"/>\n")
    o.write("\n</robot>\n")

with open(path+"/"+outFile,'r') as os:
    newlines = os.readlines()

#print newlines
for index in newlines:
    if "./defs" in index:
        temp1 = index.split("defs/")
      #  print "mama"
       # temp2 = temp1[1].split("\"")
     #   map_name = temp2[0]
        temp3 = temp1[1].split(".")
        temp4 = temp3[0]
        map_name = temp4
        temp5 = ''
        temp6 = 0
        temp7 = 0
        while (temp5 == ''):
            #print temp4
         #   print "verar"
        #    print temp_array3[temp6]
            if temp4 == temp_array3[temp6]:
                temp7 = temp6 + 1
                temp5 = temp_array3[temp7]
            temp6 = temp6 + 2
        #print temp5
        with open(path+"/"+map_name+".xml",'w') as o:
            o.write("<?xml version=\"1.0\"?>\n")
            o.write("<robot xmlns:sensor=\"http://playerstage.sourceforge.net/gazebo/xmlschema/#sensor\"\n")
            o.write("xmlns:controller=\"http://playerstage.sourceforge.net/gazebo/xmlschema/#controller\"\n")
            o.write("xmlns:interface=\"http://playerstage.sourceforge.net/gazebo/xmlschema/#interface\"\n")
            o.write("xmlns:xacro=\"http://www.ros.org/wiki/xacro\">\n\n")
            o.write("<material name=\"Blue\">\n")
            o.write("<color rgba=\"0.0 0.0 0.8 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"DarkGreen\">\n")
            o.write("<color rgba=\"0.0 0.5 0.0 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"Green\">\n")
            o.write("<color rgba=\"0.0 0.8 0.0 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"Grey\">\n")
            o.write("<color rgba=\"0.7 0.7 0.7 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"Grey2\">\n")
            o.write("<color rgba=\"0.9 0.9 0.9 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"Red\">\n")
            o.write("<color rgba=\"0.8 0.0 0.0 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"White\">\n")
            o.write("<color rgba=\"1.0 1.0 1.0 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"Black\">\n")
            o.write("<color rgba=\"0.1 0.1 0.1 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"LightGrey\">\n")
            o.write("<color rgba=\"0.6 0.6 0.6 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<material name=\"DarkOrange\">\n")
            o.write("<color rgba=\"0.8 0.5 0.0 1.0\"/>\n")
            o.write("</material>\n\n")
            o.write("<macro name=\""+temp4+"\">\n\n")
            o.write("<joint name=\""+temp4+"_joint\" type=\"fixed\">\n")
            o.write("<origin xyz=\"0 0 0\" rpy=\"0 0 0\"/>\n")
            o.write("<parent link=\"map_link\"/>\n")
            o.write("<child link=\""+temp4+"_link\"/>\n")
            o.write("</joint>\n\n")
            o.write("<link name=\""+temp4+"_link\">\n")
            o.write("<visual>\n")
            testera = position.pop(0)
            testerb = position.pop(0)
            testerc = position.pop(0)
            
            o.write("<origin xyz=\""+testera+" "+testerb+" "+testerc+" "+"\" rpy=\"0 0 0\"/>\n")
            o.write("<geometry>\n")
            o.write("<mesh filename=\""+temp5+"\"/>\n")
            o.write("</geometry>\n")
            o.write("<material name=\"Green\"/>\n")
            o.write("</visual>\n")
            o.write("<collision>\n")
            o.write("<origin xyz=\""+testera+" "+testerb+" "+testerc+" "+"\" rpy=\"0 0 0\"/>\n")
            o.write("<geometry>\n")
            o.write("<mesh filename=\""+temp5+"\"/>\n")
            o.write("</geometry>\n")
            o.write("</collision>\n")    
            o.write("</link>\n\n")
            o.write("<gazebo>\n")
            o.write("<static>true</static>\n")
            o.write("</gazebo>\n\n")
            o.write("</macro>\n")
            o.write("</robot>\n")
