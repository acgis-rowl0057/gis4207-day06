#-------------------------------------------------------------------------------
# Name:        Mapping07
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
mxd.findAndReplaceWorkspacePaths(r'D:\Semester2\gis4207_Customization_I\Data', r'D:\Semester2\gis4207_Customization_I\day06\lab\MatthewRandEmmaY\mxdTemp')
mxd.saveACopy(r'D:\Semester2\gis4207_Customization_I\day06\lab\MatthewRandEmmaY\mxdTemp\MappingEX.mxd')

del mxd