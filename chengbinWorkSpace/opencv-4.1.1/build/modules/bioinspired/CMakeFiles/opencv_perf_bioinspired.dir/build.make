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
CMAKE_SOURCE_DIR = /home/xcb/shuikeWorkSpace/opencv-4.1.1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xcb/shuikeWorkSpace/opencv-4.1.1/build

# Include any dependencies generated for this target.
include modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/depend.make

# Include the progress variables for this target.
include modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/progress.make

# Include the compile flags for this target's objects.
include modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/flags.make

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/flags.make
modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/opencl/perf_retina.ocl.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/opencl/perf_retina.ocl.cpp

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/opencl/perf_retina.ocl.cpp > CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.i

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/opencl/perf_retina.ocl.cpp -o CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.s

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.requires:

.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.requires

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.provides: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.requires
	$(MAKE) -f modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/build.make modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.provides.build
.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.provides

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.provides.build: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o


modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/flags.make
modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/perf_main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/perf_main.cpp

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/perf_main.cpp > CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.i

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired/perf/perf_main.cpp -o CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.s

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.requires:

.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.requires

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.provides: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.requires
	$(MAKE) -f modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/build.make modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.provides.build
.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.provides

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.provides.build: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o


# Object files for target opencv_perf_bioinspired
opencv_perf_bioinspired_OBJECTS = \
"CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o" \
"CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o"

# External object files for target opencv_perf_bioinspired
opencv_perf_bioinspired_EXTERNAL_OBJECTS =

bin/opencv_perf_bioinspired: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o
bin/opencv_perf_bioinspired: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o
bin/opencv_perf_bioinspired: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/build.make
bin/opencv_perf_bioinspired: lib/libopencv_ts.a
bin/opencv_perf_bioinspired: lib/libopencv_bioinspired.so.4.1.1
bin/opencv_perf_bioinspired: lib/libopencv_highgui.so.4.1.1
bin/opencv_perf_bioinspired: lib/libopencv_videoio.so.4.1.1
bin/opencv_perf_bioinspired: lib/libopencv_imgcodecs.so.4.1.1
bin/opencv_perf_bioinspired: lib/libopencv_imgproc.so.4.1.1
bin/opencv_perf_bioinspired: lib/libopencv_core.so.4.1.1
bin/opencv_perf_bioinspired: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable ../../bin/opencv_perf_bioinspired"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/opencv_perf_bioinspired.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/build: bin/opencv_perf_bioinspired

.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/build

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/requires: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/opencl/perf_retina.ocl.cpp.o.requires
modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/requires: modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/perf/perf_main.cpp.o.requires

.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/requires

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/clean:
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired && $(CMAKE_COMMAND) -P CMakeFiles/opencv_perf_bioinspired.dir/cmake_clean.cmake
.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/clean

modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/depend:
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xcb/shuikeWorkSpace/opencv-4.1.1 /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/bioinspired /home/xcb/shuikeWorkSpace/opencv-4.1.1/build /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : modules/bioinspired/CMakeFiles/opencv_perf_bioinspired.dir/depend

