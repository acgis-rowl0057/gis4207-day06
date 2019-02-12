#-------------------------------------------------------------------------------
# Name:        Mapping01
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

mxd.title = "arcpy.mapping module exercises"
mxd.author = "Matthew and Emma"
mxd.credits = "David Viljoen made me do it"
mxd.summary = "See Description"
mxd.description = "This document was used for practicing Python coding with the arcpy.mapping module."
mxd.tags = "arcpy.mapping.python.gis4207"

mxd.save()