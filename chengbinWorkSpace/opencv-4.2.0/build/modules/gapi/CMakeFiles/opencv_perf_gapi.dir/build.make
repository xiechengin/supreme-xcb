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
include modules/gapi/CMakeFiles/opencv_perf_gapi.dir/depend.make

# Include the progress variables for this target.
include modules/gapi/CMakeFiles/opencv_perf_gapi.dir/progress.make

# Include the compile flags for this target's objects.
include modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o: ../modules/gapi/perf/common/gapi_core_perf_tests.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/common/gapi_core_perf_tests.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/common/gapi_core_perf_tests.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/common/gapi_core_perf_tests.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o: ../modules/gapi/perf/common/gapi_imgproc_perf_tests.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/common/gapi_imgproc_perf_tests.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/common/gapi_imgproc_perf_tests.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/common/gapi_imgproc_perf_tests.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o: ../modules/gapi/perf/cpu/gapi_core_perf_tests_cpu.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_core_perf_tests_cpu.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_core_perf_tests_cpu.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_core_perf_tests_cpu.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o: ../modules/gapi/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o: ../modules/gapi/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o: ../modules/gapi/perf/gpu/gapi_core_perf_tests_gpu.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/gpu/gapi_core_perf_tests_gpu.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/gpu/gapi_core_perf_tests_gpu.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/gpu/gapi_core_perf_tests_gpu.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o: ../modules/gapi/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o: ../modules/gapi/perf/internal/gapi_compiler_perf_tests.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/internal/gapi_compiler_perf_tests.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/internal/gapi_compiler_perf_tests.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/internal/gapi_compiler_perf_tests.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o: ../modules/gapi/perf/perf_bench.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/perf_bench.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/perf_bench.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/perf_bench.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o


modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/flags.make
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o: ../modules/gapi/perf/perf_main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building CXX object modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/ccache /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o -c /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/perf_main.cpp

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.i"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/perf_main.cpp > CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.i

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.s"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi/perf/perf_main.cpp -o CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.s

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.requires:

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.provides: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.requires
	$(MAKE) -f modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.provides.build
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.provides

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.provides.build: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o


# Object files for target opencv_perf_gapi
opencv_perf_gapi_OBJECTS = \
"CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o" \
"CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o"

# External object files for target opencv_perf_gapi
opencv_perf_gapi_EXTERNAL_OBJECTS =

bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build.make
bin/opencv_perf_gapi: lib/libopencv_ts.a
bin/opencv_perf_gapi: lib/libopencv_gapi.so.4.2.0
bin/opencv_perf_gapi: lib/libopencv_highgui.so.4.2.0
bin/opencv_perf_gapi: lib/libopencv_videoio.so.4.2.0
bin/opencv_perf_gapi: lib/libopencv_imgcodecs.so.4.2.0
bin/opencv_perf_gapi: lib/libopencv_imgproc.so.4.2.0
bin/opencv_perf_gapi: lib/libopencv_core.so.4.2.0
bin/opencv_perf_gapi: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Linking CXX executable ../../bin/opencv_perf_gapi"
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/opencv_perf_gapi.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build: bin/opencv_perf_gapi

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/build

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_core_perf_tests.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/common/gapi_imgproc_perf_tests.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_core_perf_tests_cpu.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_cpu.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/cpu/gapi_imgproc_perf_tests_fluid.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_core_perf_tests_gpu.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/gpu/gapi_imgproc_perf_tests_gpu.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/internal/gapi_compiler_perf_tests.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_bench.cpp.o.requires
modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires: modules/gapi/CMakeFiles/opencv_perf_gapi.dir/perf/perf_main.cpp.o.requires

.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/requires

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/clean:
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi && $(CMAKE_COMMAND) -P CMakeFiles/opencv_perf_gapi.dir/cmake_clean.cmake
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/clean

modules/gapi/CMakeFiles/opencv_perf_gapi.dir/depend:
	cd /home/xcb/shuikeWorkSpace/opencv-4.2.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xcb/shuikeWorkSpace/opencv-4.2.0 /home/xcb/shuikeWorkSpace/opencv-4.2.0/modules/gapi /home/xcb/shuikeWorkSpace/opencv-4.2.0/build /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/gapi/CMakeFiles/opencv_perf_gapi.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : modules/gapi/CMakeFiles/opencv_perf_gapi.dir/depend
