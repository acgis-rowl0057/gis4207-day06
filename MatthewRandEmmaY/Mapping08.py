#-------------------------------------------------------------------------------
# Name:        Mapping08
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



def exportCanadaPDF():
    mxd = arcpy.mapping.MapDocument(r'D:\Semester2\gis4207_Customization_I\Data\MappingEx.mxd')
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.scale = 100000000
    arcpy.mapping.ExportToPDF(mxd, r'D:\Semester2\gis4207_Customization_I\day06\temp\Canada.PDF',df)
    del mxd

def exportWorldPDF():
    mxd = arcpy.mapping.MapDocument(r'D:\Semester2\gis4207_Customization_I\Data\MappingEx.mxd')
    df = arcpy.mapping.ListDataFrames(mxd)[1]
    df.scale = 150000000
    arcpy.mapping.ExportToPDF(mxd, r'D:\Semester2\gis4207_Customization_I\day06\temp\World.PDF',df)
    del mxd

def exportSFPDF():
    mxd = arcpy.mapping.MapDocument(r'D:\Semester2\gis4207_Customization_I\Data\MappingEx.mxd')
    df = arcpy.mapping.ListDataFrames(mxd)[2]
    arcpy.mapping.ExportToPDF(mxd, r'D:\Semester2\gis4207_Customization_I\day06\temp\SanFrancisco.PDF',df)
    del mxd

def createPDF():
    pdfPath = r'D:\Semester2\gis4207_Customization_I\day06\temp\AllMaps.PDF'
    pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfPath)
    pdfDoc.appendPages(r'D:\Semester2\gis4207_Customization_I\day06\temp\Canada.PDF')
    pdfDoc.appendPages(r'D:\Semester2\gis4207_Customization_I\day06\temp\World.PDF')
    pdfDoc.appendPages(r'D:\Semester2\gis4207_Customization_I\day06\temp\SanFrancisco.PDF')
    pdfDoc.saveAndClose()
    del pdfDoc


exportCanadaPDF()
exportWorldPDF()
exportSFPDF()
createPDF()