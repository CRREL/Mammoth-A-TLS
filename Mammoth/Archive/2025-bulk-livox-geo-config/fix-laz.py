#!/usr/bin/env python3
#******************************** Dependencies *********************************
import subprocess
import os
import argparse
from tqdm import tqdm
#*******************************************************************************

#=================================== Globals ===================================
#---------------------------------- Constants ----------------------------------
PREFIX = "[LAScript]: "
#-------------------------------------------------------------------------------
#===============================================================================

#================================= Functions ===================================
#-------------------------------------------------------------------------------
def convert_directory( path ):
    las2las = "las2las64"
    lasinfo = "lasinfo64"
    to_convert = []
    
    # parallel
    pipe = subprocess.Popen( ["find", path, "-name", "*.las" ], stdout = subprocess.PIPE )
    redirect = subprocess.check_output( [ "parallel", las2las, "-i", "{}",  "-set_version", "1.4", "-set_point_data_format", "3", "-o", "{.}.laz","-epsg","4978","-meter","-elevation_meter","-vertical_wgs84","-set_ogc_wkt" ], stdin=pipe.stdout )
    out = pipe.communicate()[0].decode("utf-8")[:-1].split("\n")
    for line in out: print( PREFIX + line )

    # sequential
    #filenames = os.listdir( path )
    #for filename in filenames:
    #    if ".las" in filename and not ".gz" in filename:
    #        to_convert.append( filename )

    #num_files = len( to_convert )       
    #prog = tqdm( total=num_files, unit="files", desc="   " )
    #for filename in to_convert:
    #    filepath = path + "/" + filename
        
        #convert
    #    pipe = subprocess.Popen( [ las2las, "-i", filepath,  "-set_version", "1.4", "-set_point_data_format", "3", "-o", path+"/"+filename[:-3]+"laz","-epsg","4978","-meter","-elevation_meter","-vertical_wgs84","-set_ogc_wkt" ], stdout=subprocess.PIPE )
    #    out = pipe.communicate()[0].decode("utf-8")[:-1].split("\n")
        #for line in out: print( PREFIX + line )

        #check
        #pipe = subprocess.Popen( [lasinfo, "-i", "./fixed2-las/"+filename ], stdout=subprocess.PIPE )
        #out = pipe.communicate()[0].decode( "utf-8" )[:-1].split( "\n" )
        #for line in out: print( PREFIX + line )

    #   prog.update( 1 )
    #prog.close()
#-------------------------------------------------------------------------------
#===============================================================================

#================================ Main Function ================================
#----------------------------- main --path arg1  ... ---------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( "-p", "--path", dest = "path", default = ".", help = "Provide the path to the directory or file to transform." )
    args = parser.parse_args()

    path = args.path
    # or
    path = "./mammoth/scans"

    convert_directory( path )
#-------------------------------------------------------------------------------
#===============================================================================