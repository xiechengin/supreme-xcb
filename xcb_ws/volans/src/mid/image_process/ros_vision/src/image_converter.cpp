#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

static const std::string OPENCV_WINDOW = "Image window";

cv::VideoWriter Write("/home/eason/volans/src/mid/image_process/ros_vision/write.avi",CV_FOURCC('M','J','P','G'),30.0,cv::Size(640,480));


class ImageConverter
{
    ros::NodeHandle nh_;
    image_transport::ImageTransport it_;
    image_transport::Subscriber image_sub_;

public:
    ImageConverter()
        :   it_(nh_)
    {
        image_sub_ = it_.subscribe("/camera/rgb/image_raw",1,&ImageConverter::imageCb,this);
        // image_pub_ = it_.advertise("/image_converter/output_video",1);

        cv::namedWindow(OPENCV_WINDOW);
    }

    ~ImageConverter()
    {
        cv::destroyWindow(OPENCV_WINDOW);
    }

    void imageCb(const sensor_msgs::ImageConstPtr& msg)
    {
        cv_bridge::CvImagePtr cv_ptr;
        try
        {
            cv_ptr = cv_bridge::toCvCopy(msg,sensor_msgs::image_encodings::BGR8);
        }
        catch (cv_bridge::Exception& e)
        {
            ROS_ERROR("cv_bridge exception: %s", e.what());
            return ;            
        }

    Write<<cv_ptr->image;
    std::cout<<"video is saving to /home/eason/volans/src/mid/image_process/ros_vision/write.avi ..."<<std::endl;

    cv::imshow(OPENCV_WINDOW, cv_ptr->image);
    cv::waitKey(3);

    }

};

int main(int argc, char** argv)
{
    ros::init(argc,argv,"image_converter");
    ImageConverter ic;
    ros::spin();
    return 0;
}
