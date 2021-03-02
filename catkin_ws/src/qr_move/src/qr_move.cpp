    #include <iostream>
    #include <math.h>

    #include <ros/ros.h>
    #include <tf/tf.h>
    #include <geometry_msgs/Twist.h>
    #include <geometry_msgs/Pose.h>
    #include <geometry_msgs/Point.h>
    #include <nav_msgs/Odometry.h>

    using namespace std;

    double x = 0.0;
    double y = 0.0;
    double theta = 0.0;
    double rot_q = 0.0;
    double roll = 0.0;
    double pitch = 0.0;

    // void NewOdom(const nav_msgs::Odometry::ConstPtr& msg)
    // {
    // x = msg->pose.pose.position.x;
    // y = msg->pose.pose.position.y;

    // rot_q = msg->pose.pose.orientation;
    // (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w]);
    // }

    int main(int argc, char **argv){

    ros::init(argc, argv, "speed_controller");
    ros::NodeHandle n;//create a handle node

    // ros::Subscriber sub = n.subscribe("/odometry/filtered", &NewOdom, this);
    ros::Publisher pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1);

    ros::Rate loop_rate(10);

    geometry_msgs::Twist speed;
    geometry_msgs::Point goal;

    while(ros::ok())
    {
 
    speed.linear.x = 0.5;
   
    pub.publish(speed);

    ros::spinOnce();
    }

    return 0;
