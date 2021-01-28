/*
 * @brief: 
 * @Version: 
 * @Autor: shuike
 * @Date: 2021-01-07 14:07:30
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-07 17:09:25
 * @FilePath: /droneLanding/src/main1.cpp
 */


#include <iostream>  
#include <opencv2/core/core.hpp>  
#include<opencv2/highgui/highgui.hpp>  
#include <opencv2/aruco/charuco.hpp>
#include "opencv2/imgproc.hpp"

using namespace cv;
using namespace std;


void gengerate_aruco_code_DICT_4X4_50(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_50);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_4X4_50_id_"+to_string(id)+".jpg", markerImage);
}

void gengerate_aruco_code_DICT_4X4_100(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_100);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DDICT_4X4_100_id_"+to_string(id)+".jpg", markerImage);
}


void gengerate_aruco_code_DICT_4X4_250(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_250);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_4X4_250_id_"+to_string(id)+".jpg", markerImage);
}

void gengerate_aruco_code_DICT_4X4_1000(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_1000);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_4X4_1000_id_"+to_string(id)+".jpg", markerImage);
}

void gengerate_aruco_code_DICT_5X5_50(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_5X5_50);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_5X5_50_id_"+to_string(id)+".jpg", markerImage);
}


void gengerate_aruco_code_DICT_5X5_100(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_5X5_100);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_5X5_100_id_"+to_string(id)+".jpg", markerImage);
}

void gengerate_aruco_code_DICT_5X5_250(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_5X5_250);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_5X5_250_id_"+to_string(id)+".jpg", markerImage);
}

void gengerate_aruco_code_DICT_5X5_1000(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_5X5_1000);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_5X5_1000_"+to_string(id)+".jpg", markerImage);
}



void gengerate_aruco_code_DICT_6X6_50(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_50);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_6X6_50_"+to_string(id)+".jpg", markerImage);
}

void gengerate_aruco_code_DICT_7X7_50(int id)
{

	// to gengerate a new maker
	cv::Mat markerImage;//创建存储marker的Mat对象
	cv::Ptr<cv::aruco::Dictionary> mdictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_7X7_50);
	cv::aruco::drawMarker(mdictionary, id, 500, markerImage, 1);//生成marker ID:11  大小500x500像素  存放至Mat对象

	imshow("test", markerImage);//显示marker
	waitKey();
	imwrite("aruco_marker_DICT_7X7_50_"+to_string(id)+".jpg", markerImage);
}

int main()
{
    for (int i = 0; i < 50; i++)
    {
        /* code */
        gengerate_aruco_code_DICT_7X7_50(i);
    }
	return 0;
}