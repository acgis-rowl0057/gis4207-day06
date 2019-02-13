#-------------------------------------------------------------------------------
# Name:        SaveLayerVisibility
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

mxd = arcpy.mapping.MapDocument(r'D:\Semester2\gis4207_Customization_I\Data\MappingEx.mxd')
savePath = r'D:\Semester2\gis4207_Customization_I\day06'


##fileName = "LayerVisibility"
##completeName = os.path.join(savePath,fileName + ".txt")
##file1 = open(completeName, "w")
##file1.write(getDataInfo())
##file1.close()

def getDataInfo():
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd,"",df):
            return "{}\t{}\t{}".format(df.name,lyr.name,lyr.visible)

def writeToText():
    fileName = "LayerVisibility"
    completeName = os.path.join(savePath,fileName + ".txt")
    file1 = open(completeName, "w")
    file1.write(getDataInfo())
    file1.close()

writeToText()