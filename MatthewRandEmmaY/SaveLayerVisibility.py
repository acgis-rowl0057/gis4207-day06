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

def main():
    fileName = "LayerVisibility"
    completeName = os.path.join(savePath,fileName + ".txt")
    file1 = open(completeName, "w")
    file1.write(getDataLayerInfo())
    file1.close()

def getDataLayerInfo():
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd,"",df):
            return df.name, '\t', lyr.name, '\t', lyr.visible




if __name__ == "__main__":
    main()