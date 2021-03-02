/******************************************************************
基于串口通信的ROS小车基础控制器，功能如下：
1.实现ros控制数据通过固定的格式和串口通信，从而达到控制小车的移动
2.订阅了/cmd_vel主题，只要向该主题发布消息，就能实现对控制小车的移动
3.发布里程计主题/odm

*******************************************************************/
#include "base_controller/base_controller.h"
#include "base_controller/motec_motor_driver.h"
//#include "base_controller/serial.h"
/****************************************************************************/
int count_flag = 0;
std::ofstream myfile("/home/nav/record/odom_linear.txt",std::ios::out); 
/****************************************************************************/
/****************************************************/

OdomData odom_data;
MotorDriver *driver = nullptr;   //电机对象


/************************************************************/
void callback(const geometry_msgs::Twist & cmd_input)//订阅/cmd_vel主题回调函数
{
  //std::cout<<"Speed_loop is reading:"<<std::endl;
  float angular = cmd_input.angular.z ;//获取/cmd_vel的角速度,rad/s
  float linear = cmd_input.linear.x ;//获取/cmd_vel的线速度.m/s
  //限制最高速度
  if(linear>1){linear = 1;}
  if(linear<-1){linear = -1;}
  if(angular>0.3){angular = 0.3;}
  if(angular<-0.3){angular = -0.3;}


  int l_n = ((linear - 0.5f * angular * odom_data.wheel_distance) *
              odom_data.deceleration_ratio*60)
            / (M_PI * odom_data.wheel_radius);//左轮转速
  int r_n = ((linear + 0.5f * angular * odom_data.wheel_distance) *
              odom_data.deceleration_ratio*60)
            / (M_PI * odom_data.wheel_radius);//右轮转速


  static int last_l_n = -1, last_r_n = -1;
  if (last_l_n != l_n || last_r_n != r_n) {
    ROS_INFO_STREAM("Get cmd's message:" <<std::endl<< cmd_input);

    cout<<"SET Left wheel rpm is:"<<l_n<<" SET Right wheel rpm is:"<<r_n<<endl;

    MotorDriver::SpeedCmd cmd[2];
    cmd[0].id = 1;
    cmd[0].rpm = l_n;
    cmd[1].id = 2;
    cmd[1].rpm = r_n;
    if (driver != nullptr) {
      driver->setSpeed(cmd, 2);
    }

    last_l_n = l_n;
    last_r_n = r_n;
  }
}



int main(int argc, char **argv)
{
    if(!myfile)
    {
        std::cout<<"open file failure"<<std::endl;
    }
    std::deque<float> vector_distance_sum, vector_distance_diff;

    ros::init(argc, argv, "base_controller");//初始化串口节点
    ros::NodeHandle n;  //定义节点进程句柄

    ros::Subscriber sub = n.subscribe("cmd_vel", 100, callback); //订阅/cmd_vel主题
    ros::Publisher odom_pub= n.advertise<nav_msgs::Odometry>("/hxzh/odom", 20); //定义要发布/odom主题   //todo 里程计

    static tf::TransformBroadcaster odom_broadcaster;//定义tf对象
    geometry_msgs::TransformStamped odom_trans;//创建一个tf发布需要使用的TransformStamped类型消息
    nav_msgs::Odometry odom;//定义里程计对象
    geometry_msgs::Quaternion odom_quat; //四元数变量
    odom_trans.header.frame_id = "/odom"; 
    odom_trans.child_frame_id = "/base_link"; 
    //发布坐标变换的父子坐标系
    odom.header.frame_id = "/odom";     
    odom.child_frame_id = "/base_link";
    //定义covariance矩阵，作用为解决文职和速度的不同测量的不确定性
    float covariance[36] = {0.01,   0,    0,     0,     0,     0,  // covariance on gps_x
                            0,  0.01, 0,     0,     0,     0,  // covariance on gps_y
                            0,  0,    99999, 0,     0,     0,  // covariance on gps_z
                            0,  0,    0,     99999, 0,     0,  // large covariance on rot x
                            0,  0,    0,     0,     99999, 0,  // large covariance on rot y
                            0,  0,    0,     0,     0,     0.01};  // large covariance on rot z 
    //载入covariance矩阵
    for(int i = 0; i < 36; i++)
    {
        odom.pose.covariance[i] = covariance[i];;
    }       


    ros::Rate loop_rate(10);//设置周期休眠时间
    ros::Time current_time, last_time, first_time, secord_time;
    current_time = ros::Time::now();
    last_time = ros::Time::now();

    double vx=0, th=0;
    const int kmotor_counts = 2;
    MotorDriver::SpeedCmd speed_cmds[kmotor_counts];

    std::string moto_driver = "";
    n.param<std::string>("moto_driver", moto_driver, "MOTEC"); 
     
      if (moto_driver.compare("MOTEC") == 0) {

        driver = new MOTECMotorDriver(0); //构造函数

       //string port("/dev/Motec");//小车串口号
        //string baudrate = "19200";
        //tring read_timeout = "50";

        //driver->setParams(port + "," + baudrate + "," + read_timeout);

//sudo ip link set...权限不够咋解决?
	driver->init();
	
	MotorDriver::EnableCmd en_cmd[2];
     en_cmd[0].enable = 1;
     en_cmd[0].id = 0;
	   en_cmd[1].id = 1;	
   	 en_cmd[1].enable = 1;
     driver->setEnable(en_cmd,2);
 
    }
   
    if (driver == nullptr)
    {
      std::cout << "Create moto driver " << moto_driver <<" failed!" << std::endl;
      return -1;
    }


    while(ros::ok())
    {   
        current_time = ros::Time::now();
        double dt = (current_time - last_time).toSec();

        int left_rpm = 0, right_rpm = 0;
        float left_speed=0.0;
        float right_speed=0.0;

        first_time = ros::Time::now();

        for (int i = 0; i < kmotor_counts; i++) {
          speed_cmds[i].id = i;
          speed_cmds[i].rpm = 0;
        }

        if(driver->getSpeed(speed_cmds, kmotor_counts) == 0) //串口接收的数据长度正确就处理并发布里程计数据消息
        {
          left_rpm = speed_cmds[0].rpm;
          right_rpm = speed_cmds[1].rpm;

          cout<<"Read wheel speed: " <<std::dec<< left_rpm << "," << std::dec<<right_rpm <<endl;

          left_speed = (left_rpm * M_PI * odom_data.left_wheel_radius)/(odom_data.deceleration_ratio*60);//单位m/s
          right_speed = (right_rpm * M_PI * odom_data.right_wheel_radius)/(odom_data.deceleration_ratio*60);
        }

		//secord_time = ros::Time::now();
		//double dtt = (first_time - secord_time).toSec();
		//std::cout<<dtt<<std::endl;
        vx = 0.5f*(left_speed+right_speed);
        th = (right_speed-left_speed)/odom_data.wheel_distance;
        myfile<<th<<std::endl;

        float delta_x=0.0, delta_y=0.0, delta_theta=0.0; 
        delta_theta = th * dt;
        delta_x = vx * cos(odom_data.oriention + delta_theta) * dt;
        delta_y = vx * sin(odom_data.oriention + delta_theta) * dt;
        odom_data.position_x += delta_x;
        odom_data.position_y += delta_y;
        odom_data.oriention += delta_theta;
        odom_data.liner_speed = vx;
        odom_data.angular_speed = th;
		//std::cout<<"delta_x: "<<delta_x<<"	"<<"thdelta_y: "<<delta_y<<std::endl;
		
        odom_quat = tf::createQuaternionMsgFromYaw(odom_data.oriention);
        //pub tf
        //载入坐标（tf）变换时间戳
        odom_trans.header.stamp = ros::Time::now();
        odom_trans.transform.translation.x = odom_data.position_x;
        odom_trans.transform.translation.y = odom_data.position_y;
        odom_trans.transform.translation.z = 0.0;
        odom_trans.transform.rotation = odom_quat ;
            
        //载入坐标（tf）变换时间戳
        odom.header.stamp = ros::Time::now();
        //载入线速度和角速度
        odom.twist.twist.linear.x = vx;
        odom.twist.twist.angular.z = th;
        odom.pose.pose.position.x = odom_data.position_x;
        odom.pose.pose.position.y = odom_data.position_y;
        odom.pose.pose.orientation = odom_quat;
        // //发布里程计
        odom_pub.publish(odom);
        odom_broadcaster.sendTransform(odom_trans);
        ros::spinOnce();//callback函数必须处理所有问题时，才可以用到
        loop_rate.sleep();//周期休眠
        /*if(++count_flag > 2)
        {
	    ros::Duration(cmd_delay).sleep();
            my_serial->write(sWriteSingleReg.close_enabled_cmd_str);
            ROS_INFO_STREAM("Send enable");
	    std::cout << "Close Enable" << std::endl;
	    count_flag = 0;
        }*/
        last_time = current_time;   
    }
    MotorDriver::EnableCmd en_cmd[2];
    en_cmd[0].id = 0;
    en_cmd[0].enable = 0;
    //cmd[0].rpm = -l_n;
    en_cmd[1].id = 1;
    en_cmd[1].enable = 0;
    driver->setEnable(en_cmd,2);    

    driver->close();
	
    delete driver;
    myfile.close();
    return 0;
}

