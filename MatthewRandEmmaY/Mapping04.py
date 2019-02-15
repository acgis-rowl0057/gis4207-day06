#-------------------------------------------------------------------------------
# Name:        Mapping04
# Purpose:
#
# Author:      Matthew Rowland
#
# Created:     12-02-2019
# Copyright:   (c) rowland 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

mxd = arcpy.mapping.MapDocument(r'D:\Semester2\gis4207_Customization_I\Data\MappingEx.mxd')

def getPath():
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd,"",df):
            if lyr.supports("DATASOURCE"):
                desc = arcpy.Describe(lyr)
                print ("{}\t{}\t{}\t{}").format(lyr.name,lyr.dataSource,lyr.dataSource.endswith(".shp"), desc.dataType)

getPath()








