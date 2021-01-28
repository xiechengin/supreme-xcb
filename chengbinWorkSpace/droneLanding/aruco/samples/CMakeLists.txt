
# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# 要生成可执行程序的名字
project(test)

#通过pkg-config管理的三方库
SET(ENV{PKG_CONFIG_PATH} /usr/local/Cellar/opencv/4.5.0_5/lib/pkgconfig)
FIND_PACKAGE(PkgConfig REQUIRED) #PkgConfig名字是固定的，代表准备加入pkg-config模块，即查找/usr/bin/pkg-config

#eg: -- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1")
PKG_SEARCH_MODULE(PKG_OPENCV REQUIRED opencv4) #通过执行pkg-config程序，并指定我需要的模块是opencv,注意opencv名字固定，是源于安装OpenCV生成的opencv.pc，PKG_OPENCV是前缀(观察下面)，

#eg: -- Checking for one of the modules 'opencv'
# 添加三方opencv的头文件路径-- -I/home/topeet/programfile/opencv2/include/opencv -I/home/topeet/programfile/opencv2/include
INCLUDE_DIRECTORIES(${PKG_OPENCV_INCLUDE_DIRS})



#源文件 (添加自己的源文件)
set(SOURCES 
    calibrate_camera_charuco.cpp
    # src/qr_detection.cpp
    )

# Declare the executable target built from your sources
add_executable(${PROJECT_NAME} ${SOURCES})


# # 为指定的bin文件添加三方链接库
target_link_libraries(${PROJECT_NAME}  ${PKG_OPENCV_LDFLAGS})

#头文件 自动包含的目录
target_include_directories(${PROJECT_NAME} 
    PRIVATE 
        ${PROJECT_SOURCE_DIR}/include 
    )