#-------------------------------------------------------------------------------
# Name:        Convert ZMap to Geotiff
# Purpose:      Convert Petrel Raster ZMap grid to Geotiff
#
# Author:      rasagwara
#
# Created:     03/07/2015
# Copyright:   (c) rasagwara 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys
import subprocess

# Folder application sits in
mainPath = r'....' # File Path to gdal library

# Set gdal environment
os.environ['PATH'] = os.path.join(mainPath, 'GDAL', 'bin') + ';' + os.environ['PATH']
os.environ['GDAL-DATA'] = os.path.join(mainPath, 'GDAL', 'bin', 'gdal-data')
##print os.environ['PATH']

gdal_translate = r'...' # file path to gdal_translate.exe

# gdal translate command and projection
cmd = '-of GTiff -a_srs'

# Define Projection
proj = '"+proj=utm +zone=32 +ellps=intl +units=m +no_defs"'
#proj =  sys.argv[3]

# Input file
input = r'...' # file input -- ZMap grid *.dat
#input = sys.argv[1]

# Output file path
output = r'...' # output file path --- *.tif
#output = sys.argv[2]

def main():
    translateFile = ' '.join([gdal_translate, cmd, proj, input, output])
    subprocess.call(translateFile)
    print translateFile


if __name__ == '__main__':
    main()
