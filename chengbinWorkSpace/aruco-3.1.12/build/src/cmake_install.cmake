# Install script for directory: /media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src

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

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xmainx" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libaruco.so.3.1.12"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libaruco.so.3.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libaruco.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/src/libaruco.so.3.1.12"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/src/libaruco.so.3.1"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/build/src/libaruco.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libaruco.so.3.1.12"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libaruco.so.3.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libaruco.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/usr/local/lib:"
           NEW_RPATH "")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/aruco" TYPE FILE FILES
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/aruco_cvversioning.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/cameraparameters.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/dictionary_based.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/ippe.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/markerdetector_impl.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/markermap.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/timers.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/aruco_export.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/cvdrawingutils.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/dictionary.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/levmarq.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/marker.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/picoflann.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/aruco.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/debug.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/markerdetector.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/markerlabeler.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/posetracker.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/fractaldetector.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/aruco/fractallabelers" TYPE FILE FILES
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/fractallabelers/fractalposetracker.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/fractallabelers/fractalmarkerset.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/fractallabelers/fractalmarker.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/fractallabelers/fractallabeler.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/aruco/dcf" TYPE FILE FILES
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/dcf/dcfmarkermaptracker.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/dcf/dcfmarkertracker.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/dcf/dcf_utils.h"
    "/media/psf/Home/Desktop/work/ParallesWorkSpace/shuike/aruco-3.1.12/src/dcf/trackerimpl.h"
    )
endif()

