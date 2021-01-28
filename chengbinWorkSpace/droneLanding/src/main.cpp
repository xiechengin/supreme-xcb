/*
 * @brief: 
 * @Version: 
 * @Autor: shuike
 * @Date: 2021-01-08 11:05:46
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-24 14:05:27
 * @FilePath: /droneLanding/src/main.cpp
 */

#include "SingleArucoDetection_class.h"

#include <chrono>
// using namespace std;
// using namespace std::chrono;
double fps()
{
	static double fps = 0.0;
	static int frameCount = 0;
	static auto lastTime = std::chrono::system_clock::now();
	static auto curTime = std::chrono::system_clock::now();
	
	curTime = std::chrono::system_clock::now();
	
	auto duration = std::chrono::duration_cast<std::chrono::microseconds>(curTime - lastTime);
	double duration_s = double(duration.count()) * std::chrono::microseconds::period::num / std::chrono::microseconds::period::den;

	if (duration_s > 2)//2秒之后开始统计FPS
	{
		fps = frameCount / duration_s;
		frameCount = 0;
		lastTime = curTime;
	}

	++frameCount;

	return fps;
}


int main(int argc, const char** argv) {

    std::string videoPath = "/home/xcb/shuikeWorkSpace/tello-cpulspuls/main/IMG_8433.mp4";
    std::string alibrationfilePath = "/home/xcb/shuikeWorkSpace/tello-cpulspuls/main/Tellocalibrationfile.yml";
    SingleArucoDetection aruco;
    aruco.init(0.176,cv::aruco::DICT_6X6_50,alibrationfilePath);
    cv::VideoCapture in_video;

    ArucoTableInfo arcoInfo;
    
	in_video.open(videoPath);

    cv::Mat image;

    ArucoTableInfoType myArucoInfo;
    std::string arucoTyep = "0";

    while (in_video.grab())
	{
 
		in_video.retrieve(image);
        aruco.process(image,arucoTyep,myArucoInfo);
        std::cout <<  "myArucoInfo.aruco_center:\t" << myArucoInfo.aruco_center << std::endl;
        std::cout <<  "myArucoInfo.aruco_id:\t"     << myArucoInfo.aruco_id << std::endl;
        std::cout <<  "myArucoInfo.camera_center\t" << myArucoInfo.camera_center << std::endl;
        std::cout <<  "myArucoInfo.center_distance:\t" << myArucoInfo.center_distance << std::endl;
        std::cout <<  "myArucoInfo.rx_world_coordinate_system:\t" << myArucoInfo.rx_world_coordinate_system << std::endl;
        std::cout <<  "myArucoInfo.ry_world_coordinate_system:\t" << myArucoInfo.ry_world_coordinate_system << std::endl;
        std::cout <<  "myArucoInfo.rz_world_coordinate_system:\t" << myArucoInfo.rz_world_coordinate_system << std::endl;
        std::cout <<  "myArucoInfo.x_world_coordinate_system:\t" << myArucoInfo.x_world_coordinate_system << std::endl;
        std::cout <<  "myArucoInfo.y_world_coordinate_system:\t" << myArucoInfo.y_world_coordinate_system << std::endl;
        std::cout <<  "myArucoInfo.z_world_coordinate_system:\t" << myArucoInfo.z_world_coordinate_system << std::endl;
        std::cout <<  "myArucoInfo.image_size:\t" << myArucoInfo.image_size << std::endl;
        // cv::imshow("img1",image);

        std::cout << "fps()" << fps() << std::endl;
        cv::waitKey(30);
    }
    
    return 0;
}

