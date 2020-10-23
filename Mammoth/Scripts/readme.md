User made tools :  
AWS:
  - syncaws: Copy scans from ~/Mammoth/Scans to AWS S3 Bucket

GPIO:
  - scanner_poweron: Switches the GPIO pin to on.
  - scanner_poweroff: Switches the GPIO pin to off.
  - scanner_shutdown: Software shutdown for the scanner
  - scanner_status: Poll the GPIO pin.

Logs:
  - logs_split: Splits logs by month to reduce file sizes

PDAL:
  - base-laz.json: Input file for PDAL to facilitate conversion from .rxp to .laz.
  - snow-sphere.json: Coordinates for a sphere to look for snow.
  - snow-sphere-2.json: Second set of coordinates for a sphere to look for snow.

Scans:
  - compress: copy/converts .rxp to .laz then compresses .rxp to .gz files.
  - frame: conducts a basic framed TLS of the terrain, then uses PDAL to look for snow.
  - line: conducts a basic single line TLS of a section of the terrain.
  - line_extended: conducts an extended single line TLS of a section of the terrain.

Vars:
  - snowing: Stores a value that correlates to snowing, or not snowing.
  - scanner_power: Stores a value that correlates to scanner power off or on.


***** See the readme.md in each directory for more information on scripts *****
