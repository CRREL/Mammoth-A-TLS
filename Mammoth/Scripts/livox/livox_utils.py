#!/usr/bin/env python3
#******************************** Dependencies *********************************
import openpylivox as opl
import argparse
from datetime import datetime
import os, subprocess
#*******************************************************************************
#==================================== Intro ====================================
# Aaron Kehl
# USACE - ERDC - CRREL
# Spring 2023
# Example provided by openpylivox, referenced/modified by me.
#===============================================================================

#=================================== Globals ===================================
#---------------------------------- Variables ----------------------------------
# Specify UDP Packet Ports
dataPort = 60001
cmdPort = 50001
imuPort = 40001
#-------------------------------------------------------------------------------
#===============================================================================

#================================= Functions ===================================
#------------------------------- spinDownSensor --------------------------------
def spinDownSensor( computerIP, sensorIP ):
    """ When powered on the livox automatically starts spinning up and scanning.
        This function is used to spin down the livox sensor after start up, but
        prior to starting a scan and after scanning is done.
        Host/client must be on same subnet.

        Inputs:
            computerIP = String of the ip address of your computer, the livox is connected to, e.g. 192.168.4.2
            sensorIP = String of the ip address of the livox sensor, e.g. 192.168.4.3
        
        Ouputs:
            None
    """
    sensor = opl.openpylivox( True )
    connected = sensor.connect( computerIP, sensorIP, dataPort, cmdPort, imuPort )
    if connected:
        sensor.dataStop()
        sensor.lidarSpinDown()
        sensor.disconnect()

    else:
        print( "Could not connect to Livox sensor at: " + sensorIP )
        print( "Make sure computer interfaces are correctly configured, and the Livox sensors are powered." )
#-------------------------------------------------------------------------------

#------------------------------- livoxCollect ----------------------------------
def livoxCollect( computerIP, sensorName, sensorIP, startDelay, duration, filePath ):
    """ This function interfaces with the openpylivox library to collect a lidar
        pointcloud, using the information provided, then saves it to file.

        Inputs:
            computerIP = String of the ip address of your computer, the livox is connected to, e.g. 192.168.4.2
            sensorName = String of the device name you would like to be included in the file name, e.g. PIVOX1
            sensorIP = String of the ip address of the livox sensor, e.g. 192.168.4.3
            startDelay = How long should the scan be delayed, after spinup, before data is recorded in seconds, e.g. 0.1
            duration = How long should the scan take place for in seconds, e.g. 45
            filepath = Where the pointcloud should be saved to, e.g. ~/pivox/scans

        Outputs:
            None. Does save a pointcloud file to your hard drive though.
    """
    sensor = opl.openpylivox( True )
    connected = sensor.connect( computerIP, sensorIP, dataPort, cmdPort, imuPort)

    sensor.lidarSpinUp()
    sensor.dataStart_RT_B()

    now = datetime.now()
    fileName = now.strftime( "%Y%m%d-%H%M-%S" ) + "." + sensorName
    filePath = filePath + "/"
    filePathAndName = filePath + fileName
    if not os.path.exists( filePath ):
        os.mkdir( filePath )

    sensor.saveDataToFile( filePathAndName, startDelay, duration )

    # simulate other operations being performed
    while True:
        # exit loop when capturing is complete (*** IMPORTANT: ignores (does not check) sensors with duration set to 0)
        if sensor.doneCapturing():
            break

    sensor.dataStop()
    sensor.lidarSpinDown()
    sensor.disconnect()

    # convert BINARY point data to LAS file and IMU data (if applicable) to CSV file
    # only works in conjunction with .dataStart_RT_B()
    # designed so the efficiently collected binary point data can be converted to LAS at any time after data collection
    opl.convertBin2LAS( filePathAndName, deleteBin=True )
    #opl.convertBin2CSV( filePathAndName, deleteBin=True )
#-------------------------------------------------------------------------------

#------------------------------ rapid_LivoxCollect -----------------------------
def rapid_livoxCollect( computerIP, sensorName, sensorIP, startDelay, scan_duration, filePath, total_duration ):
    """ This function interfaces with the openpylivox library to collect a lidar
        pointcloud, using the information provided, then saves it to file.

        Inputs:
            computerIP = String of the ip address of your computer, the livox is connected to, e.g. 192.168.4.2
            sensorName = String of the device name you would like to be included in the file name, e.g. PIVOX1
            sensorIP = String of the ip address of the livox sensor, e.g. 192.168.4.3
            startDelay = How long should the scan be delayed, after spinup, before data is recorded in seconds, e.g. 0.1
            scan_duration = How long should the scan take place for in seconds, e.g. 45
            filepath = Where the pointcloud should be saved to, e.g. ~/pivox/scans
            overall_duration = How long repeated scans should take place for, e.g. 10s scans for 2 hours. input in [min]

        Outputs:
            None. Does save a pointcloud file to your hard drive though in binary format. to be converted later
    """

    sensor = opl.openpylivox( True )
    connected = sensor.connect( computerIP, sensorIP, dataPort, cmdPort, imuPort)

    sensor.lidarSpinUp()

    number_of_collects = int( ( total_duration * 60 ) / scan_duration )
    print( number_of_collects )
    filePath = filePath + "/"

    for i in range( 1, number_of_collects + 1 ):
        sensor.dataStart_RT_B()
        print( "Rapid collect " + str( i ) + " of " + str( number_of_collects ) )
        subprocess.call( filePath + "../scripts/pivox/camera_capture", shell=True )
        now = datetime.now()
        fileName = now.strftime( "%Y%m%d-%H%M-%S" ) + "." + sensorName
        filePathAndName = filePath + fileName
        if not os.path.exists( filePath ):
            os.mkdir( filePath )

        sensor.saveDataToFile( filePathAndName, startDelay, scan_duration )

        # simulate other operations being performed
        while True:
            # exit loop when capturing is complete (*** IMPORTANT: ignores (does not check) sensors with duration set to 0)
            if sensor.doneCapturing():
                break

        if ( number_of_collects / i * 100 ) % 20 == 0:
            subprocess.call( filePath + "../scripts/telemetry/telemetry_capture", shell=True )

        sensor.dataStop()
        
    sensor.lidarSpinDown()
    sensor.disconnect()
    
    convertDirectory( sensorName, filePath )
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#------------------------------- convertDirectory ------------------------------
def convertDirectory( name, directory ):
    """ Converts the directory contents ending with <name> to .laz or .csv
    """
    directory_file_names = os.listdir( directory )

    for file_name in directory_file_names:
        if name in file_name and not ".laz" in file_name and not ".csv" in file_name:
            filePathAndName = directory + "/" + file_name
            opl.convertBin2LAS( filePathAndName, deleteBin=True )
            #opl.convertBin2CSV( filePathAndName, deleteBin=True )
#-------------------------------------------------------------------------------
#===============================================================================

#================================ Main Function ================================
#------------------------- main -sip arg1 -dip arg2 ... ------------------------
if __name__ == '__main__':
    """ Main function for the livox utility script that interfaces with the 
        openpylivox library.  Several parameters can be passed in with the call
        so that a terminal user can address individual lidar units as needed.
        This function will orchestrate the collection of a pointcloud from the
        livox, given the passed in parameters or defaults.

        Inputs (flags):
            -sip = source ip address
            -dip = destination ip address
            -t = length of scan duration in seconds
            -d = start up delay
            -c = command
            -n = device name, e.g. PIVOX1
            -p = path to save to, directory

        Outputs:
            None. Does save a pointcloud to the given path though.

        Syntax for Callin the main function:
            livox_utils -sip 192.168.4.2 -dip 192.168.4.3 -t 45 -d 0.1 -c collect -n PIVOX1 -p ~/pivox/scans
    """
    parser = argparse.ArgumentParser()

    #-sip, Source IP -dip, Destination IP -t, Duration in time [s] -d, Start delay duration in [s],
    parser.add_argument( "-sip", "--SourceIP", dest = "source_ip", default = "192.168.2.2", help = "Source IP, i.e. IP of the Stealth that the Livox is attached to." )
    parser.add_argument( "-dip", "--DestinationIP", dest = "dest_ip" ,default = "192.168.2.4", help = "Destination IP, i.e. IP address of the Livox." )
    parser.add_argument( "-t", "--time", dest = "dur", default = "10", help = "Livox lidar scan duration in seconds." )
    parser.add_argument( "-d", "--delay", dest = "start_delay", default = "0.1", help = "Livox lidar scan start delay in seconds." )
    parser.add_argument( "-c", "--command", dest = "command", default = "spindown", help = "Enter program command; spindown, collect, or convert." )
    parser.add_argument( "-n", "--name", dest = "name", default = "Livox_unassigned", help = "Enter a suffix for the file name, e.g. Livox_1, Livox_2, etc..." )
    parser.add_argument( "-p", "--path", dest = "path", default = "", help = "Provide the directory you wish you save the .las file to" )
    parser.add_argument( "-tt", "--total_time", dest = "total_dur", default = 0, help = "When conducting a rapid/repeated scan, how long to take scans at the scan duration, enter in [min]" )

    args = parser.parse_args()

    if args.command.lower() == "collect":
        livoxCollect( args.source_ip, args.name, args.dest_ip, float(args.start_delay), float(args.dur), args.path )
    elif args.command.lower() == "rapidcollect":
        rapid_livoxCollect( args.source_ip, args.name, args.dest_ip, float(args.start_delay), float(args.dur), args.path, int( args.total_dur ) ) 
    elif args.command.lower() == "spindown":
        spinDownSensor( args.source_ip, args.dest_ip )
    elif args.command.lower() == "convert":
        convertDirectory( args.name, args.path )
    else:
        print("Unknown command, exiting program.")
#-------------------------------------------------------------------------------
#===============================================================================