/*
 * @brief: 
 * @Version: 
 * @Autor: shuike
 * @Date: 2020-12-30 15:15:02
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-08 10:24:41
 * @FilePath: /droneLanding/src/qr_detection.cpp
 */
#include "qr_detection.h"

int qr_detection::process(cv::Mat &in_frame)
{
    clock_t clockBegin = clock();

    cvtColor(in_frame, m_gray, cv::COLOR_BGR2GRAY);
    bool det_result = m_qrcode_detector.detect(m_gray, m_pts);

    if (det_result) {
			m_qr_info = m_qrcode_detector.decode(m_gray, m_pts, m_qrcode_roi);
	}

    /*检查点是否在*/
    cv::Rect rect = cv::boundingRect(m_pts);
    // if(0 <= rect.x && 0 <= rect.width && rect.x + rect.width <= in_frame.cols && 0 <= rect.y && 0 <= rect.height && rect.y + rect.height <= in_frame.rows)
    // {
    //     return -1;
    // }
    if(rect.x >= 0 && rect.y >= 0 &&
           (rect.x + rect.width) < in_frame.cols &&
           (rect.y + rect.height) < in_frame.rows)
 	{
         
    }


     /*轮廓信息*/	
    CV_Assert(m_pts.size() > 3);
    
	if(m_pts.size() > 3)
	{
		std::vector<std::vector<cv::Point> > contours;
		/*绘制四个点*/
		for (size_t i = 0; i < m_pts.size(); i++)
		{
			cv::putText(in_frame, cv::format("index:%d(%d,%d)",i, m_pts[i].x,m_pts[i].y),m_pts[i], cv::FONT_HERSHEY_SIMPLEX, 1.0, cv::Scalar(0, 0, 255), 2, 8);
		}

        std::cout << "rect:" << rect << std::endl;
        double area = cv::contourArea(m_pts);
        std::cout << "area:" << area << std::endl;

        imshow("in_frame_roi",in_frame(rect));

        contours.push_back(m_pts);
        
		cv::drawContours(in_frame, contours, 0, cv::Scalar(0, 0, 255), 2);
		
		clock_t clockEnd = clock();
			printf("qr_process time: %f sec \n", (double)(clockEnd - clockBegin) / CLOCKS_PER_SEC);
			putText(in_frame, m_qr_info.c_str(), cv::Point(20, 200), cv::FONT_HERSHEY_SIMPLEX, 1.0, cv::Scalar(0, 0, 255), 2, 8);
			printf("qrcode info %s \n", m_qr_info.c_str());
	}

    return 0;
}

int qr_detection::init() /*初始相机设备(启动线程一直读取摄像头资源)*/
{
    //   m_capture.open(0);
}

qr_detection::qr_detection()
{ 
    m_qr_info = "";
    m_qr_x = 0;
    m_qr_y = 0;
    m_qr_z = 0;
    m_qr_q = 0.0;
    m_qr_pitch = 0.0;
}

std::string qr_detection::get_qr_info()
{
    return m_qr_info;
}
int qr_detection::get_qr_x()
{
    return m_qr_x;
}
int qr_detection::get_qr_y()
{
    return m_qr_y;
}
int qr_detection::get_qr_z()
{
    return m_qr_z;
}
double qr_detection::get_qr_q()
{
    return m_qr_q;
}
double qr_detection::get_qr_pitch()
{
    return m_qr_pitch;
}

qr_detection::~qr_detection()
{
    
}