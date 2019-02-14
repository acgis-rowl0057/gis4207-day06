#-------------------------------------------------------------------------------
# Name:        LoadLayerVisibility
# Purpose:
#
# Author:      Matthew Rowland
#
# Created:     12-02-2019
# Copyright:   (c) rowland 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os

mxd = arcpy.mapping.MapDocument("CURRENT")
text = r'D:\Semester2\gis4207_Customization_I\day06\LayerVisibility.txt'

def changeTextBoolean():
    with open(text,'r') as file1:
        fileData = file1.read()
    fileData = fileData.replace("False", "True")
    with open(text,'w') as file1:
        file1.write(fileData)
changeTextBoolean()

##def getLayerList():
##    f = open(text,"r")
##    column = f.readlines()
##    visibility = []
##    for x in column:
##        visibility.append(x.split("\t")[1])
##    f.close()
##    print visibility
##getLayerList()

def turnOnAllLayers():
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd,"",df):
            lyr.visible = True
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

turnOnAllLayers()

