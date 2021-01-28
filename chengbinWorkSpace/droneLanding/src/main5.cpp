/*
 * @brief: 检测marker Demo
 * @Version: 
 * @Autor: shuike
 * @Date: 2019-01-31 16:53:26
 * @LastEditors: shuike
 * @LastEditTime: 2020-12-31 21:09:06
 * @FilePath: /droneLanding/src/main5.cpp
 * @refrence:https://blog.csdn.net/qq_33446100/article/details/89115983
 */

#include <opencv2/highgui.hpp>
#include <opencv2/aruco.hpp>
#include <opencv2/aruco/dictionary.hpp>
#include <opencv2/core.hpp>
#include <vector>
#include <iostream>
 
using namespace std;
using namespace cv;
 
int main() 
{
	cv::Mat markerImage;
	cv::VideoCapture mVideoCapture(0);//0表示使用电脑自带摄像头，>1表示使用外置摄像头
 
	//创建字典，这里注意使用Ptr<>，不然无法显示结果
	Ptr<aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_50); /*创建的和图像的必须一致*/
	cv::aruco::drawMarker(dictionary, 23, 240, markerImage);//这里取出一个marker用于检测
 
	imshow("marker", markerImage);//显示待检测标记
 
	while (mVideoCapture.grab()) {//取得下一帧
		cv::Mat frame, frame_show;
		mVideoCapture.retrieve(frame);//放入Mat
 
		frame.copyTo(frame_show);//复制一份
 
		std::vector<int> ids;
		std::vector<std::vector<cv::Point2f>> corners;
 
		cv::aruco::detectMarkers(frame, dictionary, corners, ids);//检测该帧是否有标记
 
		if (ids.size() > 0)
			cv::aruco::drawDetectedMarkers(frame_show, corners, ids);//如果有，则标记出来，放入另一个Mat
 
		cv::imshow("video", frame_show);//显示结果
 
		char key = (char)waitKey(30);
		if (key == 'b') break;
	}
 
	return 0;
}