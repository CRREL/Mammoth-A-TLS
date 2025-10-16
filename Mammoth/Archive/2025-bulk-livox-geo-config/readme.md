# Georegistering Livox Files

## OpenPyLivox (OPL) & las.gz

- The original OpenPyLivox library is old and not maintained.
- Provided initial means to read binary data to file for livox mid-70.
- Created problems down the road wrt data storage and processing.

### OpenPyLivox (old)

- Open source tool to read livox data to binary file.
- Built in converter for binary to las or csv files.
- Does not capture intesity_confidence and spatial_confidence as reported by the livox mid-70.
- Improper header writing that is not compatible with PDAL processing.
- Required old laspy version, e.g. no ability to write las v1.4 files, unclear how to use VLRs with changes between las v1.2 and v1.4
- I had a difficult time with obtaining documentation related to the very outdated laspy version needed for this library.
- Does not assign a CRS.

### OpenPyLivox (my fork)

- Modified OpenPyLivox library.
- Updates library to record intensity_confidence and spatial_confidence to file.
- Allows for current laspy use, required for writing .laz files instead of las files.
- Better documentation on what to do and where by using current laspy version.
- Fixes las header issues and gets the file directly output to .laz vs. .las.
- Files compatible for processing with PDAL.
- Have options to assign CRS using Pyproj, but by default does not assign a CRS.
- Look for the bulk of changes in the _convertBin2Las function.

### Summary OPL

- Old OPL las.gz, no write out to .laz and incompatible with PDAL due to improper header. No CRS, not able to add one.
- New .laz, allows las v1.4, works with current laspy for compresses las files, compatible with PDAL. No CRS by default, but can add one.

## Old las.gz to New .laz

### LASTools

- Las2las offers a means to correcting las.gz header information for compatibility with PDAL.
    1. Uncompress las.gz -> las.
    2. Modifies header to las v1.4, point format 3, though 1 is likely to be more appropriate since no RGB values.
    3. Uses a 'dummy' EPSG code to insert CRS information into header. We used 4978 for Vicksburg project and 7789 doesn't work here.
    4. Sensor records in mm so we are just setting units of the file in the header, just in case, of meters in xy and also in z.
    5. Sets vertical to WGS84 in header <- used for Vicksburg project and copy/pasted, perhaps not necessary here.
    6. Sets OGC_WKT flag in header <- I believe this is for the CRS in the header.
    7. Writes out to a compressed las file (.laz) saving a lot of disk space when processing.
- These steps, right or wrong, gave us a version of a laz file we were then able to bulk process.
- A lot of combinations of options were tried, and a lot of them ended up failing in Las2las or were incompatible with PDAL.

### LASPY

- Current laspy can be installed with laszip and/or lazrs to write directly to compressed las.
- Old version of laspy used with old OPL did not allow for use of/with laszip/lazrs so it could only convert to las.
- Documentation.
- Used by OPL (my fork) to write proper las headers and construct las file.
- Only used when converting from binary file to las file.

## SOPs

- Why do they differ?

### Bulk Processing SOPs

- Files fixed from las.gz to PDAL compatible .laz with LASTools use EPSG 4978 to start.
    1. Couldn't leave the EPSG blank and have las2las work.
    2. Couldn't assign to EPSG 7789 like the vz400, las2las would reject it as invalid.
    3. Conversions using the same SOP/POP have different outcomes when using different starting EPSGs. Likely due to the reprojection stage of PDAL pipeline.
- SOP matrix to georegister was generated using RiScan Pro, referencing these 'fixed' EPSG 4978 files to the georegistered EPSG 7789 -> 26911 files of the vz400.
    1. This resulted in an offset in the georegistered data because the starting EPSGs do not match.
    2. By adjusting the SOP, we were able to correct the transformation to correctly georegister the point clouds.
    3. The correction only applies to files that have an EPSG assigned by las2las.
- Conversions of a LAStools fixed laz file.
    1. default srs = 4978
    2. SOP generated from 7789 -> 26911 of VZ400 with modifications applied to incorporate reprojection issues due to 4978.
    3. POP matrix generated from RiScan Pro.
    4. Reprojection from 4978 -> 26911.
    5. Forward all non modified header values.
    6. Include all non standard las dimensions.
    7. Validate offset and scale.
    8. Saves to *.REG.laz
- Conversions of a new .laz with no default CRS (ERROR).
    1. default srs = 7789
    2. SOP generated from 7789 -> 26911 of VZ400.
    3. POP generated from RiScan Pro.
    4. Reprojection from 7789 -> 26911.
    5. Forward all non modified header values.
    6. Include all non standard las dimensions.
    7. Validate offset and scale.
    8. Saves to *.REG.laz
    9. Incorrect georegistration, does not align properly with vz400 georegistered files.
    10. Have to use the SOP generated from 7789 -> 26911 with modifications, and EPSG of 4978, just like if we were processing the LAStools fixed laz file.
    11. Different PDAL versions are handling the reprojection differently?

### Mammoth A-TLS SOPs

- Files generated as .laz are now compatible with PDAL and do not assign a default CRS.
- The PDAL version used on board is a much older release because readers_rdb and readers_rxp are not compatible with newer releases.
- We can assign a default srs of 7789 properly without unintended consequences.
- Conversions of a livox file on the Mammoth A-TLS PC.
    1. default srs = 7789
    2. SOP generated from 7789 -> 26911 of VZ400.
    3. POP matrix generated from RiSCAN Pro.
    4. Reprojection from 7789 -> 26911.
    5. Forward all non modified header values.
    6. Include all non standard las dimensions.
    7. Validate offset and scale.
    8. Saves to *.REG.laz
    9. Correct georegistration, aligns properly to vz400 georegistered files.
