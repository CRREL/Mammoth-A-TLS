Decompressing and compiling the LidarCollect-master.zip library from a terminal.

1. mkdir /home/mammoth/Mammoth/LidarCollect
2. cd /home/mammoth/Mammoth/
3. cp <source location> /lidarcollect.zip
4. unzip lidarcollect.zip
5. cd LidarCollect-master/
6. cmake -DCMAKE_PREFIX_PATH=/home/mammoth/Mammoth/RiVLIB/rivlib-2_5_7-x86-linux-gcc44/
