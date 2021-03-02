#include <iostream>
#include <math.h>

#include <ros/ros.h>
#include <tf/tf.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/Odometry.h>
#include "std_msgs/Float64.h"
#include "aruco_cammer.h"
#include "geometry_msgs/Pose2D.h"
#include "SingleArucoDetection_class.hpp"
#include <unistd.h>
#include <stdio.h>
#include <termio.h>
#include <sys/time.h>
// #include "conio.h"

using namespace std;


double aruco_center_x = 0.0;
double aruco_center_y = 0.0;
double aruco_z = 0.0;
int state = 0;
int key;
double realdistance = 0.0;
double realtime = 0.0;
// static struct termios initial_settings, new_settings;  
// static int peek_character = -1;  
// void init_keyboard(void);  
// void close_keyboard(void);  
// int kbhit(void);  
// int readch(void); 


// double turning_contrller(double inc_theta, double theta){
//     double speed = 0.0;
// if(inc_theta >= 0) {
//     /*刚开始时缓慢加速，最高限速在base_contrller节点*/
//     if (inc_theta >  PI / 9) {
//         speed = theta * 2 / 3; 
//         if (speed< 0.08) speed = 0.08;
//     }   else if (inc_theta <  PI / 9 && inc_theta > 0.01){ /*当接近目标角度时，匀速减速，缓慢靠近目标角度*/
//         speed = inc_theta * 2 / 3;
//         if (speed< 0.05) speed = 0.04;
//     }   else if (inc_theta > -0.01 && inc_theta < 0.01){
//              speed = 0.0;
//     }
// }
// else {
//     if (inc_theta <  -PI / 9) {
//         speed = theta * 2 / 3; 
//         if (speed > -0.08) speed = -0.08;
//     }   else if (inc_theta  > -PI / 9 && inc_theta < -0.01){
//         speed = inc_theta * 2 / 3;
//         if (speed > -0.05) speed = -0.04;
//     }   else if (inc_theta > -0.01 && inc_theta < 0.01){
//     speed = 0.0;
//     }
// }
//     return speed;
// }
//  if self.state == 1:
           
//            if self.out_info[0] < 460 and self.out_info[0] >20:
//                 self.left_right_velocity = -S
//                 print ("leftleftleftleftleftleftleftleft")
//                 # time.sleep (0.1)
//                 # self.left_right_velocity =  0
//            if  self.out_info[0] > 500:  # set right velocity
//                 self.left_right_velocity = S
//                 print ('rightrightrightrightright')
//                 # time.sleep (0.1)
//                 # self.left_right_velocity =  0
//            if self.out_info[0] > 460 and self.out_info[0] < 500:
//                 self.left_right_velocity = 0
//                 print ("okokokokokokokokok")
           
//                 self.state = 2
           
//        if self.state == 2:
               
//             if self.out_info[1]<340 or self.out_info[1]>20:
//                 self.up_down_velocity = S
//                 print ('upupupupupupup')
//                 # time.sleep(0.1)
//             if  self.out_info[1]>380:
//                 self.up_down_velocity = -S
//                 print ("downdowndown")
//                 # time.sleep(0.1)
//             if  self.out_info[1]>340 and self.out_info[1]<380:
//                 self.up_down_velocity = 0
//                 self.left_right_velocity = 0
//                 print ("0k0000000000k")
//                 self.state = 4

//        if self.state == 4:
       
//             if self.out_info[2]<1.4:
//                 self.for_back_velocity = -S
//                 self.left_right_velocity = 0
//                 self.up_down_velocity = 0
//                 print ('backbackbackback')
//             if  self.out_info[2]>1.8:
//                 self.for_back_velocity = S
//                 self.left_right_velocity = 0
//                 self.up_down_velocity = 0
//                 print ("forwardforwardforward")
//             if  self.out_info[2]>1.4 and self.out_info[2]<1.8:
//                 self.up_down_velocity = 0
//                 self.left_right_velocity = 0
//                 self.for_back_velocity =  0
//                 print ("donedonedonedone")
//                 self.state = 5
       
//        if self.state == 5:
//             if self.out_info[0]<460 or self.out_info[0] >500 or self.out_info[1]<340 or self.out_info[1]>380:
//                self.state = 1

//改写成逻辑控制






void Movelogic(const geometry_msgs::Pose2D::ConstPtr &msg)
{
//ROS_INFO("x:[%d]\n",msg->x);
if(state == 0 || state ==2 || state == 3 || state == 4){
aruco_center_x = msg->x;
aruco_center_y = msg->y;
aruco_z = msg->theta;
}

}
//回调函数




// char getch(void)

// {

//     struct termios tmtemp,tm;

//     char c;

//     int fd=0;

//     if(tcgetattr(fd,&tm) != 0){      /*获取当前的终端属性设置，并保存到tm结构体中*/

//         return -1;

//     }

//     tmtemp=tm;

//     cfmakeraw(&tmtemp);     /*将tetemp初始化为终端原始模式的属性设置*/

//     if(tcsetattr(fd,TCSANOW,&tmtemp) != 0){     /*将终端设置为原始模式的设置*/

//         return -1;

//     }

//     c=getchar();

//     if(tcsetattr(fd,TCSANOW,&tm) != 0){      /*接收字符完毕后将终端设置回原来的属性*/

//         return 0;
//     }

//     return c;

// }




int getch()
{
  //  struct termios
  //    {
  //      tcflag_t c_iflag;		/* input mode flags */
  //      tcflag_t c_oflag;		/* output mode flags */
  //      tcflag_t c_cflag;		/* control mode flags */
  //      tcflag_t c_lflag;		/* local mode flags */
  //      cc_t c_line;			/* line discipline */
  //      cc_t c_cc[NCCS];		/* control characters */
  //      speed_t c_ispeed;		/* input speed */
  //      speed_t c_ospeed;		/* output speed */
  //  #define _HAVE_STRUCT_TERMIOS_C_ISPEED 1
  //  #define _HAVE_STRUCT_TERMIOS_C_OSPEED 1
  //    };
  int in;
  struct termios new_settings;
  struct termios stored_settings;
  tcgetattr(STDIN_FILENO,&stored_settings); //获得stdin 输入
  new_settings = stored_settings;           //
  new_settings.c_lflag &= (~ICANON);        //
  new_settings.c_cc[VTIME] = 0;
  tcgetattr(STDIN_FILENO,&stored_settings); //获得stdin 输入
  new_settings.c_cc[VMIN] = 1;
  tcsetattr(STDIN_FILENO,TCSANOW,&new_settings); //

  in = getchar();

  tcsetattr(STDIN_FILENO,TCSANOW,&stored_settings);
  return in;
}


// void init_keyboard()  
// {  
//     tcgetattr(0,&initial_settings);  
//     new_settings = initial_settings;  
//     new_settings.c_lflag |= ICANON;  
//     new_settings.c_lflag |= ECHO;  
//     new_settings.c_lflag |= ISIG;  
//     new_settings.c_cc[VMIN] = 1;  
//     new_settings.c_cc[VTIME] = 0;  
//     tcsetattr(0, TCSANOW, &new_settings);  
// }  
  
// void close_keyboard()  
// {  
//     tcsetattr(0, TCSANOW, &initial_settings);  
// }  
  
// int kbhit()  
// {  
//     unsigned char ch;  
//     int nread;  
  
//     if (peek_character != -1) return 1;  
//     new_settings.c_cc[VMIN]=0;  
//     tcsetattr(0, TCSANOW, &new_settings);  
//     nread = read(0,&ch,1);  
//     new_settings.c_cc[VMIN]=1;  
//     tcsetattr(0, TCSANOW, &new_settings);  
//     if(nread == 1)   
//     {  
//         peek_character = ch;  
//         return 1;  
//     }  
//     return 0;  
// }  
  
// int readch()  
// {  
//     char ch;  
  
//     if(peek_character != -1)   
//     {  
//         ch = peek_character;  
//         peek_character = -1;  
//         return ch;  
//     }  
//     read(0,&ch,1);  
//     return ch;  
// }  
   
// int mainn()  
// {   
//     char key;
//     init_keyboard();  
//     while(1)  
//     {  
//         kbhit();  
//         printf("\n%d\n", readch());  
//     }  
//     close_keyboard();  
//     key = readch();
//     return key;  
// }  



int main(int argc, char **argv)
{
ros::init(argc, argv, "subscriber");
ros::NodeHandle nh;//create a handle node

ros::Subscriber sub = nh.subscribe("aruco_data",1000,Movelogic);
ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);

ros::Rate loop_rate(10);

geometry_msgs::Twist speed;


  

 while (ros::ok())
    {
       
        //1.横着放,左右矫正后,转向,朝着二维码
        //2.正着放,转向矫正后,直接开过去

        //加入按键 或者 修改传入数据后归零
        key = getch();
  

        std::cout<<"key:"<<key<<std::endl;
        std::cout<<"msg->x:"<<aruco_center_x<<"  msg->y:"<<aruco_center_y<<"  z:"<<aruco_z<<std::endl;

        if (state == 0){

        realdistance = aruco_z;
        realtime = (realdistance - 0.4)/0.2;
        std::cout<<"time:"<<realtime<<std::endl;

        if (aruco_center_x  < 300 && aruco_center_x >20)
        {
            speed.linear.x = 0.2;
            std::cout<<"left"<<std::endl;
        }//left
        if (aruco_center_x  > 340)
        {
            speed.linear.x = -0.2;
            std::cout<<"right"<<std::endl;
        }//right
        if (aruco_center_x  < 340 && aruco_center_x > 300)
        {
            
            state = 2;        
            speed.linear.x = 0;
            std::cout<<"stop and turn around"<<std::endl;
        }//stop
        }
        std::cout<< "state:"<<state<<std::endl;
        if (state == 2)
        {
           speed.angular.z = -0.258;
           pub.publish(speed);
           sleep(6);
           speed.angular.z = 0;
           state = 3;
        }
        if (state == 3)
        {
              
        //    if (aruco_z >0.6){
        //        speed.linear.x = 0.2;
        //        std::cout<<"forward"<<std::endl;
        //    }
        //    if (aruco_z<0.6){
        //       speed.linear.x = 0;
        //       std::cout<<"done"<<std::endl;
        //       state = 4;
        //    }
        std::cout<<"time"<<realtime<<std::endl;

        if (realtime > 0){
            speed.angular.z = 0;
            speed.linear.x = 0.2;
              pub.publish(speed);
            sleep(realtime);
            speed.linear.x = 0;
            }
        if (realtime < 0){
            speed.angular.z = 0;
            speed.linear.x = -0.2;
              pub.publish(speed);
            sleep(realtime);
            speed.linear.x = 0;
            }
            state = 4;
        }//1s 0.2m
   

    if (key == 97){
        state = 5;
        aruco_center_x = 0.0;
        aruco_center_y = 0.0;
        aruco_z = 0.0;
        speed.angular.z = 0;
        speed.linear.x = 0;
    } //a stop
    if (key == 115){
       state = 1;
       aruco_center_x = 0.0;
       aruco_center_y = 0.0;
       aruco_z = 0.0;
    }//s reset
    if (key == 100){
        state =0;
    }//d restart
    
/* 
      if 
*/


        
        pub.publish(speed);

        ros::spinOnce();
        loop_rate.sleep();
       // aruco_cammer->run();
    }


return 0;
}
