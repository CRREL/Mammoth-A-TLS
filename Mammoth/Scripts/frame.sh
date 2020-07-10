#!/bin/bash

# Change to the directory where file scans are to be stored to
cd ~/Mammoth/scans

# Conduct a basic frame scan
~/LidarCollect --ip 192.168.0.128 --frame 1 50 130 0.04 110 280 0.04

# Initialize the PDAL environment for scan processing
source ~/miniconda3/etc/profile.d/conda.sh
conda activate pdal

# Use PDAL to determine the number of points within two different spheres
filename=$(ls -t *frame.rxp | head -1)
snowcount=$(pdal pipeline ../scripts/PDAL/snow-sphere.json --metadata=stdout --readers.rxp.filename=$filename | jq '.stages["filters.stats"].statistic [].count')
snowcount2=$(pdal pipeline ../scripts/PDAL/snow-sphere-2.json --metadata=stdout --readers.rxp.filename=$filename | jq '.stages["filters.stats"].statistic [].count')

# Determine if there are enough points to declare a snowfall event.
if [ $snowcount -gt 15 ] && [ $snowcount2 -gt 15 ]; then
  echo "Snowing, starting line scan"
  ../scripts/line.sh
else
  echo "No Snow"
fi
