##sitl_gazebo
gnome-terminal --window -e 'bash -c "roslaunch simulation sitl_precision_landing.launch; exec bash"' \
--tab -e 'bash -c "sleep 15; roslaunch px4_control mavros_mission_px4.launch; exec bash"' \
--tab -e 'bash -c "sleep 5; rosrun ros_vision image_converter; exec bash"' \


