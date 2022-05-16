Decompressing the RiVLIB library (provided by Riegl) from a terminal.

1. cd /home/mammoth/Mammoth
2. cp source_location /rivlib-2_5_7-x86_64-linux-gcc55.zip
3. unzip rivlib-2_5_7-x86_64-linux-gcc55.zip
4. rm rivlib-2_5_7-x86_64-linux-gcc55.zip
5. mv rivlib-2_5_7-x86_64-linux-gcc55 RiVLIB

**Note: LidarCollect uses components of RiVLIB to function, so this library only
needs to be copied onto the computer.  It does not need to be compiled.

If you do wish to install the library, or find you need to install it.
1. Navigate to unzipped /rivlib-2_5_7-x86_64-linux-gcc55 directory
2. export CMAKE_PREFIX_PATH=$(pwd)
3. cd doc/rivlib/examples
4. mkdir build
5. cd build
6. cmake ..
7. make
8. sudo make install
