/**
 * @ref:
 * @autor:
 * @time:
*/
#ifndef ARUCO_CAMMER_H_
#define ARUCO_CAMMER_H_

#include <deque>
#include <mutex>

#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>
#include<opencv2/imgproc/imgproc.hpp>
#include <opencv2/aruco.hpp>
#include <opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>

#include "hxzh_aruco_cammer/SingleArucoDetection_class.hpp"

//#include<aruco_msgs/Marker.h>
//#include<aruco_msgs/MarkerArray.h>

class ARUCO_CAMMER
{
private:
    ros::NodeHandle nh_;
    ros::Subscriber color_Img_sub_;
    ros::Subscriber depth_Img_sub_;

    std::mutex Color_Image_Lock;
    std::mutex Depth_Image_Lock;

    cv::Ptr<cv::aruco::Dictionary> dictionary_;
    cv::Mat marker_img_;
    // double timeDepthImageCur;
    bool init_process = false;

    std::string color_image_topic;
    std::string depth_image_topic;
    cv::Mat K_, dist_; //　相机内参数
    double marker_length_;
    double fx,fy, cx, cy, k1, k2, p1, p2, k3;

    void ColorImageCallback(const sensor_msgs::ImagePtr& imt_ptr);
    void DepthImageCallback(const sensor_msgs::ImagePtr& imt_ptr);

    std::deque<sensor_msgs::ImagePtr> ColorImageQueue;
    std::deque<sensor_msgs::ImagePtr> DepthImageQueue;
    ArucoTableInfoType ArucoTableInf;
    SingleArucoDetection aruco;
    
public:
    ARUCO_CAMMER(ros::NodeHandle nh);
    ~ARUCO_CAMMER();
    void run(ArucoTableInfoType &AInf);
};


#endif
