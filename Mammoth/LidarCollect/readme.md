Decompressing and compiling the LidarCollect-master.zip library from a terminal.

1. mkdir /home/mammoth/Mammoth/LidarCollect
2. cd /home/mammoth/Mammoth/
3. cp <source location> /lidarcollect.zip
4. unzip lidarcollect.zip
5. cd LidarCollect-master/
6. cp <source location> /CMakeLists.txt
7. mkdir build
8. cd build
9. cmake .. -DCMAKE_PREFIX_PATH=/home/mammoth/Mammoth/RiVLIB/rivlib-2_5_7-x86_64-linux-gcc55/
10. make

**Note: To run on the Stealth LPC-835, the CMakeLists.txt file is updated to
run on a 64-bit system. The 64-bit CMakeLists.txt is included in this directory
and must be copy/pasted, overwrite, the native CMakeLists.txt file provided when
unpacking the lidarcollect.zip
