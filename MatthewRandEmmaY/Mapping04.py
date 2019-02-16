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

##mxd = arcpy.mapping.MapDocument(r'D:\Semester2\gis4207_Customization_I\Data\MappingEx.mxd')
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

##                        print "this layer is not a point feature class"
##                        print lyr.name

##                        print ("{}\t{}\t{}").format(lyr.name,lyr.dataSource, desc.datatype)

#getPath()
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()

main()






