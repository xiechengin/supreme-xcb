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



double turning_contrller(double inc_theta, double theta){
    double speed = 0.0;
if(inc_theta >= 0) {
    /*刚开始时缓慢加速，最高限速在base_contrller节点*/
    if (inc_theta >  PI / 9) {
        speed = theta * 2 / 3; 
        if (speed< 0.08) speed = 0.08;
    }   else if (inc_theta <  PI / 9 && inc_theta > 0.01){ /*当接近目标角度时，匀速减速，缓慢靠近目标角度*/
        speed = inc_theta * 2 / 3;
        if (speed< 0.05) speed = 0.04;
    }   else if (inc_theta > -0.01 && inc_theta < 0.01){
             speed = 0.0;
    }
}
else {
    if (inc_theta <  -PI / 9) {
        speed = theta * 2 / 3; 
        if (speed > -0.08) speed = -0.08;
    }   else if (inc_theta  > -PI / 9 && inc_theta < -0.01){
        speed = inc_theta * 2 / 3;
        if (speed > -0.05) speed = -0.04;
    }   else if (inc_theta > -0.01 && inc_theta < 0.01){
    speed = 0.0;
    }
}
    return speed;
}

void NewGoal(const std_msgs::Float64::ConstPtr &msg) {
    goal_theta = msg->data;     /*NICE!!!!!*/
}





/*回调函数, 订阅里程计信息,转换到本地x,y坐标*/
void NewOdom(const nav_msgs::Odometry::ConstPtr& msg)
{
x = msg->pose.pose.position.x;	
y = msg->pose.pose.position.y;
tf::Quaternion rot_q;
tf::quaternionMsgToTF(msg->pose.pose.orientation,rot_q);
tf::Matrix3x3(rot_q).getRPY(roll,pitch,theta);
//tf::Matrix3x3.getRPY(roll,pitch,yaw);
//(roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w]);
}





int main(int argc, char **argv)
{
ros::init(argc, argv, "turning_controller");
ros::NodeHandle n;//create a handle node

ros::Subscriber sub = n.subscribe("/odom",10000,NewOdom);// 订阅里程计信息
ros::Publisher pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
ros::Subscriber sub_theta = n.subscribe("/goal_theta", 10000, NewGoal); //订阅/goal_theta主题 

ros::Rate loop_rate(10);

geometry_msgs::Twist speed;
geometry_msgs::Point goal;

goal.x = 0;
goal.y = 0;
while(ros::ok())
{
double inc_x = goal.x - x;
double inc_y = goal.y - y;
double inc_theta = goal_theta - theta; 

double distance_to_goal = sqrt(inc_x*inc_x+inc_y*inc_y); 
double angle_to_goal = atan2(inc_y, inc_x);//  反正切

ROS_INFO("inc_theta: %.4lf\n", inc_theta);
ROS_INFO("theta: %.4lf\n", theta);
speed.angular.z = turning_contrller(inc_theta, theta);
pub.publish(speed);

ros::spinOnce();
loop_rate.sleep();
}

return 0;
}
