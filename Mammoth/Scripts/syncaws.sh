export HOME=/home/mammoth
/usr/local/bin/./aws s3 mv /home/mammoth/Mammoth/scans s3://crrel-mammoth-lidarscans/original_scans --recursive --exclude "*" --include "*.gz"
/usr/local/bin/./aws s3 mv /home/mammoth/Mammoth/scans s3://crrel-mammoth-lidarscans/laz --recursive --exclude "*" --include "*.laz"
