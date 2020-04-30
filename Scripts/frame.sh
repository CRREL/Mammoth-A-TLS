#!/bin/bash
cd ~/Mammoth/scans
~/LidarCollect --ip 192.168.0.128 --frame 1 50 130 0.04 110 280 0.04
source ~/miniconda3/etc/profile.d/conda.sh
conda activate pdal

filename=$(ls -t *frame.rxp | head -1)
snowcount=$(pdal pipeline ../scripts/snow-sphere.sh --metadata=stdout --readers.rxp.filename=$filename | jq '.stages["filters.stats"].statistic [].count')
snowcount2=$(pdal pipeline ../scripts/snow-sphere-2.sh --metadata=stdout --readers.rxp.filename=$filename | jq '.stages["filters.stats"].statistic [].count')
if [ $snowcount -gt 15 ] && [ $snowcount2 -gt 15 ]
then
  echo "Snowing, starting line scan"
  ../scripts/line.sh
else
  echo "No Snow"
fi
