# Mammoth-A-TLS
  A Reigl VZ400 (or VZ1000) lidar scanner conducts a frame scan once an hour at the remote mountain location in Mammoth, California.  Two spheres located within the frame scan are processed using the Point Data Abstraction Library (PDAL) to determine the number of particles within each sphere.  If both spheres contain a number of particles over the specified threshold, it is a snowfall event and a line scan is conducted.  Once a day the scan data files are converted from .rxp to .laz and transferred to an AWS S3 bucket to prevent filling up the scanner's internal memory.

 Hardware Dependencies:
 1. Linux box with general purpose input/output (GPIO)
 2. Reigl VZ400 or VZ1000
 3. System internet connectivity or adequate memory for data storage
 4. Power source(s)/supply

 Software Dependencies:
 1. RivLib (Scanner Comms)
    - Info: http://www.riegl.com/index.php?id=224
 2. LidarCollect (Scanner Commands)
    - Included
 3. Python
    - Download: https://www.python.org/downloads/
 4. Conda (Environment for PDAL)
    - Download: https://www.anaconda.com/products/individual
 5. PDAL (Convert to .laz and analyze point cloud data)
    - Info: https://pdal.io/download.html#conda
    - Download: https://anaconda.org/conda-forge/pdal
 6. Fintek GPIO (Control GPIO of the linux box)
    - Download: http://www.fintek.com.tw/index.php/mnu-swdevelopkitdl
 7. CMake (To help install repository files)
    - Info:https://cmake.org/cmake/help/v3.17/
    - Download: https://cmake.org/download/

 Default System Information:
 1. Linux IP: 172.17.0.251
 2. Reigl VZ400 IP: 192.168.0.128

 General Order of Operations:
 1. Turn on scanner
 2. Conduct a frame scan
 3. Determine if there is a snowfall event
 4. Conduct a line scan if it is snowing
 5. If end of day, convert all .rxp to .laz
 6. If end of day, upload all .rxp, .laz to AWS S3 bucket
 7. Turn off scanner
