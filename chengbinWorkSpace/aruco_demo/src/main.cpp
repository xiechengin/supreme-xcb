// License: Apache 2.0. See LICENSE file in root directory.
// Copyright(c) 2017 Intel Corporation. All Rights Reserved.

#include <librealsense2/rs.hpp> // Include RealSense Cross Platform API
#include "example.hpp"          // Include short list of convenience functions for rendering

#include "cv-helpers.hpp"
#include "SingleArucoDetection_class.hpp"
#include <opencv2/opencv.hpp>
#include <string>
// Capture Example demonstrates how to
// capture depth and color video streams and render them to the screen
int main(int argc, char * argv[]) try
{
    rs2::log_to_console(RS2_LOG_SEVERITY_ERROR);
    // Create a simple OpenGL window for rendering:
    window app(1280, 720, "RealSense Capture Example");

    // Declare depth colorizer for pretty visualization of depth data
    rs2::colorizer color_map;
    // Declare rates printer for showing streaming rates of the enabled streams.
    rs2::rates_printer printer;

    // Declare RealSense pipeline, encapsulating the actual device and sensors
    rs2::pipeline pipe;

    // Start streaming with default recommended configuration
    // The default video configuration contains Depth and Color streams
    // If a device is capable to stream IMU data, both Gyro and Accelerometer are enabled by default
    pipe.start();

    std::string alibrationfilePath = "/home/xcb/shuikeWorkSpace/aruco_demo/data/D455calibrationfile.yml";
    SingleArucoDetection aruco;
    float aruco_length = 0.176;
    ArucoTableInfoType ArucoTableInf;
    aruco.init(aruco_length,cv::aruco::DICT_6X6_50, alibrationfilePath);

    const auto window_name = "Display Image";
    cv::namedWindow(window_name, cv::WINDOW_AUTOSIZE);
    const auto window_name_depth = "Display depth Image";
    cv::namedWindow(window_name_depth,cv::WINDOW_AUTOSIZE); 
    while (app && ((cv::getWindowProperty(window_name, cv::WND_PROP_AUTOSIZE) >= 0))) // Application still alive?
    {
        rs2::frameset data = pipe.wait_for_frames().    // Wait for next set of frames from the camera
                             apply_filter(printer).     // Print each enabled stream frame rate
                             apply_filter(color_map);   // Find and colorize the depth data


        auto color_frame = data.get_color_frame();
        auto depth_frame = data.get_depth_frame();
        
        //if we onle received new depth frame,
        // but the color did not update, continue
        static int last_frame_number = -1;
        if(color_frame.get_frame_number() == last_frame_number) continue;

        // CConver RealSense frame to OpenCV matrix
        auto color_mat =  frame_to_mat(color_frame);
        auto depth_mat =  depth_frame_to_meters(depth_frame);

        std::cout << "color_mat.size()" << color_mat.size() << std::endl;
        std::cout << "depth_mat.size()" << depth_mat.size() << std::endl;

        aruco.process(color_mat,ArucoTableInf);  

        cv::Size aruco_center = ArucoTableInf.aruco_center;
        cv::Size aruco_frame_size = ArucoTableInf.image_size;

        // Get the depth frame's dimensions
        float depth_width = depth_frame.get_width();
        float depth_height = depth_frame.get_height();

        // Query the distance from the camera to the object in the center of the image
        float dist_to_center = depth_frame.get_distance(depth_width / 2, depth_height / 2);

        float depth_aruco_center_height = (float(aruco_center.height)/ float(aruco_frame_size.height)) * depth_height;
        float depth_aruco_center_width =  (float(aruco_center.width) / float(aruco_frame_size.width)) * depth_height;

        float dist_to_aruco_center = depth_frame.get_distance(depth_aruco_center_width,depth_aruco_center_height);
        double aruco_Z = ArucoTableInf.z_world_coordinate_system;

        // show      
		cv::putText(color_mat, cv::format("aruco_z:%lf m",aruco_Z),
						cv::Point(10, 20), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
        cv::putText(color_mat, cv::format("depth_Z:%lf m",dist_to_aruco_center),
						cv::Point(10, 50), cv::FONT_HERSHEY_SIMPLEX, 0.6,
						cv::Scalar(0, 252, 124), 1);
        // Print the distance
        std::cout << "The camera is facing an object " << dist_to_center << " meters away \r";
        

              
        cv::imshow(window_name,color_mat);
        // if (cv::waitKey(1) >= 0) break;
        static std::string dataPaht = "/home/xcb/shuikeWorkSpace/aruco_demo/data/";
        static int index = 0;
        if( cv::waitKey(1) == 's')
        {
            index = index + 1;
            std::string save_path = dataPaht+std::to_string(index) + ".jpg";
            std::cout << save_path << std::endl;
            cv::imwrite(save_path,color_mat);
        }
        // cv::imshow("depth_mat",depth_mat);
        // The show method, when applied on frameset, break it to frames and upload each frame into a gl textures
        // Each texture is displayed on different viewport according to it's stream unique id


        // 485 电机
        std::cout << "info " << ArucoTableInf.aruco_center  << std::endl;


        app.show(data);
    }

    return EXIT_SUCCESS;
}
catch (const rs2::error & e)
{
    std::cerr << "RealSense error calling " << e.get_failed_function() << "(" << e.get_failed_args() << "):\n    " << e.what() << std::endl;
    return EXIT_FAILURE;
}
catch (const std::exception& e)
{
    std::cerr << e.what() << std::endl;
    return EXIT_FAILURE;
}