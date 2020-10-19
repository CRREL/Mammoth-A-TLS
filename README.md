# Mammoth-A-TLS
  A Riegl VZ400 (or VZ1000) lidar scanner conducts a framed terrestrial laser scan (TLS) once an hour at the remote mountain location in Mammoth, California.  Two spheres located within the frame scan are processed using the Point Data Abstraction Library (PDAL) to determine the number of particles within each sphere.  If both spheres contain a number of particles over the specified threshold, it is a snowfall event and a single line TLS is conducted.  During a snowfall event, extended single line TLS are conducted every fifteen minutes.  Once a day the scan data files are converted from .rxp to .laz and transferred to an AWS S3 bucket to prevent filling up the scanner's internal memory.

 Hardware Dependencies:
 1. Linux box with general purpose input/output (GPIO)
 2. Riegl VZ-series scanner (VZ-400 has been tested)
 3. System internet connectivity or adequate memory for data storage
 4. Power source(s)/supply

 Software Dependencies:
 1. Make (to help install compiler libraries)
    - Info: https://www.gnu.org/software/make/manual/
    - Install: sudo apt-get install build-essential
 2. CMake (also to help install compiler libraries)
    - Info: https://cmake.org/cmake/help/v3.18/
    - Download: https://cmake.org/download/
    - Install: https://cmake.org/install/
 3. RivLib (scanner communications)
    - Info: http://www.riegl.com/index.php?id=224
 4. LidarCollect (scanner commands)
    - Included
 5. Conda, Python, PDAL
    - Info: https://pdal.io/download.html#conda
    - Download: https://www.anaconda.com/products/individual
 6. Fintek GPIO (control GPIO of the linux box)
    - Download: http://www.fintek.com.tw/index.php/mnu-swdevelopkitdl
 7. AWS CLI Tools
    - Repository: https://github.com/aws/aws-cli
    - pip: https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html

 General Order of Operations:
 1. Turn on scanner
 2. Conduct a frame scan
 3. Determine if there is a snowfall event
 4. Conduct a line scan if it is snowing
 5. Conduct extended line scans at *:05, *:20, *:35, *:50 if it is snowing
 5. If end of day, convert all .rxp to .laz
 6. If end of day, upload all .rxp, .laz to AWS S3 bucket
 7. Turn off scanner
