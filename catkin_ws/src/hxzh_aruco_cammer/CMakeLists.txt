cmake_minimum_required(VERSION 3.0.2)
project(hxzh_aruco_cammer)

add_compile_options(-std=c++11)
#SET(CMAKE_BUILD_TYPE Release)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  cv_bridge
  sensor_msgs
#  aruco_msgs
)

catkin_package()

find_package(OpenCV 3.0 QUIET)
find_package(Eigen3  REQUIRED)

include_directories(
  ${catkin_INCLUDE_DIRS}
  include
  ${EIGEN3_INCLUDE_DIR}
  ${PCL_INCLUDE_DIRS}
)

add_executable(hxzh_aruco_cammer_node
  src/aruco_cammer_node2.cpp
  src/aruco_cammer.cpp
  src/SingleArucoDetection_class.cpp
  )
  
target_link_libraries(hxzh_aruco_cammer_node
  ${catkin_LIBRARIES}
  ${OpenCV_LIBS}
  ${EIGEN3_LIBS}
)

add_executable(subscriber
  src/qr_control.cpp
  )
  
target_link_libraries(subscriber
  ${catkin_LIBRARIES}
)

add_executable(text
  src/text.cpp
  )
  
target_link_libraries(text
  ${catkin_LIBRARIES}
)
