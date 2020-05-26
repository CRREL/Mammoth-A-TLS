mammoth user account Files/Folder
- These binary executable files are accessed via the mammoth user account.
- These files should be copied to the mammoth account /Mammoth/scripts/ directory.
- For now, all files executed by the root user account are seperated from the
    files executed by the mammoth user account.

User made tools (mammoth user) : ~/Mammoth/Scripts/  
1. frame.sh:  issues a frame scan via LidarCollect, calls PDAL to see if there is snow  
2. line.sh:  issues a line scan via LidarCollect  
3. compress.sh:  convert to .laz and gzip .rxp files  
4. syncaws.sh:  copy scans from Scans/ to AWS S3 Bucket  
5. snow-sphere.sh:  coordinates/dimensions for sphere in which to look for snow points  
6. snow-sphere-2.sh:  coordinates/dimensions for 2nd sphere in which to look for snow points  
7. base-laz.json:  PDAL pipeline used by compress.sh to convert .rxp to .laz  