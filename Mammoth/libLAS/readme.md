# Installing libLAS from github

1. cd ~/mammoth (as user, as root navigate to /home/mammoth/mammoth)
2. git clone <https://github.com/libLAS/libLAS>
3. cd libLAS
4. mkdir build
5. cd build
6. cmake ..
7. make
8. sudo make install

** requires git and cmake on linux, as well as libboost-all-dev and libgeotiff-dev
