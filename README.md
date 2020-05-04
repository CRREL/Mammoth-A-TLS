# Mammoth-A-TLS
  A Reigl VZ400 (or VZ1000) lidar scanner conducts a frame scan once an hour.  Two spheres located within the frame scan are processed through the Point Data Abstraction Library (PDAL) to determine the number of particles within each sphere.  If both spheres contain a number of particles over the specified threshold, it is a snowfall event and a line scan is conducted.  Once a day the scan data files are converted to .gz, .laz (from .rxp) and transferred to an AWS S3 bucket to prevent filling up the scanner's internal memory.

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
