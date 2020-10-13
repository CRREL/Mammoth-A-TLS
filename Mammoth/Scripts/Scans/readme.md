Scripts involved in obtaining lidar scans or processing lidar scan files

compress:
  - Converts riegl scan files from .rxp to .laz using PDAL, preserves original files.
  - Compresses the original .rxp file into a .gz file.

frame:
  - Turns the scanner power on, waits 4 minutes.
  - Conducts a basic frame scan using the LidarCollect library.
  - Analyzes two spheres within the frame scan using PDAL to determine snowfall.
  - If it is snowing, it will call the line script
  - Turns the scanner power off.

line:
  - Conducts a basic line scan using the LidarCollect library.
  - Conducts a basic calibration line scan of the Spectralon panel on-site.

line_extended:
  - Checks to see if the last frame scan recorded snowfall.
  - If last frame scan recorded snowfall, turn on the scanner if it is off.
  - Conducts an extended line scan using the LidarCollect library.
  - Only conducts a spectralon scan if it is less than 10 minutes into the hour.
  - Turns the scanner power off when it is done.
