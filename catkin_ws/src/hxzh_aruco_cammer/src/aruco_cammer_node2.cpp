#include "aruco_cammer.h"
#include "geometry_msgs/Pose2D.h"
#include "SingleArucoDetection_class.hpp"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "hxzh_aruco_cammer");

    ros::NodeHandle nh;
    // ros::NodeHandle pnh_("~");
    

    ros::Publisher pub = nh.advertise<geometry_msgs::Pose2D>("aruco_data", 1000);



    geometry_msgs::Pose2D center;


    ArucoTableInfo arucoTableInfo;

   


    ARUCO_CAMMER *aruco_cammer = new ARUCO_CAMMER(nh);

    ros::Rate loop_rate(200);
    while (ros::ok())
    {
        
        pub.publish(center);
        ros::spinOnce();
        loop_rate.sleep();
        aruco_cammer->run(arucoTableInfo);
        //center = ArucoTableInf.aruco_center
        center.x = arucoTableInfo.aruco_center.x;
        center.y = arucoTableInfo.aruco_center.y;
        center.theta = arucoTableInfo.z_world_coordinate_system;
      // std::cout<<"center.x:"<<center.x<<std::endl;
      // std::cout<<"center.y:"<<center.y<<std::endl;
        
    }

    return 0;
}
//想要获得的数据
//ArucoTableInfo.aruco_center    x,y
//ArucoTableInfo.camera_center:[320, 240]
 

 