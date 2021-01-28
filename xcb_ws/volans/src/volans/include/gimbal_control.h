#include <ros/ros.h>
#include <iostream>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include <geometry_msgs/Twist.h>
#include <mavros_msgs/PositionTarget.h>
#include <sensor_msgs/Imu.h>
#include <Eigen/Dense>
#include "offboard_control.h"
#include <tf/transform_datatypes.h>
using namespace std;
using namespace Eigen;
class GimbalControl {
 public:
    /**
     *默认构造函数
     */
    GimbalControl(const ros::NodeHandle& nh, const ros::NodeHandle& nh_private);
    /**
     * 析构函数
     */
    ~GimbalControl();
    void initialize();

  OffboardControl OffboardControl_;
 private:
  ros::NodeHandle nh_;
  ros::NodeHandle nh_private_;
  ros::Timer cmdloop_timer_;
  void CmdLoopCallback(const ros::TimerEvent& event);
  void ImuDataCallback(const sensor_msgs::Imu &msg);
  void PublishGimbalControl();
  Eigen::Vector3d gimbal_att_;
  Eigen::Vector3d uav_curr_att_;
  ros::Subscriber imu_data_sub_;
};
