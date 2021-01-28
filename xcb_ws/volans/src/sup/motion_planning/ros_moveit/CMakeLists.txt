cmake_minimum_required(VERSION 2.8.8 FATAL_ERROR)

project(dronedoc)

add_compile_options(-std=c++11)

find_package(Boost 1.4.0 COMPONENTS system filesystem REQUIRED)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  mavros_msgs
  roscpp
  sensor_msgs
  nav_msgs
  nav_core
  tf
  costmap_2d
  actionlib
  trajectory_msgs
  pluginlib
  moveit_msgs
  moveit_core
)

find_package(yaml-cpp REQUIRED)
find_package(Protobuf REQUIRED)


include (FindPkgConfig)
if (PKG_CONFIG_FOUND)
  pkg_check_modules(SDF sdformat)
endif()

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES map_builder
  CATKIN_DEPENDS
    geometry_msgs
    mavros_msgs
    roscpp
    sensor_msgs
    nav_msgs
    nav_core
    tf
    navigation
    actionlib
    moveit_core
    moveit_msgs
    trajectory_msgs
    pluginlib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${YAML_CPP_INCLUDE_DIR}
  ${SDF_INCLUDE_DIRS}
  ${CMAKE_CURRENT_BINARY_DIR}/msgs/proto
)

link_directories(${CMAKE_CURRENT_BINARY_DIR}/msgs/proto)


# Build moveit library
add_library(${PROJECT_NAME}_moveit_multi_dof_controller_manager src/moveit_multi_dof_controller_manager.cpp)
target_link_libraries(${PROJECT_NAME}_moveit_multi_dof_controller_manager ${catkin_LIBRARIES} ${Boost_LIBRARIES})

# Build ROS nodes
add_executable(drone_controller src/drone_controller.cpp)
add_executable(offboard_sample src/offboard_sample.cpp)
add_executable(odom_publisher src/odom_publisher.cpp)

target_link_libraries(drone_controller ${catkin_LIBRARIES})
target_link_libraries(offboard_sample ${catkin_LIBRARIES})
target_link_libraries(odom_publisher ${catkin_LIBRARIES})


