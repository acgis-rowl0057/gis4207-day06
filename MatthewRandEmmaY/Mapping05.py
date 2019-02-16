#-------------------------------------------------------------------------------
# Name:        Mapping05
# Purpose:
#
# Author:      Matthew Rowland
#
# Created:     12-02-2019
# Copyright:   (c) rowland 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy



mxd = arcpy.mapping.MapDocument("CURRENT")

def addContinents():
    df1 = arcpy.mapping.ListDataFrames(mxd,"Canada")[0]
    addLayer = arcpy.mapping.Layer(r"D:\Semester2\gis4207_Customization_I\Data\World\Continents.lyr")
    arcpy.mapping.AddLayer(df1, addLayer, "AUTO_ARRANGE")

def addWorldCities():
    df1 = arcpy.mapping.ListDataFrames(mxd,"Canada")[0]
    addLayer = arcpy.mapping.Layer(r"D:\Semester2\gis4207_Customization_I\Data\World\World Cities.lyr")
    arcpy.mapping.AddLayer(df1, addLayer, "AUTO_ARRANGE")
addContinents()
addWorldCities()
arcpy.RefreshActiveView()
arcpy.RefreshTOC