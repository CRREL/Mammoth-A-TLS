#!/usr/bin/env python3
#---------------------------------- Header -------------------------------------
#-------------------------------------------------------------------------------
import openpylivox as opl
import argparse
from datetime import datetime
import os

#--------------------------------- Variables -----------------------------------
# Specify UDP Packet Ports
dataPort = 60001
cmdPort = 50001
imuPort = 40001
#-------------------------------------------------------------------------------

def spinDownSensor( computerIP, sensorIP ):
    sensor = opl.openpylivox( True )
    connected = sensor.connect( computerIP, sensorIP, dataPort, cmdPort, imuPort )
    if connected:
        sensor.dataStop()
        sensor.lidarSpinDown()
        sensor.disconnect()

    else:
        print( "Could not connect to Livox sensor at: " + sensorIP )
        print( "Make sure computer interfaces are correctly configured, and the Livox sensors are powered." )

def livoxCollect( computerIP, sensorName, sensorIP, startDelay, duration, filePath ):
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    #-sip, Source IP -dip, Destination IP -t, Duration in time [s] -d, Start delay duration in [s],
    parser.add_argument( "-sip", "--SourceIP", dest = "source_ip", default = "192.168.2.2", help = "Source IP, i.e. IP of the Stealth that the Livox is attached to." )
    parser.add_argument( "-dip", "--DestinationIP", dest = "dest_ip" ,default = "192.168.2.4", help = "Destination IP, i.e. IP address of the Livox." )
    parser.add_argument( "-t", "--time", dest = "dur", default = "10", help = "Livox lidar scan duration in seconds." )
    parser.add_argument( "-d", "--delay", dest = "start_delay", default = "0.1", help = "Livox lidar scan start delay in seconds." )
    parser.add_argument( "-c", "--command", dest = "command", default = "spindown", help = "Enter program command, spindown or collect." )
    parser.add_argument( "-n", "--name", dest = "name", default = "Livox_unassigned", help = "Enter a suffix for the file name, e.g. Livox_1, Livox_2, etc..." )
    parser.add_argument( "-p", "--path", dest = "path", default = "", help = "Provide the directory you wish you save the .las file to" )

    args = parser.parse_args()

    if args.command.lower() == "collect":
        livoxCollect( args.source_ip, args.name, args.dest_ip, float(args.start_delay), float(args.dur), args.path )

    elif args.command.lower() == "spindown":
        spinDownSensor( args.source_ip, args.dest_ip )

    else:
    	print("Unknown command, exiting program.")
