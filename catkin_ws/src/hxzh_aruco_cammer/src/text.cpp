#include <iostream>
#include <math.h>

#include <ros/ros.h>
#include <tf/tf.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/Odometry.h>
#include "std_msgs/Float64.h"
#include <unistd.h>
#include <stdio.h>
#include <termio.h>
#include <sys/time.h>

# define PI 3.1415
using namespace std;

double x = 0.0;
double y = 0.0;
double theta = 0.0;
double roll = 0.0;
double pitch = 0.0;
double goal_theta = 0.0;
int state = 0;


int main(int argc, char **argv)
{
ros::init(argc, argv, "turning_controller");
ros::NodeHandle n;//create a handle node

ros::Publisher pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);

ros::Rate loop_rate(200);

geometry_msgs::Twist speed;


while(ros::ok())
{
if (state == 0){
sleep(2);
speed.linear.x = 0.2;

pub.publish(speed);
ros::spinOnce();
loop_rate.sleep();
sleep(2);
speed.linear.x = 0;
pub.publish(speed);
sleep(1);
state = 1;
}
}
return 0;
}
