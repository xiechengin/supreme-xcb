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
include modules/quality/CMakeFiles/opencv_test_quality.dir/depend.make

# Include the progress variables for this target.
include modules/quality/CMakeFiles/opencv_test_quality.dir/progress.make

# Include the compile flags for this target's objects.
include modules/quality/CMakeFiles/opencv_test_quality.dir/flags.make

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o: modules/quality/CMakeFiles/opencv_test_quality.dir/flags.make
modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_brisque.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_brisque.cpp

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_brisque.cpp > CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.i

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_brisque.cpp -o CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.s

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.requires:

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.requires

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.provides: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.requires
	$(MAKE) -f modules/quality/CMakeFiles/opencv_test_quality.dir/build.make modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.provides.build
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.provides

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.provides.build: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o


modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o: modules/quality/CMakeFiles/opencv_test_quality.dir/flags.make
modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_gmsd.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_gmsd.cpp

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_gmsd.cpp > CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.i

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_gmsd.cpp -o CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.s

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.requires:

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.requires

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.provides: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.requires
	$(MAKE) -f modules/quality/CMakeFiles/opencv_test_quality.dir/build.make modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.provides.build
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.provides

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.provides.build: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o


modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o: modules/quality/CMakeFiles/opencv_test_quality.dir/flags.make
modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_main.cpp

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_main.cpp > CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.i

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_main.cpp -o CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.s

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.requires:

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.requires

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.provides: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.requires
	$(MAKE) -f modules/quality/CMakeFiles/opencv_test_quality.dir/build.make modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.provides.build
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.provides

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.provides.build: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o


modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o: modules/quality/CMakeFiles/opencv_test_quality.dir/flags.make
modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_mse.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_mse.cpp

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_mse.cpp > CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.i

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_mse.cpp -o CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.s

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.requires:

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.requires

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.provides: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.requires
	$(MAKE) -f modules/quality/CMakeFiles/opencv_test_quality.dir/build.make modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.provides.build
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.provides

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.provides.build: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o


modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o: modules/quality/CMakeFiles/opencv_test_quality.dir/flags.make
modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_psnr.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_psnr.cpp

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_psnr.cpp > CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.i

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_psnr.cpp -o CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.s

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.requires:

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.requires

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.provides: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.requires
	$(MAKE) -f modules/quality/CMakeFiles/opencv_test_quality.dir/build.make modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.provides.build
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.provides

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.provides.build: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o


modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o: modules/quality/CMakeFiles/opencv_test_quality.dir/flags.make
modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_ssim.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o -c /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_ssim.cpp

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_ssim.cpp > CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.i

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality/test/test_ssim.cpp -o CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.s

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.requires:

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.requires

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.provides: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.requires
	$(MAKE) -f modules/quality/CMakeFiles/opencv_test_quality.dir/build.make modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.provides.build
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.provides

modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.provides.build: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o


# Object files for target opencv_test_quality
opencv_test_quality_OBJECTS = \
"CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o" \
"CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o" \
"CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o" \
"CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o" \
"CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o" \
"CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o"

# External object files for target opencv_test_quality
opencv_test_quality_EXTERNAL_OBJECTS =

bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o
bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o
bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o
bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o
bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o
bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o
bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/build.make
bin/opencv_test_quality: lib/libopencv_ts.a
bin/opencv_test_quality: lib/libopencv_quality.so.4.1.1
bin/opencv_test_quality: lib/libopencv_highgui.so.4.1.1
bin/opencv_test_quality: lib/libopencv_ml.so.4.1.1
bin/opencv_test_quality: lib/libopencv_videoio.so.4.1.1
bin/opencv_test_quality: lib/libopencv_imgcodecs.so.4.1.1
bin/opencv_test_quality: lib/libopencv_imgproc.so.4.1.1
bin/opencv_test_quality: lib/libopencv_core.so.4.1.1
bin/opencv_test_quality: modules/quality/CMakeFiles/opencv_test_quality.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable ../../bin/opencv_test_quality"
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/opencv_test_quality.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
modules/quality/CMakeFiles/opencv_test_quality.dir/build: bin/opencv_test_quality

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/build

modules/quality/CMakeFiles/opencv_test_quality.dir/requires: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_brisque.cpp.o.requires
modules/quality/CMakeFiles/opencv_test_quality.dir/requires: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_gmsd.cpp.o.requires
modules/quality/CMakeFiles/opencv_test_quality.dir/requires: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_main.cpp.o.requires
modules/quality/CMakeFiles/opencv_test_quality.dir/requires: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_mse.cpp.o.requires
modules/quality/CMakeFiles/opencv_test_quality.dir/requires: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_psnr.cpp.o.requires
modules/quality/CMakeFiles/opencv_test_quality.dir/requires: modules/quality/CMakeFiles/opencv_test_quality.dir/test/test_ssim.cpp.o.requires

.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/requires

modules/quality/CMakeFiles/opencv_test_quality.dir/clean:
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality && $(CMAKE_COMMAND) -P CMakeFiles/opencv_test_quality.dir/cmake_clean.cmake
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/clean

modules/quality/CMakeFiles/opencv_test_quality.dir/depend:
	cd /home/xcb/shuikeWorkSpace/opencv-4.1.1/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xcb/shuikeWorkSpace/opencv-4.1.1 /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/quality /home/xcb/shuikeWorkSpace/opencv-4.1.1/build /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/quality/CMakeFiles/opencv_test_quality.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : modules/quality/CMakeFiles/opencv_test_quality.dir/depend

