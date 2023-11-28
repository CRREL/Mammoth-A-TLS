# Mammoth-A-TLS
  
  A Riegl VZ400 (or VZ1000) lidar scanner conducts a framed terrestrial laser scan (TLS) once an hour at the remote mountain location in Mammoth, California.  Two spheres located within the frame scan are processed using the Point Data Abstraction Library (PDAL) to determine the number of particles within each sphere.  If both spheres contain a number of particles over the specified threshold, it is a snowfall event and a single line TLS is conducted.  During a snowfall event, extended single line TLS are conducted every fifteen minutes.  Once a day the scan data files are converted from .rxp to .laz and transferred to an AWS S3 bucket to prevent filling up the scanner's internal memory.

## Hardware Dependencies

- To be filled out.

## Software Dependencies

- To be filled out.

## General Order of Operations

- To be filled out.
