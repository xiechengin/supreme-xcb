/*
 * @brief: 获取二维码的信息
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
 * @LastEditTime: 2020-12-30 20:19:13
 * @FilePath: /droneLanding/include/qr_detection.h
 */

#ifndef __QR_DETECTION_H__
#define __QR_DETECTION_H__

#include <opencv2/opencv.hpp>
#include <iostream>
#include <ctime>

class qr_detection  
{
    public:
        /*获取x,y,z,q,pitch,info*/
        int init(); /*初始相机设备(启动线程一直读取摄像头资源)*/

        /*导航组组长要求点信息*/
        std::string get_qr_info(); /*x(相对摄像头中心为原点)*/
        int get_qr_x(); /*x(相对摄像头中心为原点)*/
        int get_qr_y(); /*y(相对摄像头中心为原点)*/
        int get_qr_z(); /*z(相对摄像头中心为原点)*/
        double get_qr_q(); /*(目标点相对镜头点位置)*/
        double get_qr_pitch();/*pitch(相机与二维码连线点和地面的倾斜角),*/


        /*自己点api*/
        int process(cv::Mat &frame);

    private:
        std::string m_qr_info;
        int m_qr_x;
        int m_qr_y;
        int m_qr_z;
        double m_qr_q;
        double m_qr_pitch;
        
    private:
        // cv::VideoCapture m_capture;
        
        cv::Point m_qr_center;

        cv::Mat m_src;
        cv::Mat m_gray;
        cv::Mat m_qrcode_roi;
        cv::QRCodeDetector m_qrcode_detector;
        std::vector<cv::Point> m_pts;
    
    private:
        void qr_logger(std::string &loginfo);
    
	public:
		qr_detection();
		virtual ~qr_detection();

};

#endif // __QR_DETECTION_H__