# User made tools

## aws/

- syncaws: Copy scans from ~/Mammoth/Scans to AWS S3 Bucket

## gpio/

- gpo_script: serial interface for the arduino relay shield.
- livox_poweroff: Switches gpo relay for livoxes to off.
- livox_poweron: Switches gpo relay for livoxes to on.
- livox_status: Checks the status of the gpo pin corresponding to livox power.
- scanner_poweron: Switches the gpo relay for riegl items to on.
- scanner_poweroff: Switches the gpo relay for riegl items to off.
- scanner_shutdown: Software shutdown for the scanner
- scanner_status: Checks the status of the gpo pin corresponding to riegl items power.

## livox/

- livox_capture: triggers the livoxes to acquire pointcloud scans, will poweron if not already on.
- livox_utils.py: coordinates with the openpylivox library for CLI style interactions, used by livox_capture.

### openpylivox/

- Livox SDK adapted to python, see folder specifics for acknowledgements and licensing.

## logs/

- logs_split: Splits logs by month to reduce file sizes

## pdal/

- base-laz.json: Input file for PDAL to facilitate conversion from .rxp to georegistered .laz.
- livox1-base.json: Input file for PDAL to faciliate georegistration.
- livox2-base.json: Input file for PDAL to faciliate georegistration.
- livox3-base.json: Input file for PDAL to faciliate georegistration.
- snow-sphere.json: Coordinates for a sphere to look for snow.
- snow-sphere-2.json: Second set of coordinates for a sphere to look for snow.

## scans/

- compress: copy/converts .rxp to .laz then compresses .rxp to .gz files.
- frame: conducts a basic framed TLS of the terrain, then uses PDAL to look for snow.
- line: conducts a basic single line TLS of a section of the terrain.
- line_extended: conducts an extended single line TLS of a section of the terrain.

## vars/

- snowing: Stores a value that correlates to snowing, or not snowing.
- scanner_power: Stores a value that correlates to scanner power off or on.

*** See the readme.md in each directory for more information on scripts
