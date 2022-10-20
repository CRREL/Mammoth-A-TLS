Decompressing the rivlib library (provided by Riegl) from a terminal.

1. cd /home/mammoth/mammoth
2. cp source_location /rivlib-2_5_7-x86_64-linux-gcc55.zip
3. unzip rivlib-2_5_7-x86_64-linux-gcc55.zip
4. rm rivlib-2_5_7-x86_64-linux-gcc55.zip
5. mv rivlib-2_5_7-x86_64-linux-gcc55 rivlib

To install the rivlib library:
1. cd ~/mammoth/rivlib
2. mkdir build
3. cd build
4. cmake ../doc/rivlib/examples -DCMAKE_PREFIX_PATH=/home/mammoth/mammoth/rivlib/cmake
5. make
6. sudo make install
