# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build

# Include any dependencies generated for this target.
include utils_dcf/CMakeFiles/aruco_dcf.dir/depend.make

# Include the progress variables for this target.
include utils_dcf/CMakeFiles/aruco_dcf.dir/progress.make

# Include the compile flags for this target's objects.
include utils_dcf/CMakeFiles/aruco_dcf.dir/flags.make

utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o: utils_dcf/CMakeFiles/aruco_dcf.dir/flags.make
utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o: ../utils_dcf/aruco_dcf.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o"
	cd /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o -c /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/utils_dcf/aruco_dcf.cpp

utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.i"
	cd /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/utils_dcf/aruco_dcf.cpp > CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.i

utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.s"
	cd /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/utils_dcf/aruco_dcf.cpp -o CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.s

utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.requires:

.PHONY : utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.requires

utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.provides: utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.requires
	$(MAKE) -f utils_dcf/CMakeFiles/aruco_dcf.dir/build.make utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.provides.build
.PHONY : utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.provides

utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.provides.build: utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o


# Object files for target aruco_dcf
aruco_dcf_OBJECTS = \
"CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o"

# External object files for target aruco_dcf
aruco_dcf_EXTERNAL_OBJECTS =

utils_dcf/aruco_dcf: utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o
utils_dcf/aruco_dcf: utils_dcf/CMakeFiles/aruco_dcf.dir/build.make
utils_dcf/aruco_dcf: src/libaruco.so.3.1.12
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_calib3d.so.4.1.1
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_highgui.so.4.1.1
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_features2d.so.4.1.1
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_flann.so.4.1.1
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_videoio.so.4.1.1
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_imgcodecs.so.4.1.1
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_imgproc.so.4.1.1
utils_dcf/aruco_dcf: /usr/local/lib/libopencv_core.so.4.1.1
utils_dcf/aruco_dcf: utils_dcf/CMakeFiles/aruco_dcf.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable aruco_dcf"
	cd /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/aruco_dcf.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
utils_dcf/CMakeFiles/aruco_dcf.dir/build: utils_dcf/aruco_dcf

.PHONY : utils_dcf/CMakeFiles/aruco_dcf.dir/build

utils_dcf/CMakeFiles/aruco_dcf.dir/requires: utils_dcf/CMakeFiles/aruco_dcf.dir/aruco_dcf.cpp.o.requires

.PHONY : utils_dcf/CMakeFiles/aruco_dcf.dir/requires

utils_dcf/CMakeFiles/aruco_dcf.dir/clean:
	cd /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf && $(CMAKE_COMMAND) -P CMakeFiles/aruco_dcf.dir/cmake_clean.cmake
.PHONY : utils_dcf/CMakeFiles/aruco_dcf.dir/clean

utils_dcf/CMakeFiles/aruco_dcf.dir/depend:
	cd /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12 /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/utils_dcf /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf/CMakeFiles/aruco_dcf.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : utils_dcf/CMakeFiles/aruco_dcf.dir/depend

