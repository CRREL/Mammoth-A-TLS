# Mammoth-A-TLS
  A Riegl VZ400 (or VZ1000) lidar scanner conducts a frame scan once an hour at the remote mountain location in Mammoth, California.  Two spheres located within the frame scan are processed using the Point Data Abstraction Library (PDAL) to determine the number of particles within each sphere.  If both spheres contain a number of particles over the specified threshold, it is a snowfall event and a line scan is conducted.  Once a day the scan data files are converted from .rxp to .laz and transferred to an AWS S3 bucket to prevent filling up the scanner's internal memory.

 Hardware Dependencies:
 1. Linux box with general purpose input/output (GPIO)
 2. Riegl VZ400 or VZ1000
 3. System internet connectivity or adequate memory for data storage
 4. Power source(s)/supply

 Software Dependencies:
 1. RivLib (scanner communications)
    - Info: http://www.riegl.com/index.php?id=224
 2. LidarCollect (scanner commands)
    - Included
 3. Python
    - Download: https://www.python.org/downloads/
 4. Conda (environment for PDAL)
    - Download: https://www.anaconda.com/products/individual
 5. PDAL (convert to .laz and analyze point cloud data)
    - Info: https://pdal.io/download.html#conda
    - Download: https://anaconda.org/conda-forge/pdal
 6. Fintek GPIO (control GPIO of the linux box)
    - Download: http://www.fintek.com.tw/index.php/mnu-swdevelopkitdl
 7. CMake (to help install compiler libraries)
    - Info: https://cmake.org/cmake/help/v3.17/
    - Download: https://cmake.org/download/

 General Order of Operations:
 1. Turn on scanner
 2. Conduct a frame scan
 3. Determine if there is a snowfall event
 4. Conduct a line scan if it is snowing
 5. If end of day, convert all .rxp to .laz
 6. If end of day, upload all .rxp, .laz to AWS S3 bucket
 7. Turn off scanner
