This is the install directory for the pdal libraries & packages, when you create
the pdal environment using:
  - conda create --name pdal

-readers_rxp and readers_rdb are needed for PDAL to read in .rxp files and convert
them into .laz files.

-jq package is needed for PDAL

-fgt cpd packages are needed for PDAL

- tiledb package currently not loading, but is not needed, so if you find error
reporting it can be ignored safely for the Mammoth A-TLS purposes.
