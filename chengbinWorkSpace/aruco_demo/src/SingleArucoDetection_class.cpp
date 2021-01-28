/*
 * @brief: 
 * @Version: 
 * @Autor: shuike
 * @Date: 2021-01-08 10:07:44
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-25 03:01:41
 * @FilePath: /droneLanding/src/SingleArucoDetection_class.cpp
 */

#include "SingleArucoDetection_class.hpp"


int SingleArucoDetection::init(float length,ArucoType arucoType, std::string alibrationfilePath) /*初始相机设备*/
{
    //   m_capture.open(0);
    //   in_video.retrieve(image);

	// float actual_marker_l = 0.193; // this should be in meters 二维码点长(打印A4)
	// float actual_marker_l = 0.2; // this should be in meters 二维码点长(红底的80x80)
	// float actual_marker_l = 0.4; // this should be in meters 二维码点长(红底的80x80)
	this->actual_marker_l = length;
    this->m_dictionary = cv::aruco::getPredefinedDictionary(arucoType); /*cv::aruco::DICT_6X6_50*/
    cv::FileStorage m_fs(alibrationfilePath, cv::FileStorage::READ);
	// cv::FileStorage m_fs("/Users/shuike/Desktop/work/svn/droneLanding/build/Tellocalibrationfile.yml", cv::FileStorage::READ);
	// /Users/shuike/Desktop/work/svn/droneLanding/build/Yu2calibrationfile.yml
	// cv::FileStorage m_fs("/Users/shuike/Desktop/work/svn/droneLanding/build/Yu2calibrationfile.yml", cv::FileStorage::READ);
    m_fs["camera_matrix"] >> m_camera_matrix;
    m_fs["distortion_coefficients"] >> m_dist_coeffs;
    m_fs.release();


	/*启动线程一直读取摄像头资源*/


    return 0;
}

SingleArucoDetection::SingleArucoDetection()
{
    
}

SingleArucoDetection::~SingleArucoDetection()
{
    
}

int SingleArucoDetection::process(const cv::Mat &Frame,ArucoTableInfoType& ArucoTableInfo) /*, ArucoTableInfoType& ArucoTableInf*/
{

		clock_t  clockBegin, clockEnd; 
		clockBegin = clock(); 
		
        cv::Ptr<cv::aruco::Dictionary> &dictionary= m_dictionary;
        cv::Mat camera_matrix = m_camera_matrix;
        cv::Mat dist_coeffs = m_dist_coeffs;
        cv::Mat image_copy;
        std::ostringstream vector_to_marker;


		cv::Mat UndistortImage;
		cv::undistort(Frame,UndistortImage,camera_matrix,dist_coeffs);/*矫正图片*/
		UndistortImage.copyTo(image_copy);

		/*二维码检测*/
		std::vector<int> ids;
		std::vector<std::vector<cv::Point2f>> corners;
		cv::aruco::detectMarkers(UndistortImage, dictionary, corners, ids);

		// if at least one marker detected
		if (ids.size() > 0)
		{
			cv::aruco::drawDetectedMarkers(image_copy, corners, ids); /*id*/
			
			std::vector<cv::Vec3d> rvecs, tvecs;
			cv::aruco::estimatePoseSingleMarkers(
				corners, this->actual_marker_l, camera_matrix, dist_coeffs,
				rvecs, tvecs
			);

			// draw axis for each marker
			for (int i = 0; i < ids.size(); i++)
			{

				if(i !=0)
					continue;
				cv::aruco::drawAxis(image_copy, camera_matrix, dist_coeffs, rvecs[i],tvecs[i], this->actual_marker_l);// 画方向轴 50
				this->m_aruco_info = std::to_string(ids[i]); 

				
				#ifdef _aruco_debug
					std::cout << "ids:" << ids[i] << std::endl;
				#endif


				/*世界坐标系x,y,z*/
				m_aruco_x = tvecs[i](0);
        		m_aruco_y = tvecs[i](1);
        		m_aruco_z = tvecs[i](2);

	    		// project axes points
				// float length = 0.193;
    			std::vector<cv::Point3f> axesPoints;
    			axesPoints.push_back(cv::Point3f(0, 0, 0));
    			axesPoints.push_back(cv::Point3f(this->actual_marker_l, 0, 0));
    			axesPoints.push_back(cv::Point3f(0, this->actual_marker_l, 0));
    			axesPoints.push_back(cv::Point3f(0, 0, this->actual_marker_l));
				
                /*绘制轴 图像坐标系*/
    			std::vector<cv::Point2f> imagePoints;
    			projectPoints(axesPoints, rvecs[i], tvecs[i], camera_matrix, dist_coeffs, imagePoints);

				#ifdef _aruco_debug
					std::cout << "imagePoints" << imagePoints << std::endl;
				#endif

				std::vector<std::string> axisV = {"o","x","y","z"};
				for(int m = 0; m < imagePoints.size() ; m++)
				{
					if( imagePoints.size() <= 4)
					{
						if(m ==0)
						{
							this->m_aruco_center = imagePoints[m];/*图像中的二维码中心点*/ 
							cv::circle(image_copy, this->m_aruco_center, 30, cv::Scalar(0, 0, 255));
						}
						cv::Point v_point(imagePoints[m]);
						putText(image_copy, cv::format("%s %d [%d,%d]",axisV[m].c_str(),m,v_point.x,v_point.y),
        	    			v_point, cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(255, 0, 0), 1, 8);
					}
				}

                /*绘制矩形*/
				this->DrawCubeWireframe(
					image_copy, camera_matrix, dist_coeffs, rvecs[i], tvecs[i],
					this->actual_marker_l
				);

				/*计算角度*/
				std::cout << "旋转向量:" << rvecs[i] << std::endl;
				/*3.01885, -0.00379782, -0.21309*/
				double deg = rvecs[i][2]/CV_PI*180;
				/*旋转矩阵*/
				cv::Mat rotationMatrix = cv::Mat(3, 3, cv::DataType<double>::type);
				cv::Rodrigues(rvecs[i], rotationMatrix);

				#ifdef _aruco_debug
					std::cout << "rotationMatrix:" << rotationMatrix << std::endl;
				#endif
				
				/*
				[0.9880954012124028, -0.005615442648649193, -0.1537398611511038;
 				-0.001029225534677069, -0.9995525334357643, 0.02989437400153886;
 				-0.1538389378463714, -0.02938026048224973, -0.9876590411150477]
				*/
				double sy = std::sqrt(rotationMatrix.at<double>(0, 0) * rotationMatrix.at<double>(0, 0) + rotationMatrix.at<double>(1, 0)* rotationMatrix.at<double>(1, 0));
				std::cout << "sy:" << std::endl;
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

				#ifdef _aruco_debug
					std::cout << "m_aruco_rx:" <<m_aruco_rx <<std::endl;
					std::cout << "m_aruco_ry" << m_aruco_ry<<std::endl;
					std::cout << "m_aruco_rz" << m_aruco_rz<<std::endl;

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
					double distance = this->GetDistance(pt_x,pt_y);
					std::cout << "distance:" << distance<< std::endl;

					cv::putText(image_copy, cv::format("distance:%lf",distance),
						cv::Point(10 + i*200, 90), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
				#endif
			}
		}

		clockEnd = clock();

		#ifdef _aruco_debug	
			/*显示耗时*/
			cv::putText(image_copy, cv::format("Elapsed time: %f sec",(double)(clockEnd - clockBegin) / CLOCKS_PER_SEC),
						cv::Point(10, 120), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
		#endif
		
		/*计算距离*/
		cv::Point2d image_center(image_copy.size()/2);
		m_camera_center = image_center;
		double center_distance = this->GetDistance(this->m_aruco_center,image_center);
		this->m_center_distance = center_distance;
		this->m_aruco_q = center_distance; 




		#ifdef _aruco_debug	
			std::cout << "center_distance:" << center_distance << std::endl;
	        cv::imshow("img",image_copy);
		#endif


		/*信息保存出去*/
		ArucoTableInfo.aruco_id = this->m_aruco_info;

		ArucoTableInfo.aruco_center = this->m_aruco_center;
		ArucoTableInfo.camera_center= this->m_camera_center;

		ArucoTableInfo.rx_world_coordinate_system= this->m_aruco_rx;
		ArucoTableInfo.ry_world_coordinate_system= this->m_aruco_ry;
		ArucoTableInfo.rz_world_coordinate_system= this->m_aruco_rz;

		ArucoTableInfo.x_world_coordinate_system= this->m_aruco_x;
		ArucoTableInfo.y_world_coordinate_system= this->m_aruco_y;
		ArucoTableInfo.z_world_coordinate_system= this->m_aruco_z;
		
		ArucoTableInfo.ry_world_coordinate_system= this->m_aruco_ry;
		ArucoTableInfo.ry_world_coordinate_system= this->m_aruco_ry;

		ArucoTableInfo.center_distance = this->m_center_distance;

		ArucoTableInfo.image_size = Frame.size();

        return 0;

}



void SingleArucoDetection::DrawCubeWireframe(
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



double SingleArucoDetection::GetDistance(cv::Point pointO,cv::Point pointA )  
{  
    double distance = 0.0;   
    distance = powf((pointO.x - pointA.x),2) + powf((pointO.y - pointA.y),2);  
    distance = sqrtf(distance);  
    return distance;   
}