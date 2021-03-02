#include "aruco_cammer.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "hxzh_aruco_cammer");

    ros::NodeHandle nh;
    // ros::NodeHandle pnh_("~");
    ArucoTableInfo &arucoTableInfo;
    ARUCO_CAMMER *aruco_cammer = new ARUCO_CAMMER(nh);

    ros::Rate loop_rate(200);
    while (ros::ok())
    {
        ros::spinOnce();
        loop_rate.sleep();
        aruco_cammer->run(arucoTableInfo);
    }

    return 0;
}
