Decompressing and compiling the lidarcollect.zip library from a terminal.

Unzip copy of Lidar Collect library and get it set up for installation
1. cd /home/mammoth/Mammoth/
2. cp <source_location> /lidarcollect.zip
3. unzip lidarcollect.zip
4. mv LidarCollect-master lidarcollect
5. rm lidarcollect.zip
6. cd lidarcollect
7. cd 'Lidar Collect'
8. mv * ../
9. cd ..
10. rmdir 'Lidar Collect'

To overwrite the default CMakeLists file to accomodate x64 (if needed):
1. cp <source location> /CMakeLists.txt

Or edit the default CMakeLists.txt file for x64 (if needed):
1. nano CMakeLists.txt
2. scroll to line 54
3. change to: set_target_properties(LidarCollect PROPERTIES COMPILE_FLAGS "-m64" LINK_FLAGS "-m64")
4. save & exit, returning to /home/mammoth/mamoth/lidarcollect

Build the Lidar Collect library:
1. mkdir build
2. cd build
3. cmake .. -DCMAKE_PREFIX_PATH=/home/mammoth/mammoth/rivlib/
4. make

Requires libLAS & rivlib.
