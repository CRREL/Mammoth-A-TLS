#
# CMake file used to generate build files for the LidarCollect
# program. You'll need to run CMake with the -DCMAKE_PREFIX_PATH
# flag pointing to the location of the downloaded RiVLib, e.g.:
#
#   -DCMAKE_PREFIX_PATH=/home/mammoth/Mammoth/RiVLIB/rivlib-2_5_7-x86_64-linux-gcc55/
#

# Set the project name
project(LidarCollect)

# CMake minimum version
cmake_minimum_required(VERSION 2.8)

# Make sure we're using C++11
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")

# Find RiVLib packages
find_package(RiVLib COMPONENTS scanlib ctrllib REQUIRED)

# Find liblas
find_package(libLAS)
if(LIBLAS_FOUND)
    find_program(LIBLAS_CONFIG_PROG liblas-config /usr/local/bin)
    if(LIBLAS_CONFIG_PROG)
        exec_program(${LIBLAS_CONFIG_PROG} ARGS --libs OUTPUT_VARIABLE LIBLAS_LIBRARIES)
        exec_program(${LIBLAS_CONFIG_PROG} ARGS --includes OUTPUT_VARIABLE LIBLAS_INCLUDE_DIRS)
        exec_program(${LIBLAS_CONFIG_PROG} ARGS --cxxflags OUTPUT_VARIABLE LIBLAS_CXXFLAGS)
        message(STATUS "Including support for LAS file I/O")
        add_definitions(-DHAS_LAS)
    endif(LIBLAS_CONFIG_PROG)
else()
    message(STATUS "libLAS not found, LAS file I/O will not be supported")
endif(LIBLAS_FOUND)

# Include this line for static compilation
# set(RiVLib_USE_STATIC_RUNTIME   ON)

# Include the RiVLib include directories
include_directories(${RiVLib_INCLUDE_DIRS})

# Add the VZFrame executable
add_executable(LidarCollect src/LidarCollect.cpp
                            src/io/InputParser.cpp
                            src/scanners/VZ1000.cpp
                            include/globals.h
                            include/io/InputParser.h
                            include/scanners/VZ1000.h)

# 32-bit
#set_target_properties(LidarCollect PROPERTIES COMPILE_FLAGS "-m32" LINK_FLAGS "-m32")

# 64-bit
set_target_properties(LidarCollect PROPERTIES COMPILE_FLAGS "-m64" LINK_FLAGS "-m64")

# Set link libraries
target_link_libraries(LidarCollect ${RiVLib_CTRLLIB_LIBRARY} ${RiVLib_SCANLIB_LIBRARY})
