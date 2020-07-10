#!/bin/bash

# Switch to the directory to save the converted to .laz files into
cd ~/Mammoth/scans

# Activate the PDAL environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate pdal

# Clone/convert all .rxp files into .laz using PDAL and its input config json file
find ~/Mammoth/scans/ -name "*.rxp" | parallel pdal pipeline ~/Mammoth/scripts/PDAL/base-laz.json --readers.rxp.filename={} --writers.las.filename={.}.laz

# Compress all original .rxp files
find  ~/Mammoth/scans/ -name "*.rxp" | parallel gzip {}
