/*
 * @brief: 建立地图
 * @Version: 
 * @Autor: shuike
 * @Date: 2021-01-07 15:10:41
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-22 13:37:34
 * @FilePath: /droneLanding/src/main13.cpp
 */


#include <iostream>  
#include <opencv2/core/core.hpp>  
#include<opencv2/highgui/highgui.hpp>  
#include <opencv2/aruco/charuco.hpp>
#include "opencv2/imgproc.hpp"


int getMap()
{
    std::string imgPath = "/home/shuike/shuikeWorkSpace/code/gitee/droneLanding/images/aruco_marker_DICT_6X6_50_0-49/aruco_marker_DICT_6X6_50_0.jpg";
    cv::Mat mark = cv::imread(imgPath);
    cv::Mat map = cv::Mat(cv::Size(1000,1000),mark.type());
    cv::Mat mapRed = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,0,255));
    cv::Mat mapGreen = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,255,0));
    cv::Mat mapBlue = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(255,0,0));
    cv::Mat mapBlack = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(128,0,128));

    /*拷贝*/
    mapRed.copyTo(map(cv::Rect(0,0,map.cols/2,map.rows/2)));
    mapGreen.copyTo(map(cv::Rect(map.cols/2,0,map.cols/2,map.rows/2)));
    mapBlue.copyTo(map(cv::Rect(map.cols/2,map.rows/2,map.cols/2,map.rows/2)));
    mapBlack.copyTo(map(cv::Rect(0,map.cols/2,map.cols/2,map.rows/2)));

    mark.copyTo(map(cv::Rect(map.cols/4,map.rows/4,map.cols/2,map.rows/2)));

    cv::imshow("img",map);

	cv::waitKey(0);

    cv::imwrite("map.jpg",map);

    return 0;

}



int getMap1()
{
    std::string imgPath = "/home/shuike/shuikeWorkSpace/code/gitee/droneLanding/images/aruco_marker_DICT_6X6_50_0-49/aruco_marker_DICT_6X6_50_0.jpg";
    cv::Mat mark = cv::imread(imgPath);
    cv::Mat map = cv::Mat(cv::Size(1000,1000),mark.type());
    cv::Mat mapRed = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,0,255));
    cv::Mat mapGreen = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,255,0));
    cv::Mat mapBlue = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(255,0,0));
    cv::Mat mapBlack = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(128,0,128));

    /*拷贝*/
    mapRed.copyTo(map(cv::Rect(0,0,map.cols/2,map.rows/2)));
    mapGreen.copyTo(map(cv::Rect(map.cols/2,0,map.cols/2,map.rows/2)));
    mapBlue.copyTo(map(cv::Rect(map.cols/2,map.rows/2,map.cols/2,map.rows/2)));
    mapBlack.copyTo(map(cv::Rect(0,map.cols/2,map.cols/2,map.rows/2)));

    mark.copyTo(map(cv::Rect(map.cols/4,map.rows/4,map.cols/2,map.rows/2)));

    cv::resize(map,map,cv::Size(2000,2000));
    cv::imshow("img",map);

	cv::waitKey(0);


    cv::imwrite("map.jpg",map);

    return 0;

}


int getMap2()
{
    std::string imgPath = "/home/shuike/shuikeWorkSpace/code/gitee/droneLanding/images/aruco_marker_DICT_6X6_50_0-49/aruco_marker_DICT_6X6_50_0.jpg";
    cv::Mat mark = cv::imread(imgPath);
    cv::resize(mark,mark,mark.size()/2);
    cv::Mat map = cv::Mat(cv::Size(1000,1000),mark.type());
    cv::Mat mapRed = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,0,255));
    cv::Mat mapGreen = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,255,0));
    cv::Mat mapBlue = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(255,0,0));
    cv::Mat mapBlack = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(128,0,128));

    /*拷贝*/
    mapRed.copyTo(map(cv::Rect(0,0,map.cols/2,map.rows/2)));
    mapGreen.copyTo(map(cv::Rect(map.cols/2,0,map.cols/2,map.rows/2)));
    mapBlue.copyTo(map(cv::Rect(map.cols/2,map.rows/2,map.cols/2,map.rows/2)));
    mapBlack.copyTo(map(cv::Rect(0,map.cols/2,map.cols/2,map.rows/2)));

    mark.copyTo(map(cv::Rect(100,100,mark.cols,mark.rows)));

    mark.copyTo(map(cv::Rect(650,100,mark.cols,mark.rows)));

    mark.copyTo(map(cv::Rect(100,650,mark.cols,mark.rows)));

    mark.copyTo(map(cv::Rect(650,650,mark.cols,mark.rows)));
    
    // mark.copyTo(map(cv::Rect((map.cols-map.cols/10)-mark.cols,map.rows/6,mark.cols,mark.rows)));

    // mark.copyTo(map(cv::Rect(map.cols/4,map.rows/4,mark.cols,mark.rows)));

    // mark.copyTo(map(cv::Rect(map.cols/4,mark.rows/4,mark.cols,mark.rows)));

    cv::resize(map,map,cv::Size(2000,2000));

    /*画圆*/
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 300,  cv::Scalar(0, 0, 0),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 250,  cv::Scalar(255, 255, 255),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 200, cv::Scalar(0, 0, 0),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 150, cv::Scalar(255, 255, 255),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 100, cv::Scalar(0, 0, 0),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 50, cv::Scalar(255, 255, 255),-1);

    line(map, cv::Point(map.cols/2 -15, map.cols/2 -15), cv::Point(map.cols/2 +15, map.cols/2 +15), cv::Scalar(89, 90, 90), 3);
    line(map, cv::Point(map.cols/2 +15, map.cols/2 -15), cv::Point(map.cols/2 -15, map.cols/2 +15), cv::Scalar(89, 90, 90), 3);

    cv::imshow("img",map);

	cv::waitKey(0);

    cv::imwrite("map.jpg",map);

    return 0;

}


int getMap3()
{
        std::string imgPath = "/home/shuike/shuikeWorkSpace/code/gitee/droneLanding/images/aruco_marker_DICT_6X6_50_0-49/aruco_marker_DICT_6X6_50_0.jpg";
    cv::Mat mark = cv::imread(imgPath);
    cv::resize(mark,mark,mark.size()/2);
    cv::Mat map = cv::Mat(cv::Size(1000,1000),mark.type());
    cv::Mat mapRed = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,0,255));
    cv::Mat mapGreen = cv::Mat(cv::Size(1000,1000),mark.type(),cv::Scalar(0,255,0));
    cv::Mat mapBlue = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(255,0,0));
    cv::Mat mapBlack = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(128,0,128));

    /*拷贝*/
    // mapRed.copyTo(map(cv::Rect(0,0,map.cols/2,map.rows/2)));
    mapGreen.copyTo(map(cv::Rect(0,0,map.cols,map.rows)));
    // mapBlue.copyTo(map(cv::Rect(map.cols/2,map.rows/2,map.cols/2,map.rows/2)));
    // mapBlack.copyTo(map(cv::Rect(0,map.cols/2,map.cols/2,map.rows/2)));

    mark.copyTo(map(cv::Rect(100,100,mark.cols,mark.rows)));

    mark.copyTo(map(cv::Rect(650,100,mark.cols,mark.rows)));

    mark.copyTo(map(cv::Rect(100,650,mark.cols,mark.rows)));

    mark.copyTo(map(cv::Rect(650,650,mark.cols,mark.rows)));
    
    // mark.copyTo(map(cv::Rect((map.cols-map.cols/10)-mark.cols,map.rows/6,mark.cols,mark.rows)));

    // mark.copyTo(map(cv::Rect(map.cols/4,map.rows/4,mark.cols,mark.rows)));

    // mark.copyTo(map(cv::Rect(map.cols/4,mark.rows/4,mark.cols,mark.rows)));

    cv::resize(map,map,cv::Size(2000,2000));

    /*画圆*/
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 300,  cv::Scalar(0, 0, 0),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 250,  cv::Scalar(255, 255, 255),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 200, cv::Scalar(0, 0, 0),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 150, cv::Scalar(255, 255, 255),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 100, cv::Scalar(0, 0, 0),-1);
    cv::circle(map, cv::Point(map.cols/ 2, map.rows / 2), 50, cv::Scalar(255, 255, 255),-1);

    line(map, cv::Point(map.cols/2 -15, map.cols/2 -15), cv::Point(map.cols/2 +15, map.cols/2 +15), cv::Scalar(89, 90, 90), 3);
    line(map, cv::Point(map.cols/2 +15, map.cols/2 -15), cv::Point(map.cols/2 -15, map.cols/2 +15), cv::Scalar(89, 90, 90), 3);

    cv::imshow("img",map);

	cv::waitKey(0);

    cv::imwrite("map.jpg",map);

    return 0;

}

int getMap4()
{
        std::string imgPath = "/home/shuike/shuikeWorkSpace/code/gitee/droneLanding/images/aruco_marker_DICT_6X6_50_0-49/aruco_marker_DICT_6X6_50_0.jpg";
    cv::Mat mark = cv::imread(imgPath);
    std::cout << "mark:size" << mark.size() << std::endl;
    cv::resize(mark,mark,cv::Size(700,700));
    cv::Mat map = cv::Mat(cv::Size(1000,1000),mark.type());
    cv::Mat mapRed = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(0,0,255));
    cv::Mat mapGreen = cv::Mat(cv::Size(1000,1000),mark.type(),cv::Scalar(0,255,0));
    cv::Mat mapBlue = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(255,0,0));
    cv::Mat mapBlack = cv::Mat(cv::Size(500,500),mark.type(),cv::Scalar(128,0,128));
    cv::Mat mapWhite = cv::Mat(cv::Size(1000,1000),mark.type(),cv::Scalar(255,255,255));

    /*拷贝*/
    // mapRed.copyTo(map(cv::Rect(0,0,map.cols/2,map.rows/2)));
    mapWhite.copyTo(map(cv::Rect(0,0,map.cols,map.rows)));
    // mapBlue.copyTo(map(cv::Rect(map.cols/2,map.rows/2,map.cols/2,map.rows/2)));
    // mapBlack.copyTo(map(cv::Rect(0,map.cols/2,map.cols/2,map.rows/2)));

    mark.copyTo(map(cv::Rect(150,150,mark.cols,mark.rows)));

    int h = map.cols-200;
    int w = map.rows-200;
    cv::Rect rect = cv::Rect(100,100,h,w);
    cv::rectangle(map, rect, cv::Scalar(0, 0, 0),30, cv::LINE_8,0);
    

    cv::imshow("img",map);

	cv::waitKey(0);

    float fx = 0.0, fy = 0.0;
    cv::resize(map,map,cv::Size(2000,2000));
    cv::imwrite("map.jpg",map);

    return 0;

}


int main(int argc, char** argv)
{
    getMap4();
    return 0;
}
