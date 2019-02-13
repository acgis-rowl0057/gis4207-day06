#-------------------------------------------------------------------------------
# Name:        Mapping03
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

def writeToText():
    fileName = "DataFrameReport"
    completeName = os.path.join(savePath,fileName + ".txt")
    file1 = open(completeName, "w")
    file1.write ("Data Frame\tScale\tExtent\n")
    for df in arcpy.mapping.ListDataFrames(mxd):
        file1.write ("{}\t{}\t{}\n".format(df.name,df.scale,df.extent))
    file1.close()

writeToText()
