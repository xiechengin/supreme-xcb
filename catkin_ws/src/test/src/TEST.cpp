#include <iostream>
#include <math.h>

#include <ros/ros.h>
#include <tf/tf.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/Odometry.h>
#include "std_msgs/Float64.h"

# define PI 3.1415
using namespace std;

double x = 0.0;
double y = 0.0;
double theta = 0.0;
double roll = 0.0;
double pitch = 0.0;
double goal_theta = 0.0;



int main(int argc, char **argv)
{
ros::init(argc, argv, "turning_controller");
ros::NodeHandle n;//create a handle node

ros::Publisher pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);

ros::Rate loop_rate(10);

geometry_msgs::Twist speed;
geometry_msgs::Point goal;

while(ros::ok())
{

speed.linear.x = 1;
pub.publish(speed);

ros::spinOnce();
loop_rate.sleep();
}

return 0;
}