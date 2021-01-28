/*
 * @brief: 校准相机(Camera Calibration) Demo,需要.yml相机参数文件
 * @Version: 
 * @Autor: shuike
 * @Date: 2020-12-31 12:32:28
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-06 16:55:20
 * @FilePath: /droneLanding/src/main8.cpp
 * @refrence: https://blog.csdn.net/qq_33446100/article/details/89192005
 */


#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/aruco.hpp>
#include <opencv2/aruco/dictionary.hpp>
#include <opencv2/aruco/charuco.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>
#include <vector>
#include <iostream>

using namespace std;
using namespace cv;
 
const double cs_knownWidth  = 0.19; /*真实距离m*/

vector< Point3f> getCornersInCameraWorld(double side, Vec3d rvec,Vec3d tvec);


/*相似三角形求距离 D = (W*F)/P 其中F为焦距，P为图像中像素宽度，W为物体实际宽度(单位m)*/
double distance_to_camera(double knownWidth, double foclaLength, double perWidth)
{
	/*compute and return the distance from the maker to the camera*/
	return (knownWidth * foclaLength) / perWidth;
}

double getDistance(cv::Point pointO,cv::Point pointA )  
{  
    double distance = 0.0;   
    distance = powf((pointO.x - pointA.x),2) + powf((pointO.y - pointA.y),2);  
    distance = sqrtf(distance);  
    return distance;   
}

/*求向量a，b之间的夹角*/
double getAngle(Point3f v1,Point3f v2)
{
	double c = 0.0,d = 0.0;
	c = v1.x*v2.x + v1.y*v2.y + v1.z*v2.z;
	d = sqrt(v1.x*v1.x + v1.y*v1.y + v1.z*v1.z) * sqrt(v2.x*v2.x + v2.y*v2.y + v2.z*v2.z);
	return acos(c/d); /*反三角*/
}


//输入参数
Mat cameraMatrix = Mat(3, 3, CV_32FC1, Scalar::all(0)); /* 摄像机内参数矩阵 */
Mat distCoeffs = Mat(1, 5, CV_32FC1, Scalar::all(0)); /* 摄像机的5个畸变系数：k1,k2,p1,p2,k3 */
double zConst = 0;//实际坐标系的距离，若工作平面与相机距离固定可设置为0
	
//计算参数
double s;
Mat rotationMatrix = Mat (3, 3, DataType<double>::type);
Mat tvec = Mat (3, 1, cv::DataType<double>::type);
void calcParameters(vector<cv::Point2f> imagePoints, vector<cv::Point3f> objectPoints)
{
	//计算旋转和平移
	Mat rvec(3, 1, cv::DataType<double>::type);
	cv::solvePnP(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec, tvec);
	cv::Rodrigues(rvec, rotationMatrix);
}

Point3f getWorldPoints(Point2f inPoints)
{
    //获取图像坐标
    cv::Mat imagePoint = cv::Mat::ones(3, 1, cv::DataType<double>::type); //u,v,1
	imagePoint.at<double>(0, 0) = inPoints.x;
	imagePoint.at<double>(1, 0) = inPoints.y;
 
	//计算比例参数S
	cv::Mat tempMat, tempMat2;
	tempMat = rotationMatrix.inv() * cameraMatrix.inv() * imagePoint;
	tempMat2 = rotationMatrix.inv() * tvec;
	s = zConst + tempMat2.at<double>(2, 0);
	s /= tempMat.at<double>(2, 0);
 
    //计算世界坐标
	Mat wcPoint = rotationMatrix.inv() * (s * cameraMatrix.inv() * imagePoint - tvec);
	Point3f worldPoint(wcPoint.at<double>(0, 0), wcPoint.at<double>(1, 0), wcPoint.at<double>(2, 0));
	return worldPoint;
}




int main()
{
	cv::VideoCapture inputVideo(1);//外置摄像头,自带摄像头请使用0
	//VideoWriter writer("VideoTest.avi", VideoWriter::fourcc('M', 'J', 'P', 'G'), 25.0, Size(640, 480));
	cv::Mat cameraMatrix, distCoeffs; // 相机参数
 
	// FileStorage fs("/Users/shuike/Desktop/work/svn/droneLanding/build/mycalibrationfile.yml", FileStorage::READ);//读取笔记本相机参数
	FileStorage fs("/Users/shuike/Desktop/work/svn/droneLanding/build/mycalibrationfile_usb2.yml", FileStorage::READ);//读取usb相机参数
	if (!fs.isOpened())
	{
		cout << "Could not open the configuration file!" << endl;
		exit(1);
	}
	fs["camera_matrix"] >> cameraMatrix;
	fs["distortion_coefficients"] >> distCoeffs;
	fs.release();
	cout << cameraMatrix << endl;
	cout << distCoeffs << endl;
 
	Ptr<aruco::Dictionary> dictionary =
		aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_50);//创建字典
 
	while (inputVideo.grab()) {
		unsigned int i = 0;
		cv::Mat image, imageCopy;

		inputVideo.retrieve(image);
		// cv::resize(image,image,cv::Size(640,480));
		cv::imshow("image",image);
		std::cout << "image.size()" << image.size() << std::endl;
		cv::Mat UndistortImage;
		cv::undistort(image,UndistortImage,cameraMatrix,distCoeffs);/*矫正图片*/
		cv::imshow("UndistortImage",UndistortImage);
		UndistortImage.copyTo(imageCopy);
 
		std::vector<int> ids;
		std::vector<std::vector<cv::Point2f> > corners;
 
		cv::aruco::detectMarkers(image, dictionary, corners, ids);// 检测markers
 
		if (ids.size() > 0) {
			cv::aruco::drawDetectedMarkers(imageCopy, corners, ids); /*绘制检测矩形和识别的id*/
			std::cout << corners[0]<< std::endl; /*4个角点*/
			for(int j = 0; j < corners.size() ; j++)
			{

				/*绘制*/
				for (int k = 0; k < corners[j].size(); k++)
				{
						cv::Point location(corners[j][k]);
						putText(imageCopy, format("index:%d [%d,%d]", k,location.x,location.y),
            			location, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 0, 0), 1, 8);
				}

				/*估计距离 真实坐标*/
				double perWidth = getDistance(corners[j][0],corners[j][1]); /*相似宽带 二维码的0点和1点点距离*/
				std::cout << "perWidth:" << perWidth << std::endl;
				double foclaLength = cameraMatrix.at<double>(0,0); /*fx=f/dx=焦距/相机平面矩阵每个像素(单位m)*/
				std::cout << "foclaLength:" << foclaLength << std::endl;
				double distance = distance_to_camera(cs_knownWidth, foclaLength, perWidth);
				std::cout << "distance:" << distance  <<" m"<< std::endl;


				/*中心点*/
				if(corners[j].size() == 4)
				{
					cv::Point center((corners[j][0] + corners[j][1] + corners[j][2] + corners[j][3])/4);
					putText(imageCopy, format("center [%d,%d]",center.x,center.y),
            			center, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 0, 0), 1, 8);

					/*计算x,y,z*/
				    // vector<Point2f> DistortCenterPnt
					// cv::undistortPoints(center,)
					cv::Vec2d imagePoint(center.x,center.y);
					std::vector<cv::Vec2d> imagePts;
					std::vector<cv::Vec2d> idealPts;
					imagePts.push_back(imagePoint);
					cv::undistortPoints(imagePts,idealPts,cameraMatrix,distCoeffs);
					const double lambda = 1.0;
					cv::Mat cameraPt(3, 1, CV_64F);
					cameraPt.at<double>(0) = idealPts[0][0] * lambda;
					cameraPt.at<double>(1) = idealPts[1][1] * lambda;
					cameraPt.at<double>(2) = lambda;


					/*求像素距离*/
					cv::Point2d imgCenter(imageCopy.cols /2,imageCopy.rows /2);
					double distance_cam2ar = getDistance(imgCenter,center);
					std::cout << "distance_cam2ar_img:" << distance_cam2ar <<std::endl;

				
				}

				
				
			}
			vector< Vec3d > rvecs, tvecs;//得到旋转向量以及平移向量
			
			/*相机的姿态R和T.*/
			/*tvecs摄影机世界 拟绘制的坐标系的转换矢量
			rvecs:模拟的坐标矢量
			cv::OutputArray rvec, //输出旋转矩阵
			旋转矩阵就是一个3*1的向量，该矩阵可以表示相机相对于世界坐标系XYZ轴的3个旋转角度。

			cv::OutputArray tvec, //输出平移矩阵
			平移矩阵也是一个3维向量，可以表示相机相对于物体的XYZ轴的偏移，而这个矩阵就是我们需要求的：我们知道了相机相对于物体的位置，也就得到了距离，从而实现了测距的目的。
			*/
			cv::aruco::estimatePoseSingleMarkers(corners, 100, cameraMatrix, distCoeffs, rvecs, tvecs); /*Pose estimation for single markers.*/
			std::cout <<"rvecs.size()"<< rvecs.size() << std::endl;
			std::cout <<"tvecs.size()"<< tvecs.size() << std::endl;

			cv::Mat rMatrix,jacobain;
			cv::Rodrigues(rvecs[0],rMatrix,jacobain);
			std::cout <<"rMatrix" << rMatrix << std::endl;
			
			for (i = 0; i < ids.size(); i++)
			{
				cv::aruco::drawAxis(imageCopy, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 10);// 画方向轴 50
	
	    		// project axes points
				float length = 10;
    			vector<Point3f> axesPoints;
    			axesPoints.push_back(Point3f(0, 0, 0));
    			axesPoints.push_back(Point3f(length, 0, 0));
    			axesPoints.push_back(Point3f(0, length, 0));
    			axesPoints.push_back(Point3f(0, 0, length));
				
    			vector<Point2f> imagePoints;
    			projectPoints(axesPoints, rvecs[i], tvecs[i], cameraMatrix, distCoeffs, imagePoints);
				std::cout << "imagePoints" << imagePoints << std::endl;
				for(int m = 0; m < imagePoints.size(); m++)
				{
					cv::Point v_point(imagePoints[m]);
					putText(imageCopy, format("V%d [%d,%d]",m,v_point.x,v_point.y),
            			v_point, FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 0, 0), 1, 8);
				}

				/*求Pitch
			  		二维码为原点
				*/

				std::cout << "tvecs[i]:" << tvecs[i] <<std::endl;
				Point3f v1(tvecs[i]); /*投影夹角*/
				v1.z = 0.0;
				std::cout << "v1:" << v1 << std::endl;
				Point3f v2(tvecs[i]); /*物体指向相机的向量*/
				std::cout << "v2:" << v2 << std::endl;
				double angle = getAngle(v1,v2);
				std::cout << "angle:" << getAngle(v1,v2) << std::endl;
				// std::cout <<"rvecs[ " + to_string(i) + "]"<< rvecs[i] << std::endl;
				std::cout <<"tvecs[ " + to_string(i) + "]"<< tvecs[i] << std::endl;


				/************************************************************************************/
				/*计算世界坐标*/
				// cv::Point2f inPoints(imageCopy.cols/2.0,imageCopy.rows/2.0); /*图像坐标*/
				// cv::Mat imagePoint = cv::Mat::ones(3,1,cv::DataType<double>::type); /*u,v,1*/
				// imagePoint.at<double>(0,0) = inPoints.x;
				// imagePoint.at<double>(1,0) = inPoints.y;

				// // /*计算参数*/
				// double s = 0.0;
				// double zConst = 0;//实际坐标系的距离，若工作平面与相机距离固定可设置为0
				// cv::Mat rotationMatrix = cv::Mat(3,3,cv::DataType<double>::type);
				// cv::Mat tevc(tvecs[i]);
				// std::cout << "tevc:" << tevc << std::endl;
				// cv::Rodrigues(tevc,rotationMatrix); /*计算旋转矩阵*/
				// std::cout << "rotationMatrix:" << rotationMatrix << std::endl;

				// // /*计算比例参数 s*/
				// cv::Mat tempMat, tempMat2;
				// tempMat = rotationMatrix.inv() * cameraMatrix.inv() * imagePoint;
				// tempMat2 = rotationMatrix.inv() * tvec;
				// s = zConst + tempMat2.at<double>(2.0);
				// s /= tempMat.at<double>(2.0);
				// std::cout << "s:" <<s<<std::endl;
				// // /*计算世界坐标系  X,Y,Z*/
				// Mat wcPoint = rotationMatrix.inv() * (s * cameraMatrix.inv() * imagePoint - tvec);
				// cv::Point3f  wordPoint(wcPoint.at<double>(0,0),wcPoint.at<double>(1,0),wcPoint.at<double>(2,0));
				// std::cout << "wordPoint:" <<wordPoint << std::endl;

				/************************************************************************************/
			/*
				std::cout <<"rvecs[ " + to_string(i) + "]"<< rvecs[i] << std::endl;
				std::cout <<"tvecs[ " + to_string(i) + "]"<< tvecs[i] << std::endl;
			*/
				

			}


			//writer << imageCopy;
		}
 
		cv::imshow("out", imageCopy);
 
		char key = (char)cv::waitKey(20);
		if (key == 'b') break;
	}
 
	return 0;
}



vector< Point3f> getCornersInCameraWorld(double side,Vec3d rvec,Vec3d tvec){
 
 double half_side = side / 2; 
 
 
 //计算rot_mat 
 Mat rot_mat; 
 cv::Rodrigues(rvec,rot_mat); 
 
 //转置rot_mat以方便提取列
 Mat rot_mat_t = rot_mat.t(); 
 
 //两个E-O和F-O向量
 double * tmp = rot_mat_t.ptr< double>(0); 
 Point3f camWorldE(tmp [0] * half_side,
 tmp [1] * half_side,
 tmp [2] * half_side); 
 
 tmp = rot_mat_t.ptr< double>(1); 
 Point3f camWorldF(tmp [0] * half_side,
 tmp [1] * half_side,
 tmp [2] * half_side); 
 
 //将tvec转换为点
 Point3f tvec_3f(tvec[0],tvec [1],tvec[2]); 
 
 //返回向量：
 vector< Point3f> ret(4,tvec_3f); 
 
 ret [0] +=  camWorldE + camWorldF; 
 ret [1] += -camWorldE + camWorldF; 
 ret [2] += -camWorldE - camWorldF; 
 ret [3] +=  camWorldE - camWorldF; 
 return ret;
}
