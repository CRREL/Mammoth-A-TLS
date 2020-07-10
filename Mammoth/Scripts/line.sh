# Directory where we want to store the scan data files
cd ~/Mammoth/scans

# Conduct a basic line scan
~/LidarCollect --ip 192.168.0.128 --line 1 30 130 0.04 195 30

# wait for the line scan to be finished.
sleep 30s

# Conduct a calibration/reference scan on the Spectralon panel.
~/LidarCollect --ip 192.168.0.128 --line 1 115 125 0.02	276 30 spectralon
