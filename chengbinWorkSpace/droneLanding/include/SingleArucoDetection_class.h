/*
 * @brief: 获取aruco二维码的信息
 *          x(相对摄像头中心为原点),
 *          y(相对摄像头中心为原点),
 *          z(相对摄像头中心为原点),
 *          q(目标点相对镜头点位置),
 *          pitch(倾斜角),
 *          info(二维码信息)
 * @Version: V1.0
 * @Autor: 税科-导航组-福建省厦门海峡智慧科技有限公司
 * @Date: 2020-12-30 15:14:26
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-24 14:05:50
 * @FilePath: /droneLanding/include/SingleArucoDetection_class.h
 */

#ifndef __ARUCO_DETECTION_H__
#define __ARUCO_DETECTION_H__

/*调试开光*/
#define __debug

// #ifdef __debug
// 　　//#define debug(format,...) printf("File: "__FILE__"\nLine: %05d\nmessage: "format"\n", __LINE__, ##__VA_ARGS__)
// 　　#define debug(format,...) printf("message: "format"\n", ##__VA_ARGS__)
// #else
// 　　#define debug(format,...)
// #endif


#include <opencv2/opencv.hpp>
#include <opencv2/aruco.hpp>
#include <iostream>
#include <ctime>

/*导航组组长要求点信息*/
typedef struct ArucoTableInfo
{
    /* data */
    std::string aruco_id;
    double x_world_coordinate_system;/*x(相对摄像头中心为原点)*/
    double y_world_coordinate_system;/*y(相对摄像头中心为原点)*/
    double z_world_coordinate_system;/*z(相对摄像头中心为原点)*/

    /*偏航，俯仰，滚动换成角度*/
    double rx_world_coordinate_system;
	double ry_world_coordinate_system;
	double rz_world_coordinate_system; /*相机旋转读数(0到180度，0到-180度)*/
        

    cv::Point aruco_center; /*aruco二维码的在相机图像的坐标*/
    cv::Point camera_center; /*相机图像的坐标*/
    double center_distance; /*中心点像素坐标距离*/    

    cv::Size image_size;
}ArucoTableInfoType;


class SingleArucoDetection  
{
    
    typedef cv::aruco::PREDEFINED_DICTIONARY_NAME ArucoType;/*二维码类型*/

    public:
        SingleArucoDetection();
        virtual ~SingleArucoDetection();
        int init(float length,ArucoType arucoType, std::string alibrationfilePath); /*初始相机设备(启动线程一直读取摄像头资源)*/
        int process(const cv::Mat &Frame, const std::string ArucoID, ArucoTableInfoType& ArucoTableInfo);
        
    private:
        float actual_marker_l;
        std::string m_aruco_info;        
        double m_aruco_x;
        double m_aruco_y;
        double m_aruco_z;
        double m_aruco_q;
        double m_aruco_pitch;
        
        /*偏航，俯仰，滚动换成角度*/
		double m_aruco_rx;
		double m_aruco_ry;
		double m_aruco_rz;

        cv::Point m_aruco_center; /*aruco二维码的在相机图像的坐标*/
        cv::Point m_camera_center; /*相机图像的坐标*/
        double m_center_distance; /*中心点像素坐标距离*/    

    private:
        cv::Ptr<cv::aruco::Dictionary> m_dictionary;
	    cv::Mat m_camera_matrix, m_dist_coeffs;
        
    private:
        void ArucoLogger(std::string &loginfo);
        double GetDistance(cv::Point pointO,cv::Point pointA);
        void DrawCubeWireframe(
	        cv::InputOutputArray image, cv::InputArray cameraMatrix,
	        cv::InputArray distCoeffs, cv::InputArray rvec, cv::InputArray tvec,
	        float l
        );
};

#endif // __ARUCO_DETECTION_H__