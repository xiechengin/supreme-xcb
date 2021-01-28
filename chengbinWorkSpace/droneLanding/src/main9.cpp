
/*校准相机并保存参数,产生.yml相机参数文件
https://www.pianshen.com/article/8777340891/
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
 
//保存相机参数
static bool saveCameraParams(const string &filename, Size imageSize, float aspectRatio, int flags,
	const Mat &cameraMatrix, const Mat &distCoeffs, double totalAvgErr) 
{
	FileStorage fs(filename, FileStorage::WRITE);
	if (!fs.isOpened())
		return false;
	char buf[1024];
 
	fs << "image_width" << imageSize.width;
	fs << "image_height" << imageSize.height;
 
	if (flags & CALIB_FIX_ASPECT_RATIO) fs << "aspectRatio" << aspectRatio;
 
	//这一段暂时没管
	if (flags != 0) {
		sprintf(buf, "flags: %s%s%s%s",
			flags & CALIB_USE_INTRINSIC_GUESS ? "+use_intrinsic_guess" : "",
			flags & CALIB_FIX_ASPECT_RATIO ? "+fix_aspectRatio" : "",
			flags & CALIB_FIX_PRINCIPAL_POINT ? "+fix_principal_point" : "",
			flags & CALIB_ZERO_TANGENT_DIST ? "+zero_tangent_dist" : "");
	}
 
	fs << "flags" << flags;
 
	fs << "camera_matrix" << cameraMatrix;
	fs << "distortion_coefficients" << distCoeffs;
 
	fs << "avg_reprojection_error" << totalAvgErr;
 
	return true;
}
 
int main()
{
	float aspectRatio = 1;//  fx/fy,长宽比，应该是board的长宽比
	VideoCapture inputVideo(0);//外置摄像头，自带摄像头请使用0
 
	Ptr<aruco::Dictionary> dictionary =
		aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_50);//创建字典
 
	//创建棋盘对象，参数参考上一篇
	Ptr<aruco::GridBoard> gridboard =
		aruco::GridBoard::create(5, 5, 100, 20, dictionary);
	Ptr<aruco::Board> board = gridboard.staticCast<aruco::Board>();
 
	// 收集信息
	vector< vector< vector< Point2f > > > allCorners;//所有marker的四个角
	vector< vector< int > > allIds;//所有marker的ID
	Size imgSize;
 
	while (inputVideo.grab()) {
		Mat image, imageCopy;
		inputVideo.retrieve(image);
 
		vector< int > ids;
		vector< vector< Point2f > > corners;
 
		// 检测标记
		aruco::detectMarkers(image, dictionary, corners, ids);
 
		// draw results
		image.copyTo(imageCopy);
		if (ids.size() > 0) aruco::drawDetectedMarkers(imageCopy, corners, ids);
 
		putText(imageCopy, "Press 'c' to add current frame. 'ESC' to finish and calibrate",
			Point(10, 20), FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 0, 0), 2);
 
		imshow("out", imageCopy);
		char key = (char)waitKey(30);
		if (key == 27) break;
		if (key == 'c' && ids.size() > 0) {
			cout << "Frame captured" << endl;
			allCorners.push_back(corners);//按下c后，将该帧中所有的标记的角以及id保存,尽量捕捉多一点的图像，20左右
			allIds.push_back(ids);
			imgSize = image.size();
		}
	}
 
	if (allIds.size() < 1) {
		cerr << "Not enough captures for calibration" << endl;
		return 0;
	}
 
	Mat cameraMatrix, distCoeffs;
	vector< Mat > rvecs, tvecs;
	double repError;
 
	if (CALIB_FIX_ASPECT_RATIO) {
		cameraMatrix = Mat::eye(3, 3, CV_64F);
		cameraMatrix.at< double >(0, 0) = aspectRatio;
	}
 
	// 开始处理收集到的信息
	vector< vector< Point2f > > allCornersConcatenated;
	vector< int > allIdsConcatenated;
	vector< int > markerCounterPerFrame;
	markerCounterPerFrame.reserve(allCorners.size());
	for (unsigned int i = 0; i < allCorners.size(); i++) {
		markerCounterPerFrame.push_back((int)allCorners[i].size());
		for (unsigned int j = 0; j < allCorners[i].size(); j++) {
			allCornersConcatenated.push_back(allCorners[i][j]);
			allIdsConcatenated.push_back(allIds[i][j]);
		}
	}
	// 校准摄像头
	repError = aruco::calibrateCameraAruco(allCornersConcatenated, allIdsConcatenated,
		markerCounterPerFrame, board, imgSize, cameraMatrix,
		distCoeffs, rvecs, tvecs, 1);
 
	//保存参数，参数保存在.cpp文件同一目录下
	bool saveOk = saveCameraParams("camera_Params.yml", imgSize, aspectRatio, 1, cameraMatrix,
		distCoeffs, repError);
 
	if (!saveOk) {
		cerr << "Cannot save output file" << endl;
		return 0;
	}
 
	cout << "Rep Error: " << repError << endl;
	cout << "Calibration saved to " << "camera.yml" << endl;
 
	return 0;
}