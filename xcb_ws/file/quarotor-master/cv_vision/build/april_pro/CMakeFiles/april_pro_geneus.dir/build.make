# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

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
CMAKE_SOURCE_DIR = /home/odroid/cv_vision/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/odroid/cv_vision/build

# Utility rule file for april_pro_geneus.

# Include the progress variables for this target.
include april_pro/CMakeFiles/april_pro_geneus.dir/progress.make

april_pro_geneus: april_pro/CMakeFiles/april_pro_geneus.dir/build.make

.PHONY : april_pro_geneus

# Rule to build all files generated by this target.
april_pro/CMakeFiles/april_pro_geneus.dir/build: april_pro_geneus

.PHONY : april_pro/CMakeFiles/april_pro_geneus.dir/build

april_pro/CMakeFiles/april_pro_geneus.dir/clean:
	cd /home/odroid/cv_vision/build/april_pro && $(CMAKE_COMMAND) -P CMakeFiles/april_pro_geneus.dir/cmake_clean.cmake
.PHONY : april_pro/CMakeFiles/april_pro_geneus.dir/clean

april_pro/CMakeFiles/april_pro_geneus.dir/depend:
	cd /home/odroid/cv_vision/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/odroid/cv_vision/src /home/odroid/cv_vision/src/april_pro /home/odroid/cv_vision/build /home/odroid/cv_vision/build/april_pro /home/odroid/cv_vision/build/april_pro/CMakeFiles/april_pro_geneus.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : april_pro/CMakeFiles/april_pro_geneus.dir/depend

