#ifndef BASE_CONTROLLER_H
#define BASE_CONTROLLER_H

#include <deque>
#include "ros/ros.h"  //ros需要的头文件
#include <geometry_msgs/Twist.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
//以下为串口通讯需要的头文件
#include <string>        
#include <iostream>
#include <cstdio>
#include <unistd.h>
#include <math.h>

#include "serial/serial.h"
#include "stdio.h"
#include "stdlib.h"
#include "sstream"
#include "bitset"
#include "algorithm"
#include "fstream"

//can通信需要的头文件
#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/can.h>
#include <linux/can/raw.h>






using std::string;
using std::exception;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;
using std::bitset;

typedef struct stOdomData{
    double wheel_radius = 0.24;//轮子,单位m
    double left_wheel_radius = 0.24;//轮子直径,单位m
    double right_wheel_radius = 0.24;   
    float deceleration_ratio=400;
    float wheel_distance = 0.42f ;    //两轮间距，单位是m
    std::string cmd_speed;
    float oriention;
    float position_x;
    float position_y;
    float liner_speed;//暂存的线速度和角速度
    float angular_speed;
    
}OdomData;



#endif
