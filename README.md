# Mammoth-A-TLS
 Control a VZ400 from a Linux machine with a GPIO.

 Dependencies:
 1. RivLib
    - Info: http://www.riegl.com/index.php?id=224
 2. LidarCollect
    - Included
 3. Python
    - Download: https://www.python.org/downloads/
 4. Conda
    - Download: https://www.anaconda.com/products/individual
 5. PDAL
    - Info: https://pdal.io/download.html#conda
    - Download: https://anaconda.org/conda-forge/pdal
 6. Fintek GPIO
    - Download: http://www.fintek.com.tw/index.php/mnu-swdevelopkitdl
 7. CMake
    - Info:https://cmake.org/cmake/help/v3.17/
    - Download: https://cmake.org/download/

 Default System Information:
 1. Linux IP: 172.17.0.251
 2. Reigl VZ400 IP: 192.168.0.128

General Overview:  
    The Reigl VZ400 (or VZ1000) lidar scanner conducts a frame scan once an hour as directed by the /root/crontab (power up/down the scanner) and the /scripts/crontab (controls scan details) files. Two spheres located within the frame scan are processed through the Point Data Abstraction Library (PDAL) to determine the number of particles within each sphere.  If both spheres contain a number of particles over a specified threshold, it is a snowfall event.  During a snowfall event the lidar scanner will conduct a line scan as described within the /scripts/crontab file.  Once a day the scan data files are transferred to an AWS S3 bucket to prevent filling up the scanner's internal memory.
