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
CMAKE_SOURCE_DIR = /home/xcb/shuikeWorkSpace/opencv-4.2.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xcb/shuikeWorkSpace/opencv-4.2.0/build

# Include any dependencies generated for this target.
include modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/depend.make

# Include the progress variables for this target.
include modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/progress.make

# Include the compile flags for this target's objects.
include modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/flags.make

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/flags.make
modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_dnn_superres.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_dnn_superres.cpp

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_dnn_superres.cpp > CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.i

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_dnn_superres.cpp -o CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.s

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.requires:

.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.requires

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.provides: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.requires
	$(MAKE) -f modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/build.make modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.provides.build
.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.provides

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.provides.build: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o


modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/flags.make
modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_main.cpp

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_main.cpp > CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.i

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres/test/test_main.cpp -o CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.s

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.requires:

.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.requires

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.provides: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.requires
	$(MAKE) -f modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/build.make modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.provides.build
.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.provides

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.provides.build: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o


# Object files for target opencv_test_dnn_superres
opencv_test_dnn_superres_OBJECTS = \
"CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o" \
"CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o"

# External object files for target opencv_test_dnn_superres
opencv_test_dnn_superres_EXTERNAL_OBJECTS =

bin/opencv_test_dnn_superres: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o
bin/opencv_test_dnn_superres: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o
bin/opencv_test_dnn_superres: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/build.make
bin/opencv_test_dnn_superres: lib/libopencv_ts.a
bin/opencv_test_dnn_superres: lib/libopencv_dnn_superres.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_highgui.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_quality.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_datasets.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_videoio.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_imgcodecs.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_text.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_ml.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_dnn.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_features2d.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_flann.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_imgproc.so.4.2.0
bin/opencv_test_dnn_superres: lib/libopencv_core.so.4.2.0
bin/opencv_test_dnn_superres: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable ../../bin/opencv_test_dnn_superres"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/opencv_test_dnn_superres.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/build: bin/opencv_test_dnn_superres

.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/build

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/requires: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_dnn_superres.cpp.o.requires
modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/requires: modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/test/test_main.cpp.o.requires

.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/requires

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/clean:
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres && $(CMAKE_COMMAND) -P CMakeFiles/opencv_test_dnn_superres.dir/cmake_clean.cmake
.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/clean

modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/depend:
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xcb/shuikeWorkSpace/opencv-4.2.0 /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/dnn_superres /home/xcb/shuikeWorkSpace/opencv-4.2.0/build /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : modules/dnn_superres/CMakeFiles/opencv_test_dnn_superres.dir/depend

