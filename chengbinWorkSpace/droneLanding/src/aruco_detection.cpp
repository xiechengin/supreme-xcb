/*
 * @brief: 
 * @Version: 
 * @Autor: shuike
 * @Date: 2021-01-08 10:07:44
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-22 11:48:04
 * @FilePath: /droneLanding/src/aruco_detection.cpp
 */

#include "aruco_detection.h"


int aruco_detection::init() /*初始相机设备(启动线程一直读取摄像头资源)*/
{
    //   m_capture.open(0);
    //   in_video.retrieve(image);
    m_dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_50);
    cv::FileStorage m_fs("/Users/shuike/Desktop/work/svn/droneLanding/build/mycalibrationfile_usb2.yml", cv::FileStorage::READ);
	// cv::FileStorage m_fs("/Users/shuike/Desktop/work/svn/droneLanding/build/Tellocalibrationfile.yml", cv::FileStorage::READ);
	// /Users/shuike/Desktop/work/svn/droneLanding/build/Yu2calibrationfile.yml
	// cv::FileStorage m_fs("/Users/shuike/Desktop/work/svn/droneLanding/build/Yu2calibrationfile.yml", cv::FileStorage::READ);
    m_fs["camera_matrix"] >> m_camera_matrix;
    m_fs["distortion_coefficients"] >> m_dist_coeffs;
    m_fs.release();
    return 0;
}

aruco_detection::aruco_detection()
{
    
}

aruco_detection::~aruco_detection()
{
    
}


int aruco_detection::process(cv::Mat &frame)
{
		cv::Point aruco_center;
		clock_t  clockBegin, clockEnd; 
		clockBegin = clock(); 
        int wait_time = 30;
	    // float actual_marker_l = 0.193; // this should be in meters 二维码点长(打印A4)
		float actual_marker_l = 0.2; // this should be in meters 二维码点长(红底的80x80)
        cv::Ptr<cv::aruco::Dictionary> &dictionary= m_dictionary;
        cv::Mat camera_matrix = m_camera_matrix;
        cv::Mat dist_coeffs = m_dist_coeffs;
        cv::Mat image_copy;
        std::ostringstream vector_to_marker;


		cv::Mat UndistortImage;
		cv::undistort(frame,UndistortImage,camera_matrix,dist_coeffs);/*矫正图片*/
		// UndistortImage = frame;
		// cv::imshow("UndistortImage",UndistortImage);
		UndistortImage.copyTo(image_copy);



		// frame.copyTo(image_copy);
		std::vector<int> ids;
		std::vector<std::vector<cv::Point2f>> corners;
		cv::aruco::detectMarkers(image_copy, dictionary, corners, ids);

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
				if(i != 0)
					continue;


				cv::aruco::drawAxis(image_copy, camera_matrix, dist_coeffs, rvecs[i],tvecs[i], actual_marker_l);// 画方向轴 50
				this->m_aruco_info = std::to_string(ids[i]); 
				
				#ifdef __debug
					std::cout << "ids:" << ids[i] << std::endl;
					dbg(ids[i]);
				#endif

	    		// project axes points
				// float length = 0.193;
				
				float length = 0.175;
    			std::vector<cv::Point3f> axesPoints;
    			axesPoints.push_back(cv::Point3f(0, 0, 0));
    			axesPoints.push_back(cv::Point3f(length, 0, 0));
    			axesPoints.push_back(cv::Point3f(0, length, 0));
    			axesPoints.push_back(cv::Point3f(0, 0, length));
				
                /*绘制轴 图像坐标系*/
    			std::vector<cv::Point2f> imagePoints;
    			projectPoints(axesPoints, rvecs[i], tvecs[i], camera_matrix, dist_coeffs, imagePoints);

				#ifdef __debug
					std::cout << "imagePoints" << imagePoints << std::endl;
				#endif

				std::vector<std::string> axisV = {"o","x","y","z"};
				for(int m = 0; m < imagePoints.size() ; m++)
				{
					if( imagePoints.size() <= 4)
					{
						if(m ==0)
						{
							aruco_center = imagePoints[m]; /*图像中的二维码中心点*/ 
						}
						cv::Point v_point(imagePoints[m]);
						putText(image_copy, cv::format("%s %d [%d,%d]",axisV[m].c_str(),m,v_point.x,v_point.y),
        	    			v_point, cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(255, 0, 0), 1, 8);
					}
				}

                /*绘制矩形*/
				drawCubeWireframe(
					image_copy, camera_matrix, dist_coeffs, rvecs[i], tvecs[i],
					actual_marker_l
				);

				/*计算角度*/
				dbg(rvecs[i]); /*旋转向量*/
				/*3.01885, -0.00379782, -0.21309*/
				double deg = rvecs[i][2]/CV_PI*180;
				/*旋转矩阵*/
				cv::Mat rotationMatrix = cv::Mat(3, 3, cv::DataType<double>::type);
				cv::Rodrigues(rvecs[i], rotationMatrix);

				#ifdef __debug
					dbg(rotationMatrix);
				#endif
				
				/*
				[0.9880954012124028, -0.005615442648649193, -0.1537398611511038;
 				-0.001029225534677069, -0.9995525334357643, 0.02989437400153886;
 				-0.1538389378463714, -0.02938026048224973, -0.9876590411150477]
				*/
			
				double sy = std::sqrt(rotationMatrix.at<double>(0, 0) * rotationMatrix.at<double>(0, 0) + rotationMatrix.at<double>(1, 0)* rotationMatrix.at<double>(1, 0));
				dbg(sy);
				double x=0.0;
				double y=0.0;
				double z=0.0;
				if(sy > 1e-6)
				{
					x = std::atan2(rotationMatrix.at<double>(2, 1),rotationMatrix.at<double>(2, 2));
					y = std::atan2(-rotationMatrix.at<double>(2, 0),sy);
					z = std::atan2(-rotationMatrix.at<double>(1, 0),rotationMatrix.at<double>(0, 0)); 
				}else
				{
					x = std::atan2(-rotationMatrix.at<double>(1, 2),rotationMatrix.at<double>(1, 1));
					y = std::atan2(-rotationMatrix.at<double>(2, 0),sy);
					z = 0;
				}
				/*偏航，俯仰，滚动换成角度*/
				m_aruco_rx = x * 180.0 / CV_PI;
				m_aruco_ry = y * 180.0 / CV_PI;
				m_aruco_rz = z * 180.0 / CV_PI;
				#ifdef __debug
					dbg(m_aruco_rx);
					dbg(m_aruco_ry);
					dbg(m_aruco_rz);

					
					cv::putText(image_copy, cv::format("m_aruco_rx:%lf deg",m_aruco_rx),
						cv::Point(10, 170), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);

					cv::putText(image_copy, cv::format("m_aruco_ry:%lf deg",m_aruco_ry),
						cv::Point(10, 185), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);


					cv::putText(image_copy, cv::format("m_aruco_rz:%lf deg",m_aruco_rz),
						cv::Point(10, 200), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);	

	                /*显示信息*/
					vector_to_marker.str(std::string());
					vector_to_marker << std::setprecision(4)
						<< "x: " << std::setw(8) << tvecs[0](0) << "m";
					cv::putText(image_copy, vector_to_marker.str(),
						cv::Point(10, 30), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);

					vector_to_marker.str(std::string());
					vector_to_marker << std::setprecision(4)
						<< "y: " << std::setw(8) << tvecs[0](1) << "m";
					cv::putText(image_copy, vector_to_marker.str(),
						cv::Point(10, 50), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);

					vector_to_marker.str(std::string());
					vector_to_marker << std::setprecision(4)
						<< "z: " << std::setw(8) << tvecs[0](2) << "m";
					cv::putText(image_copy, vector_to_marker.str(),
					cv::Point(10, 70), cv::FONT_HERSHEY_SIMPLEX, 0.6,
					cv::Scalar(0, 252, 124), 1);

					cv::Point pt_x(tvecs[0](0));
					cv::Point pt_y(tvecs[0](1));
					double distance = getDistance(pt_x,pt_y);
					std::cout << "distance:" << std::endl;

					cv::putText(image_copy, cv::format("distance:%lf",distance),
						cv::Point(10, 90), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
				#endif
			}
		}

		clockEnd = clock();

		#ifdef __debug	
			/*显示耗时*/
			cv::putText(image_copy, cv::format("Elapsed time: %f sec",(double)(clockEnd - clockBegin) / CLOCKS_PER_SEC),
						cv::Point(10, 120), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
		#endif
		
		/*计算距离*/
		cv::Point2d image_center(image_copy.size()/2);
		double center_distance = getDistance(aruco_center,image_center);
		this->m_aruco_q = center_distance; 

		#ifdef __debug	
			dbg(center_distance);
	        cv::imshow("img",image_copy);
		#endif


        return 0;
}


int aruco_detection::process80x80_4Aruco_1Circle(cv::Mat &frame)
{


		cv::Point aruco_center;
		clock_t  clockBegin, clockEnd; 
		clockBegin = clock(); 
        int wait_time = 30;
		float actual_marker_l = 0.176; // this should be in meters 二维码点长(打印A4)
	    // float actual_marker_l = 0.193; // this should be in meters 二维码点长(打印A4)
		// float actual_marker_l = 0.2; // this should be in meters 二维码点长(红底的80x80)
		// float actual_marker_l = 0.4; // this should be in meters 二维码点长(红底的80x80)
        cv::Ptr<cv::aruco::Dictionary> &dictionary= m_dictionary;
        cv::Mat camera_matrix = m_camera_matrix;
        cv::Mat dist_coeffs = m_dist_coeffs;
        cv::Mat image_copy;
        std::ostringstream vector_to_marker;


		cv::Mat UndistortImage;
		cv::undistort(frame,UndistortImage,camera_matrix,dist_coeffs);/*矫正图片*/
		// cv::imshow("UndistortImage",UndistortImage);
		UndistortImage.copyTo(image_copy);


		// cv::Mat gray;
		// cv::cvtColor(image_copy,gray,cv::COLOR_BGR2GRAY);
		// cv::imshow("gray",gray);
		// cv::GaussianBlur(gray,gray,cv::Size(9,9),2,2);
		// cv::imshow("GaussianBlur",gray);
		// cv::Mat binary;
		// cv::threshold(gray,binary,50,255,cv::THRESH_BINARY);
		// cv::imshow("binary",binary);
		

		// frame.copyTo(image_copy);
		std::vector<int> ids;
		std::vector<std::vector<cv::Point2f>> corners;
		// cv::aruco::detectMarkers(image_copy, dictionary, corners, ids);
		cv::aruco::detectMarkers(UndistortImage, dictionary, corners, ids);

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
				this->m_aruco_info = std::to_string(ids[i]); 
				
				#ifdef __debug
					std::cout << "ids:" << ids[i] << std::endl;
					dbg(ids[i]);
				#endif


				/*世界坐标系x,y,z*/
				m_aruco_x = tvecs[i](0);
        		m_aruco_y = tvecs[i](1);
        		m_aruco_z = tvecs[i](2);

	    		// project axes points
				// float length = 0.193;
				float length = 0.175;
    			std::vector<cv::Point3f> axesPoints;
    			axesPoints.push_back(cv::Point3f(0, 0, 0));
    			axesPoints.push_back(cv::Point3f(length, 0, 0));
    			axesPoints.push_back(cv::Point3f(0, length, 0));
    			axesPoints.push_back(cv::Point3f(0, 0, length));
				
                /*绘制轴 图像坐标系*/
    			std::vector<cv::Point2f> imagePoints;
    			projectPoints(axesPoints, rvecs[i], tvecs[i], camera_matrix, dist_coeffs, imagePoints);

				#ifdef __debug
					std::cout << "imagePoints" << imagePoints << std::endl;
				#endif

				std::vector<std::string> axisV = {"o","x","y","z"};
				for(int m = 0; m < imagePoints.size() ; m++)
				{
					if( imagePoints.size() <= 4)
					{
						if(m ==0)
						{
							aruco_center = imagePoints[m]; /*图像中的二维码中心点*/ 
							this->m_aruco_center = imagePoints[m];
						}
						cv::Point v_point(imagePoints[m]);
						putText(image_copy, cv::format("%s %d [%d,%d]",axisV[m].c_str(),m,v_point.x,v_point.y),
        	    			v_point, cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(255, 0, 0), 1, 8);
					}
				}

                /*绘制矩形*/
				drawCubeWireframe(
					image_copy, camera_matrix, dist_coeffs, rvecs[i], tvecs[i],
					actual_marker_l
				);

				/*计算角度*/
				dbg(rvecs[i]); /*旋转向量*/
				/*3.01885, -0.00379782, -0.21309*/
				double deg = rvecs[i][2]/CV_PI*180;
				/*旋转矩阵*/
				cv::Mat rotationMatrix = cv::Mat(3, 3, cv::DataType<double>::type);
				cv::Rodrigues(rvecs[i], rotationMatrix);

				#ifdef __debug
					dbg(rotationMatrix);
				#endif
				
				/*
				[0.9880954012124028, -0.005615442648649193, -0.1537398611511038;
 				-0.001029225534677069, -0.9995525334357643, 0.02989437400153886;
 				-0.1538389378463714, -0.02938026048224973, -0.9876590411150477]
				*/
				double sy = std::sqrt(rotationMatrix.at<double>(0, 0) * rotationMatrix.at<double>(0, 0) + rotationMatrix.at<double>(1, 0)* rotationMatrix.at<double>(1, 0));
				dbg(sy);
				double x=0.0;
				double y=0.0;
				double z=0.0;
				if(sy > 1e-6)
				{
					x = std::atan2(rotationMatrix.at<double>(2, 1),rotationMatrix.at<double>(2, 2));
					y = std::atan2(-rotationMatrix.at<double>(2, 0),sy);
					z = std::atan2(-rotationMatrix.at<double>(1, 0),rotationMatrix.at<double>(0, 0)); 
				}else
				{
					x = std::atan2(-rotationMatrix.at<double>(1, 2),rotationMatrix.at<double>(1, 1));
					y = std::atan2(-rotationMatrix.at<double>(2, 0),sy);
					z = 0;
				}

				/*偏航，俯仰，滚动换成角度*/
				m_aruco_rx = x * 180.0 / CV_PI;
				m_aruco_ry = y * 180.0 / CV_PI;
				m_aruco_rz = z * 180.0 / CV_PI;

				#ifdef __debug
					dbg(m_aruco_rx);
					dbg(m_aruco_ry);
					dbg(m_aruco_rz);

					cv::putText(image_copy, cv::format("m_aruco_rx:%lf deg",m_aruco_rx),
						cv::Point(10, 170), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);

					cv::putText(image_copy, cv::format("m_aruco_ry:%lf deg",m_aruco_ry),
						cv::Point(10, 185), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);

					cv::putText(image_copy, cv::format("m_aruco_rz:%lf deg",m_aruco_rz),
						cv::Point(10, 200), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);


	                /*显示信息*/
					vector_to_marker.str(std::string());
					vector_to_marker << std::setprecision(4)
						<< "x: " << std::setw(8) << tvecs[0](0) << "m";
					cv::putText(image_copy, vector_to_marker.str(),
						cv::Point(10+i*150, 30), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);

					vector_to_marker.str(std::string());
					vector_to_marker << std::setprecision(4)
						<< "y: " << std::setw(8) << tvecs[0](1) << "m";
					cv::putText(image_copy, vector_to_marker.str(),
						cv::Point(10+i*150, 50), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);

					vector_to_marker.str(std::string());
					vector_to_marker << std::setprecision(4)
						<< "z: " << std::setw(8) << tvecs[0](2) << "m";
					cv::putText(image_copy, vector_to_marker.str(),
					cv::Point(10+i*150, 70), cv::FONT_HERSHEY_SIMPLEX, 0.6,
					cv::Scalar(0, 252, 124), 1);

					cv::Point pt_x(tvecs[0](0));
					cv::Point pt_y(tvecs[0](1));
					double distance = getDistance(pt_x,pt_y);
					std::cout << "distance:" << std::endl;

					cv::putText(image_copy, cv::format("distance:%lf",distance),
						cv::Point(10 + i*200, 90), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
				#endif
			}
		}

		clockEnd = clock();

		#ifdef __debug	
			/*显示耗时*/
			cv::putText(image_copy, cv::format("Elapsed time: %f sec",(double)(clockEnd - clockBegin) / CLOCKS_PER_SEC),
						cv::Point(10, 120), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
		#endif
		
		/*计算距离*/
		cv::Point2d image_center(image_copy.size()/2);
		m_camera_center = image_center;
		double center_distance = getDistance(aruco_center,image_center);
		this->m_center_distance = center_distance;
		this->m_aruco_q = center_distance; 




		#ifdef __debug	
			dbg(center_distance);
	        cv::imshow("img",image_copy);
		#endif
        return 0;

}



void aruco_detection::drawCubeWireframe(
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



double aruco_detection::getDistance(cv::Point pointO,cv::Point pointA )  
{  
    double distance = 0.0;   
    distance = powf((pointO.x - pointA.x),2) + powf((pointO.y - pointA.y),2);  
    distance = sqrtf(distance);  
    return distance;   
}