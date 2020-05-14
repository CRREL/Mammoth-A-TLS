#!/bin/bash
cd ~/Mammoth/scans
source ~/miniconda3/etc/profile.d/conda.sh
conda activate pdal
find /home/mammoth/Mammoth/scans/ -name "*.rxp" | parallel pdal pipeline ~/Mammoth/scripts/base-laz.json --readers.rxp.filename={} --writers.las.filename={.}.laz

find  /home/mammoth/Mammoth/scans/ -name "*.rxp" | parallel gzip {}
