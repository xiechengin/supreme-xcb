#sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev
#sudo apt-get update && sudo apt-get install build-essential freeglut3 freeglut3-dev libxmu-dev libxi-dev
# minimum required cmake version: 3.1.0

cmake_minimum_required(VERSION 3.10.0)

project(example)

set(CMAKE_EXPORT_COMPILE_COMMANDS 1)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread")

include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
endif()

find_package(realsense2 REQUIRED )


#OpenCV
# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI
find_package(OpenCV REQUIRED)

# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")



find_package(OpenGL REQUIRED)

find_package(PkgConfig REQUIRED)
pkg_search_module(GLFW REQUIRED glfw3)

find_package(GLUT REQUIRED)


set(SOURCES 
    src/main.cpp    
    src/SingleArucoDetection_class.cpp
)


add_executable( ${PROJECT_NAME} ${SOURCES})

include_directories(include 
    ${realsense_INCLUDE_DIR}
    ${OpenCV_INCLUDE_DIRS}
    ${OPENGL_INCLUDE_DIRS}
    ${GLFW_INCLUDE_DIRS}
    )

target_include_directories( ${PROJECT_NAME} 
    PRIVATE ${realsense_INCLUDE_DIR}
            ${PROJECT_SOURCE_DIR}/include
)

target_link_libraries( ${PROJECT_NAME} 
    ${realsense2_LIBRARY}
    ${OpenCV_LIBS}
    ${OPENGL_LIBRARIES} 
    ${GLFW_LIBRARIES}
)
