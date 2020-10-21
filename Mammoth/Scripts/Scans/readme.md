Scripts involved in obtaining lidar scans or processing lidar scan files

compress:
 - Converts riegl scan files from .rxp to .laz using PDAL, preserves original files.
 - Compresses the original .rxp file into a .gz file.

frame:
 - Conducts a basic frame scan using the LidarCollect library.
 - Analyzes two spheres within the frame scan using PDAL to determine snowfall.
 - If it is snowing, it will call the line script

line:
 - Conducts a basic line scan using the LidarCollect library.
 - Conducts a basic calibration line scan of the Spectralon panel on-site.

line_extended:
 - Checks to see if the last frame scan recorded snowfall.
 - Conducts an extended line scan using the LidarCollect library, if snowing.
 - Only conducts a spectralon scan if it is less than 10 minutes into the hour.
