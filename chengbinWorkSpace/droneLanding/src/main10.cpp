/*
 * @brief: 第二个AR Demo-画Cube
 * @Version: 
 * @Autor: shuike
 * @Date: 2020-12-31 14:52:07
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-11 15:57:54
 * @FilePath: /droneLanding/src/main10.cpp
 * @refrence:https://blog.csdn.net/qq_33446100/article/details/95796560
 */

#include <iostream>
#include <opencv2/aruco.hpp>
#include <opencv2/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/core/utils/logger.hpp>
#include <vector>

// #define CV_LOGTAG_EXPAND_NAME CV_LOG_INFO

using namespace std;
using namespace cv;

void drawCubeWireframe(
	cv::InputOutputArray image, cv::InputArray cameraMatrix,
	cv::InputArray distCoeffs, cv::InputArray rvec, cv::InputArray tvec,
	float l
);

double getDistance(cv::Point pointO,cv::Point pointA )  
{  
    double distance = 0.0;   
    distance = powf((pointO.x - pointA.x),2) + powf((pointO.y - pointA.y),2);  
    distance = sqrtf(distance);  
    return distance;   
}

int main(int argc, char **argv)
{
	int wait_time = 30;
	float actual_marker_l = 0.193; // this should be in meters 二维码点长

	VideoWriter writer("VideoTest.avi", VideoWriter::fourcc('M', 'J', 'P', 'G'), 20.0, Size(640, 480));

	cv::Mat image, image_copy;
	cv::Mat camera_matrix, dist_coeffs;
	std::ostringstream vector_to_marker;

	cv::VideoCapture in_video;
	in_video.open(1);
	cv::Ptr<cv::aruco::Dictionary> dictionary =
		cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_50);

	// cv::FileStorage fs("/Users/shuike/Desktop/work/svn/droneLanding/build/mycalibrationfile.yml", cv::FileStorage::READ);
	cv::FileStorage fs("/Users/shuike/Desktop/work/svn/droneLanding/build/mycalibrationfile_usb2.yml", cv::FileStorage::READ);
	

// %YAML:1.0
// ---
// image_width: 1280
// image_height: 720
// camera_matrix: !!opencv-matrix
//    rows: 3
//    cols: 3
//    dt: d
//    data: [ 1.0469767604608298e+03, 0., 5.9853976023463395e+02,
//            0.,1.0430263713114271e+03, 3.5645459145653604e+02, 
//            0., 0., 1. ]
// distortion_coefficients: !!opencv-matrix
//    rows: 1
//    cols: 5
//    dt: d
//    data: [ 8.2382597445800981e-02, -2.2498207643305578e-02,
//        -2.7418174646471941e-03, -1.5825004421531050e-02,
//        -1.3837111976553737e-01 ]

	/*相机矩阵
	[fx,0,cx,
	 0, fy,cy,
	 0,0,1]
	 
	 fx,fy焦距
	 cx,cy小孔中心点
	*/
	fs["camera_matrix"] >> camera_matrix;
	/*畸变参数标定
	多项式畸变系数,纠正相机坐标关系
	(k1,k2,p1,p2,k3) 
	https://docs.opencv.org/4.5.0/d4/d94/tutorial_camera_calibration.html
	*/
	fs["distortion_coefficients"] >> dist_coeffs;

	std::cout << "camera_matrix\n"
		<< camera_matrix << std::endl;
	std::cout << "\ndist coeffs\n"
		<< dist_coeffs << std::endl;

	int frame_width = 480;
	int frame_height = 640;

	clock_t  clockBegin, clockEnd; 

	while (in_video.grab())
	{

		// ‪CV_LOG_DEBUG(NULL, ‪cv::format("cv::samples::findFile('%s', %s)", relative_path.c_str(), required ? "true" : "false"));
		// ‪CV_LOG_DEBUG
		CV_LOG_DEBUG(nullptr,"shuike123456");
		
		clockBegin = clock(); 

		// ‪CV_LOG_DEBUG(NULL, ‪cv::format("shuike", relative_path.c_str(), required ? "true" : "false"));

		in_video.retrieve(image);
		
		image.copyTo(image_copy);
		std::vector<int> ids;
		std::vector<std::vector<cv::Point2f>> corners;
		cv::aruco::detectMarkers(image, dictionary, corners, ids);

		// if at least one marker detected
		if (ids.size() > 0)
		{
			cv::aruco::drawDetectedMarkers(image_copy, corners, ids); /*id*/
			
			std::vector<cv::Vec3d> rvecs, tvecs;
			cv::aruco::estimatePoseSingleMarkers(
				corners, actual_marker_l, camera_matrix, dist_coeffs,
				rvecs, tvecs
			);

			// draw axis for each marker
			for (int i = 0; i < ids.size(); i++)
			{
				cv::aruco::drawAxis(image_copy, camera_matrix, dist_coeffs, rvecs[i],tvecs[i], actual_marker_l);// 画方向轴 50

				std::cout << "ids:" << ids[i] << std::endl;
				
	    		// project axes points
				float length = 0.193;
    			vector<Point3f> axesPoints;
    			axesPoints.push_back(Point3f(0, 0, 0));
    			axesPoints.push_back(Point3f(length, 0, 0));
    			axesPoints.push_back(Point3f(0, length, 0));
    			axesPoints.push_back(Point3f(0, 0, length));
				
    			vector<Point2f> imagePoints;
    			projectPoints(axesPoints, rvecs[i], tvecs[i], camera_matrix, dist_coeffs, imagePoints);
				std::cout << "imagePoints" << imagePoints << std::endl;
				std::vector<std::string> axisV = {"o","x","y","z"};
				for(int m = 0; m < imagePoints.size() ; m++)
				{
					if( imagePoints.size() <= 4)
					{

						cv::Point v_point(imagePoints[m]);
						putText(image_copy, format("%s %d [%d,%d]",axisV[m].c_str(),m,v_point.x,v_point.y),
        	    			v_point, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 0, 0), 1, 8);
					}
				}

				drawCubeWireframe(
					image_copy, camera_matrix, dist_coeffs, rvecs[i], tvecs[i],
					actual_marker_l
				);

				vector_to_marker.str(std::string());
				vector_to_marker << std::setprecision(4)
					<< "x: " << std::setw(8) << tvecs[0](0) << "m";
				cv::putText(image_copy, vector_to_marker.str(),
					Point(10, 30), cv::FONT_HERSHEY_SIMPLEX, 0.6,
					Scalar(0, 252, 124), 1);

				vector_to_marker.str(std::string());
				vector_to_marker << std::setprecision(4)
					<< "y: " << std::setw(8) << tvecs[0](1) << "m";
				cv::putText(image_copy, vector_to_marker.str(),
					Point(10, 50), cv::FONT_HERSHEY_SIMPLEX, 0.6,
					Scalar(0, 252, 124), 1);

				vector_to_marker.str(std::string());
				vector_to_marker << std::setprecision(4)
					<< "z: " << std::setw(8) << tvecs[0](2) << "m";
				cv::putText(image_copy, vector_to_marker.str(),
					Point(10, 70), cv::FONT_HERSHEY_SIMPLEX, 0.6,
					Scalar(0, 252, 124), 1);

				/*计算执行时间*/
				

				/*计算距离*/

				cv::Point pt_x(tvecs[0](0));
				cv::Point pt_y(tvecs[0](1));
				double distance = getDistance(pt_x,pt_y);
				std::cout << "distance:" << std::endl;

				cv::putText(image_copy, format("distance:%lf",distance),
					Point(10, 90), cv::FONT_HERSHEY_SIMPLEX, 0.6,
					Scalar(0, 252, 124), 1);

			}
		}

		cv::imshow("Pose estimation", image_copy);

		writer << image_copy;

		char key = (char)cv::waitKey(wait_time);
		if (key == 'b')
			break;
			
	}

}

void drawCubeWireframe(
	cv::InputOutputArray image, cv::InputArray cameraMatrix,
	cv::InputArray distCoeffs, cv::InputArray rvec, cv::InputArray tvec,
	float l
)
{

	CV_Assert(
		image.getMat().total() != 0 &&
		(image.getMat().channels() == 1 || image.getMat().channels() == 3)
	);
	CV_Assert(l > 0);
	float half_l = l / 2.0;

	// project cube points
	std::vector<cv::Point3f> axisPoints;
	axisPoints.push_back(cv::Point3f(half_l, half_l, l));
	axisPoints.push_back(cv::Point3f(half_l, -half_l, l));
	axisPoints.push_back(cv::Point3f(-half_l, -half_l, l));
	axisPoints.push_back(cv::Point3f(-half_l, half_l, l));
	axisPoints.push_back(cv::Point3f(half_l, half_l, 0));
	axisPoints.push_back(cv::Point3f(half_l, -half_l, 0));
	axisPoints.push_back(cv::Point3f(-half_l, -half_l, 0));
	axisPoints.push_back(cv::Point3f(-half_l, half_l, 0));

	std::vector<cv::Point2f> imagePoints;
	projectPoints(
		axisPoints, rvec, tvec, cameraMatrix, distCoeffs, imagePoints
	);

	// draw cube edges lines
	cv::line(image, imagePoints[0], imagePoints[1], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[0], imagePoints[3], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[0], imagePoints[4], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[1], imagePoints[2], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[1], imagePoints[5], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[2], imagePoints[3], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[2], imagePoints[6], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[3], imagePoints[7], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[4], imagePoints[5], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[4], imagePoints[7], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[5], imagePoints[6], cv::Scalar(255, 0, 0), 3);
	cv::line(image, imagePoints[6], imagePoints[7], cv::Scalar(255, 0, 0), 3);

	/*相机中心*/
	cv::line(image, cv::Point2d(image.cols(),image.rows()/2), cv::Point2d(0,image.rows()/2), cv::Scalar(255, 0, 0), 3);
	cv::line(image, cv::Point2d(image.cols()/2,image.rows()), cv::Point2d(image.cols()/2,0), cv::Scalar(255, 0, 0), 3);
}

