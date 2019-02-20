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


mxd = arcpy.mapping.MapDocument("CURRENT")

def main():
    for df in arcpy.mapping.ListDataFrames(mxd):
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            if lyr.isGroupLayer:
                lyr.visible = True
                continue
            if lyr.isRasterLayer:
                lyr.visible = False
                continue
            if lyr.supports("DATASOURCE"):
                desc = arcpy.Describe(lyr)
                # DV:  Not all feature classes are SHP files
                #if lyr.dataSource.endswith(".shp"):
                if desc.shapeType == "Point":
                    lyr.visible = True
                else:
                    lyr.visible = False


    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()

main()






