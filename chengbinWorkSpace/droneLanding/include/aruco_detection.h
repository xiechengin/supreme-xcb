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
 * @LastEditTime: 2021-01-18 14:50:46
 * @FilePath: /droneLanding/include/aruco_detection.h
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
#include "dbg.h"

class aruco_detection  
{
    public:
        /*获取x,y,z,q,pitch,info*/
        int init(); /*初始相机设备(启动线程一直读取摄像头资源)*/

        int process(cv::Mat &frame);
        int process80x80_4Aruco_1Circle(cv::Mat &frame);

        /*导航组组长要求点信息*/
        double get_aruco_x() {return m_aruco_x;}; /*x(相对摄像头中心为原点)*/
        double get_aruco_y() {return m_aruco_y;}; /*y(相对摄像头中心为原点)*/
        double get_aruco_z() {return m_aruco_z;}; /*z(相对摄像头中心为原点)*/
        double get_aruco_q() {return m_aruco_q;}; /*(目标点相对镜头点位置,图像平面)*/
        double get_aruco_pitch() { return m_aruco_pitch;};/*pitch(相机与二维码连线点和地面的倾斜角)*/


        /*偏航，俯仰，滚动换成角度*/
        double get_aruco_rx() {return m_aruco_rx;};
		double get_aruco_ry() {return m_aruco_ry;};
		double get_aruco_rz() {return m_aruco_rz;};

        /*像素坐标*/
        cv::Point m_aruco_center; /*aruco二维码的在相机图像的坐标*/
        cv::Point m_camera_center; /*相机图像的坐标*/
        double m_center_distance; /*中心点像素坐标距离*/



        std::vector<double> get_aruco_allInfo();/*所有信息x,y,z,q,pitch,info*/
        
    private:
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


                
    private:
        cv::Mat m_src;
        cv::Mat m_gray;
        cv::Mat m_aruco_roi;
        cv::QRCodeDetector m_aruco_detector;
        std::vector<cv::Point> m_pts;

        cv::Ptr<cv::aruco::Dictionary> m_dictionary;
        cv::Mat m_image, m_image_copy;
	    cv::Mat m_camera_matrix, m_dist_coeffs;
	    std::ostringstream m_vector_to_marker;
        cv::VideoCapture m_Capture;
        
    private:
        void aruco_logger(std::string &loginfo);
        double getDistance(cv::Point pointO,cv::Point pointA);
        void drawCubeWireframe(
	        cv::InputOutputArray image, cv::InputArray cameraMatrix,
	        cv::InputArray distCoeffs, cv::InputArray rvec, cv::InputArray tvec,
	        float l
        );
	public:
		aruco_detection();
		virtual ~aruco_detection();
};

#endif // __ARUCO_DETECTION_H__