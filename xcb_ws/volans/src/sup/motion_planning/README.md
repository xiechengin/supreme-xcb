# motion_planning

- ros_moveit
- ......

## ros_moveit

1：安装moveit包

```
 sudo apt-get install ros-melodic-moveit
```
2：配置moveit

```
roslaunch moveit_setup_assistant setup_assistant.launch
```

视频指导：[moveit_config]()

```
rotors_description_dir:=/home/bingo/project/some/src/simulation/urdf/iris_depth_camera/xacro visual_material:=green
```

运行demo

```
roslaunch ros_moveit_config demo.launch
```

Controller.Yaml 

该文件描述了控制器管理器使用的参数。
```
controller_list:
 - name: iris_group_controller
   action_ns: follow_multi_dof_joint_trajectory
   type: FollowMultiDOFJointTrajectory
   default: true
   joints:
    - virtual_joint
```