# Install script for directory: /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/aruco-uninstalled.pc"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/aruco.pc"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aruco" TYPE FILE FILES "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/arucoConfig.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/src/cmake_install.cmake")
  include("/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils/cmake_install.cmake")
  include("/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_markermap/cmake_install.cmake")
  include("/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_calibration/cmake_install.cmake")
  include("/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_dcf/cmake_install.cmake")
  include("/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/utils_fractal/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
