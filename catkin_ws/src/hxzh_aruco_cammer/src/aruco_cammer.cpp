#include "aruco_cammer.h"

ARUCO_CAMMER::ARUCO_CAMMER(ros::NodeHandle nh)
:nh_(nh)
{
    ros::param::param<std::string>("color_image_topic_", color_image_topic, "/camera/color/image_raw");
    ros::param::param<std::string>("depth_image_topic_", depth_image_topic, "/camera/depth/image_rect_raw");
    ros::param::param<double>("fx_", fx, 0);
    ros::param::param<double>("fy_", fy, 0);
    ros::param::param<double>("cx_", cx, 0);
    ros::param::param<double>("cy_", cy, 0);
    ros::param::param<double>("k1_", k1, 0);
    ros::param::param<double>("k2_", k2, 0);
    ros::param::param<double>("k3_", k3, 0);
    ros::param::param<double>("p1_", p1, 0);
    ros::param::param<double>("p2_", p2, 0);

    cv::Mat K = (cv::Mat_<float>(3, 3) << fx, 0, cx, 0, fy, cy, 0, 0, 1);
    cv::Mat dist = (cv::Mat_<float>(5, 1) << k1, k2, p1, p2, k3);

    color_Img_sub_ = nh_.subscribe(color_image_topic, 1,&ARUCO_CAMMER::ColorImageCallback, this);
    depth_Img_sub_ = nh_.subscribe(depth_image_topic, 1, &ARUCO_CAMMER::DepthImageCallback, this);
    //run();
}

ARUCO_CAMMER::~ARUCO_CAMMER()
{

}

void ARUCO_CAMMER::run(ArucoTableInfoType &AInf)
{
    if(!init_process)
    {
        ROS_INFO("Init all first !!!");
        std::string alibrationfilePath = "/home/xcb/catkin_ws/src/hxzh_aruco_cammer/config/D455mycalibrationfile2.yml";
        float aruco_length = 0.176;
        aruco.init(aruco_length,cv::aruco::DICT_6X6_50, alibrationfilePath);
        init_process = true;
        return;
    }
    // std::cout<<"hxzh"<<std::endl;
    if(!ColorImageQueue.empty() && !DepthImageQueue.empty())
    {
        ros::Time ColorImage_stamp = ColorImageQueue.front()->header.stamp;

        auto depth_iter = DepthImageQueue.begin();
        for(depth_iter; depth_iter != DepthImageQueue.end(); depth_iter++)
        {
            if(ColorImage_stamp < (*depth_iter)->header.stamp )
            {
                break;
            }
        }

        Color_Image_Lock.lock();
        DepthImageQueue.erase(DepthImageQueue.begin(), depth_iter);
        sensor_msgs::ImagePtr color_image;
        color_image = (ColorImageQueue.front());
        sensor_msgs::ImagePtr depth_image;
        depth_image = (DepthImageQueue.front());
        const int depth_w = depth_image->width;
        const int depth_h = depth_image->height;
        const int color_w = color_image->width;
        const int color_h = color_image->height;
        ColorImageQueue.pop_back();
        Color_Image_Lock.unlock();

        // 检验时间是否一致
        double color_image_time = color_image->header.stamp.toSec();
        double depth_image_time = depth_image->header.stamp.toSec();
        double diff_time = color_image_time - depth_image_time;
        if(diff_time < 0.01 && diff_time > -0.01)
        {
            try
            {
                cv_bridge::CvImagePtr cv_ptr;
                cv_ptr = cv_bridge::toCvCopy(color_image, sensor_msgs::image_encodings::RGB8);
                cv::Mat color_image = cv_ptr->image;

                // cv::Mat color_image(cv::Size(color_w, color_h), CV_8UC3, color_image.data, cv::Mat::AUTO_STEP);
                aruco.process(color_image, ArucoTableInf);  
                
                // // show      
                cv::Mat  color_mat = color_image;
                double aruco_Z=  ArucoTableInf.z_world_coordinate_system;
                cv::putText(color_mat, cv::format("aruco_z:%lf m",aruco_Z),
                                cv::Point(10, 20), cv::FONT_HERSHEY_SIMPLEX, 0.6,
                                cv::Scalar(0, 0, 255), 1);

                //实现深度图对齐到彩色图
                // cv::Mat result = align_Depth2Color(depth_image,color_image, profile);
       
                // double dist_to_aruco_center  =   measure_distance(color_image,ArucoTableInf.aruco_center,result,Size(10,10),profile);            //自定义窗口大小

                // cv::putText(color_mat, cv::format("depth_Z:%lf m",dist_to_aruco_center),
                //                 cv::Point(10, 50), cv::FONT_HERSHEY_SIMPLEX, 0.6,
                //                 cv::Scalar(0, 0,255), 1);


                imshow("color_image",color_image);
                //imshow("result",result);
                int key = cv::waitKey(1);
                if(char(key) == 27)return;
                //std::cout<<"hxzh1"<<std::endl;
            }
            catch(cv_bridge::Exception& e)
            {
                ROS_ERROR("cv_bridge exception: %s", e.what());
                return;
            }
            
            
            // cv::Size aruco_center = ArucoTableInf.aruco_center;
            // std::cout << "aruco_center:" <<  aruco_center << std::endl;
            // cv::Size aruco_frame_size = ArucoTableInf.image_size;
            // std::cout << "aruco_frame_szie:"<<aruco_frame_size << std::endl;
         }//else
        // {
        //     ROS_ERROR("Time aligned failed...");
        // }
    }
    AInf = ArucoTableInf;
}
// std::cout << "info" << ArucoTableInf.aruco_center  << std::endl;
void ARUCO_CAMMER::ColorImageCallback(const sensor_msgs::ImagePtr& img_ptr)
{
    Color_Image_Lock.lock();
    ColorImageQueue.push_back(img_ptr);
    Color_Image_Lock.unlock();
}

void ARUCO_CAMMER::DepthImageCallback(const sensor_msgs::ImagePtr& img_ptr)
{

    Color_Image_Lock.lock();
    DepthImageQueue.push_back(img_ptr);
    Color_Image_Lock.unlock();
}