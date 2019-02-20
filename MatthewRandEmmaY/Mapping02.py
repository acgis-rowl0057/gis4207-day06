#-------------------------------------------------------------------------------
# Name:        Mapping02
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

def setActiveView():
    mxd.activeView = "World"


setActiveView()

