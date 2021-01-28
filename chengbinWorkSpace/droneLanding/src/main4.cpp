/*
 * @brief: 创建board Demo
 * @Version: v1.0
 * @Autor: shuike
 * @Date: 2020-12-31 12:22:21
 * @LastEditors: shuike
 * @LastEditTime: 2021-01-07 14:04:37
 * @FilePath: /droneLanding/src/main4.cpp
 * @refrence:https://blog.csdn.net/qq_33446100/article/details/89186826
 */

#include <opencv2/highgui.hpp>
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
 
int main()
{
	int markersX = 1;//X轴上标记的数量5
	int markersY = 1;//Y轴上标记的数量5  本例生成5x5的棋盘
	int markerLength = 1000;//标记的长度，单位是像素100
	int markerSeparation = 20;//每个标记之间的间隔，单位像素
	int dictionaryId = cv::aruco::DICT_4X4_50;//生成标记的字典ID
	int margins = markerSeparation;//标记与边界之间的间隔
 
	int borderBits = 1;//标记的边界所占的bit位数
	bool showImage = true;
 
	Size imageSize;
	imageSize.width = markersX * (markerLength + markerSeparation) - markerSeparation + 2 * margins;
	imageSize.height =
		markersY * (markerLength + markerSeparation) - markerSeparation + 2 * margins;
 
	Ptr<aruco::Dictionary> dictionary =
		aruco::getPredefinedDictionary(aruco::PREDEFINED_DICTIONARY_NAME(dictionaryId));
 
	Ptr<aruco::GridBoard> board = aruco::GridBoard::create(markersX, markersY, float(markerLength),
		float(markerSeparation), dictionary);
 
	// show created board
	Mat boardImage;
	board->draw(imageSize, boardImage, margins, borderBits);
 
	if (showImage) {
		imshow("board", boardImage);
		imwrite("boardImage1.png",boardImage);
		waitKey(0);
	}
	imwrite("/Users/shuike/Desktop/work/svn/droneLanding/build/boardImage.png",boardImage);

	return 0;
}