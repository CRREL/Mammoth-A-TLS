Point Data Abstraction Library (PDAL) Scripts

201909-Mammoth-VZ400-POP.dat:
  - data file containing the POP conversion matrix.

201909-Mammoth-VZ400-SOP.dat:
  - data file containing the SOP conversion matrix.

base-laz.json:
  - Input file for PDAL to help in converting the scanner .rxp to .laz.
  - Contains the SOP and POP georeferencing conversion matrices.

snow-sphere.json:
  - Configuration file used by PDAL to help determine a snowfall event.
  - Contains coordinates for a sphere within the basic frame scan.

snow-sphere-2.json:
  - Configuration file used by PDAL to help determine a snowfall event.
  - Contains coordinates for a second sphere within the basic frame scan.

  Visualization of snow-sphere locations:
  ![](https://github.com/CRREL/Mammoth-A-TLS/blob/master/Images/snow-spheres-1.png)
  ![](https://github.com/CRREL/Mammoth-A-TLS/blob/master/Images/snow-spheres-2.png)
  ![](https://github.com/CRREL/Mammoth-A-TLS/blob/master/Images/snow-spheres-3.png)
