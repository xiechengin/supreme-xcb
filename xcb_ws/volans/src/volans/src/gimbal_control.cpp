/***************************************************************************************************************************
*
* Author: bingo
* Email: bingobin.lw@gmail.com
* Time: 2020.05.13
* Description: 实现mavlink控制px4 gimbal
***************************************************************************************************************************/
#include "gimbal_control.h"
using namespace std;
using namespace Eigen;
GimbalControl::GimbalControl(const ros::NodeHandle& nh, const ros::NodeHandle& nh_private):
  nh_(nh),
  nh_private_(nh_private) 
{
  initialize();
  cmdloop_timer_ = nh_.createTimer(ros::Duration(0.02), &GimbalControl::CmdLoopCallback, this); //定义运行周期为0.02s,50hz
  imu_data_sub_ = nh_private_.subscribe("/mavros/imu/data", 1, &GimbalControl::ImuDataCallback, this,ros::TransportHints().tcpNoDelay());
}

GimbalControl::~GimbalControl() 
{
  //Destructor
}
void GimbalControl::CmdLoopCallback(const ros::TimerEvent& event)
{
	PublishGimbalControl();
}

void GimbalControl::PublishGimbalControl()
{
  gimbal_att_[0] = -uav_curr_att_[0]/pi*180*4;
  gimbal_att_[1] = uav_curr_att_[1]/pi*180*4;
  gimbal_att_[2] = 10;
  OffboardControl_.send_mount_control_command(gimbal_att_);
}

void GimbalControl::ImuDataCallback(const sensor_msgs::Imu &msg)
{

  //四元数转欧拉角 其中uav_curr_att_[0]为roll方向角度 左倾roll- 右倾roll+，uav_curr_att_[1]为pitch方向角度 下倾pitch+，uav_curr_att_[2]为yaw方向角度
  tf::Quaternion quat;
  tf::quaternionMsgToTF(msg.orientation,quat);
  tf::Matrix3x3(quat).getRPY(uav_curr_att_[0],uav_curr_att_[1],uav_curr_att_[2]);
//  cout << "uav_curr_att_[0]:"  << uav_curr_att_[0]/pi*180 << endl;
//  cout << "uav_curr_att_[1]:"  << uav_curr_att_[1]/pi*180 << endl;
//  cout << "uav_curr_att_[2]:"  << uav_curr_att_[2]/pi*180 << endl;
}
void GimbalControl::initialize()
{
  gimbal_att_[0] = 0;
  gimbal_att_[1] = 0;
  gimbal_att_[2] = 0;
  uav_curr_att_[0] = 0;
  uav_curr_att_[1] = 0;
  uav_curr_att_[2] = 0;

}
int main(int argc, char** argv) 
{
  ros::init(argc,argv,"ros_nav_quadrotor");
  ros::NodeHandle nh("");
  ros::NodeHandle nh_private("~");

  GimbalControl GimbalControl(nh, nh_private);

  ros::spin();
  return 0;
}
