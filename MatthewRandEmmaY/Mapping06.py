#-------------------------------------------------------------------------------
# Name:        Mapping06
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

def removeContinents():
    df = arcpy.mapping.ListDataFrames(mxd,"Canada")[0]
    lyr = arcpy.mapping.ListLayers(mxd,"",df)
    for layer in lyr:
        if layer.name == "Continents":
            arcpy.mapping.RemoveLayer(df,layer)

def removeWorldCities():
    df = arcpy.mapping.ListDataFrames(mxd,"Canada")[0]
    lyr = arcpy.mapping.ListLayers(mxd,"",df)
    for layer in lyr:
        if layer.name == "World Cities":
            arcpy.mapping.RemoveLayer(df,layer)

removeContinents()
removeWorldCities()
arcpy.RefreshActiveView()
arcpy.RefreshTOC()