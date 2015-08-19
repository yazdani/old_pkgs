#!/usr/bin/python
" author: Fereshta Yazdani"

import sys

inFile = sys.argv[1]
outFile = sys.argv[2]
array = []
map_name = []
position = []
orientation = []
with open(inFile,'r') as i:
    lines = i.readlines()
    
with open(outFile,'w') as o:
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
            o.write("<xacro:include filename=\"$(PATH_TO_THE_PACKAGE)/"+pointer+".xml\"/>\n")
    o.write("\n<link name=\"map_link\">\n")
    o.write("</link>\n\n")
    for pointer2 in array:
        if pointer2 == "VectorX" or pointer2 == "VectorXneg" or pointer2 == "VectorTable" or "SemanticMapPerception" in pointer2 or "RotationMatrix3D" in pointer2:
            temp ="test2"
        else:
            o.write("<"+pointer2+"/>\n")
    o.write("\n</robot>\n")

with open(outFile,'r') as os:
    newlines = os.readlines()

for index in newlines:
    if "PATH_TO_THE_PACKAGE" in index:
        temp1 = index.split("/")
        temp2 = temp1[1].split("\"")
        map_name = temp2[0]
        temp3 = map_name.split(".")
        temp4 = temp3[0]
        with open(map_name,'w') as o:
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
            o.write("<mesh filename=\"package://PATH_TO_MESH/tanne1.dae+\"/>\n")
            o.write("</geometry>\n")
            o.write("<material name=\"TODOCOLOR\"/>\n")
            o.write("</visual>\n")
            o.write("<collision>\n")
            o.write("<origin xyz=\""+testera+" "+testerb+" "+testerc+" "+"\" rpy=\"0 0 0\"/>\n")
            o.write("<geometry>\n")
            o.write("<mesh filename=\"package://PATH_TO_MESH/tanne1.dae+\"/>\n")
            o.write("</geometry>\n")
            o.write("</collision>\n")    
            o.write("</link>\n\n")
            o.write("<gazebo>\n")
            o.write("<static>true</static>\n")
            o.write("</gazebo>\n\n")
            o.write("</macro>\n")
            o.write("</robot>\n")
