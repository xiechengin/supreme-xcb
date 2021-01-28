#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>
#include <math.h> 
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgproc/types_c.h"

using namespace cv;
using namespace std;

bool IsQrRate(float rate);
bool AdjustQrPoint(Point* pointSrc, Point* pointDest);
bool IsQrColorRateX(cv::Mat& image, int flag);
bool IsQrColorRate(cv::Mat& image, int flag);
bool IsQrPoint(vector<Point>& contour, Mat& img);
int FindQrPoint(Mat& srcImg, vector<vector<Point>>& qrPoint);

//原理:黑白比例为1:1:3:1:1

int main()
{
	Mat src = imread("/Users/shuike/Desktop/work/svn/droneLanding/resource/B02D001.png", IMREAD_COLOR);
	vector<vector<Point>> qrPoint;
	FindQrPoint(src,qrPoint);
	//二维码倾斜角度
	//Point hor(pointAdjust[0].x + 300, pointAdjust[0].y); //水平线
	//double qrAngle = Angle(pointAdjust[1], hor, pointAdjust[0], clockwise);

	////以二维码左上角点为中心 旋转
	//Mat drawingRotation = Mat::zeros(Size(src.cols, src.rows), CV_8UC3);
	//double rotationAngle = clockwise ? -qrAngle : qrAngle;
	//Mat affine_matrix = getRotationMatrix2D(pointAdjust[0], rotationAngle, 1.0);//求得旋转矩阵
	//warpAffine(src, drawingRotation, affine_matrix, drawingRotation.size());

	return 0;
}

int FindQrPoint(Mat & srcImg, vector<vector<Point>> & qrPoint)  //
 {
	     //彩色图转灰度图
		 Mat src_gray;
	     cvtColor(srcImg, src_gray, CV_BGR2GRAY);
	     namedWindow("src_gray");
	     imshow("src_gray", src_gray);
		
		 //使灰度图象直方图均衡化  
		 equalizeHist(src_gray, src_gray);
		 //二值化
		 Mat threshold_output;
	     threshold(src_gray, threshold_output, 0, 255, THRESH_BINARY | THRESH_OTSU);
	     Mat threshold_output_copy = threshold_output.clone();
	     namedWindow("Threshold_output");
	     imshow("Threshold_output", threshold_output);
	
		 //调用查找轮廓函数
		 //   参数说明
		//	输入图像image必须为一个2值单通道图像
		//	contours参数为检测的轮廓数组，每一个轮廓用一个point类型的vector表示
		//	hiararchy参数和轮廓个数相同，每个轮廓contours[ i ]对应4个hierarchy元素hierarchy[ i ][ 0 ] ~hierarchy[ i ][ 3 ]，
		//		分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，该值设置为负数。
		//	mode表示轮廓的检索模式
		//		CV_RETR_EXTERNAL 表示只检测外轮廓
		//		CV_RETR_LIST 检测的轮廓不建立等级关系
		//		CV_RETR_CCOMP 建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
		//		CV_RETR_TREE 建立一个等级树结构的轮廓。具体参考contours.c这个demo
		//	method为轮廓的近似办法
		//		CV_CHAIN_APPROX_NONE 存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
		//		CV_CHAIN_APPROX_SIMPLE 压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
		//		CV_CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS 使用teh-Chinl chain 近似算法
		//	offset表示代表轮廓点的偏移量，可以设置为任意值。对ROI图像中找出的轮廓，并要在整个图像中进行分析时，这个参数还是很有用的。
	     vector<vector<Point> > contours;//	contours参数为检测的轮廓数组，每一个轮廓用一个point类型的vector表示
	     vector<Vec4i> hierarchy;//	hiararchy参数和轮廓个数相同，每个轮廓contours[ i ]对应4个hierarchy元素hierarchy[ i ][ 0 ] ~hierarchy[ i ][ 3 ]
	     findContours(threshold_output, contours, hierarchy, CV_RETR_TREE, CHAIN_APPROX_NONE, Point(0, 0));
	
		 //通过黑色定位角作为父轮廓，有两个子轮廓的特点，筛选出三个定位角
		 int parentIdx = -1;
	     int ic = 0;
	
		for (int i = 0; i < contours.size(); i++)
		{
			if (hierarchy[i][2] != -1 && ic == 0)
				{
					parentIdx = i;
					ic++;
				}
			else if (hierarchy[i][2] != -1)
				{
					ic++;
				}
			else if (hierarchy[i][2] == -1)
				{
					ic = 0;
					parentIdx = -1;
				}
		
			
			// {
			// bool isQr = IsQrPoint(contours[parentIdx], threshold_output_copy);//
			
			// //保存找到的三个黑色定位角
			// if (isQr)
			// 	qrPoint.push_back(contours[parentIdx]);
			
			// ic = 0;
			// parentIdx = -1;
			// }
		}
	
		return 0;
	 }

bool IsQrPoint(vector<Point>& contour, Mat& img)
{
	//最小大小限定
	RotatedRect rotatedRect = minAreaRect(contour);
	if (rotatedRect.size.height < 10 || rotatedRect.size.width < 10)
		return false;

	//将二维码从整个图上抠出来
	cv::Mat cropImg = CropImage(img, rotatedRect);
	int flag = i++;

	//横向黑白比例1:1:3:1:1
	bool result = IsQrColorRate(cropImg, flag);
	return result;
}

//横向和纵向黑白比例判断
bool IsQrColorRate(cv::Mat& image, int flag)
{
	bool x = IsQrColorRateX(image, flag);
	if (!x)
		return false;
	bool y = IsQrColorRateY(image, flag);
	return y;
}
//横向黑白比例判断
bool IsQrColorRateX(cv::Mat& image, int flag)
{
	int nr = image.rows / 2;
	int nc = image.cols * image.channels();

	vector<int> vValueCount;
	vector<uchar> vColor;
	int count = 0;
	uchar lastColor = 0;

	uchar* data = image.ptr<uchar>(nr);
	for (int i = 0; i < nc; i++)
	{
		vColor.push_back(data[i]);
		uchar color = data[i];
		if (color > 0)
			color = 255;

		if (i == 0)
		{
			lastColor = color;
			count++;
		}
		else
		{
			if (lastColor != color)
			{
				vValueCount.push_back(count);
				count = 0;
			}
			count++;
			lastColor = color;
		}
	}

	if (count != 0)
		vValueCount.push_back(count);

	if (vValueCount.size() < 5)
		return false;

	//横向黑白比例1:1:3:1:1
	int index = -1;
	int maxCount = -1;
	for (int i = 0; i < vValueCount.size(); i++)
	{
		if (i == 0)
		{
			index = i;
			maxCount = vValueCount[i];
		}
		else
		{
			if (vValueCount[i] > maxCount)
			{
				index = i;
				maxCount = vValueCount[i];
			}
		}
	}

	//左边 右边 都有两个值，才行
	if (index < 2)
		return false;
	if ((vValueCount.size() - index) < 3)
		return false;

	//黑白比例1:1:3:1:1
	float rate = ((float)maxCount) / 3.00;

	cout << "flag:" << flag << " ";

	float rate2 = vValueCount[index - 2] / rate;
	cout << rate2 << " ";
	if (!IsQrRate(rate2))
		return false;

	rate2 = vValueCount[index - 1] / rate;
	cout << rate2 << " ";
	if (!IsQrRate(rate2))
		return false;

	rate2 = vValueCount[index + 1] / rate;
	cout << rate2 << " ";
	if (!IsQrRate(rate2))
		return false;

	rate2 = vValueCount[index + 2] / rate;
	cout << rate2 << " ";
	if (!IsQrRate(rate2))
		return false;

	return true;
}
//纵向黑白比例判断 省略
bool IsQrColorRateY(cv::Mat& image, int flag);

bool IsQrRate(float rate)
{
	//大概比例 不能太严格
	return rate > 0.6 && rate < 1.9;
}
 // pointDest存放调整后的三个点，三个点的顺序如下
 // pt0----pt1
 // 
 // pt2
 bool AdjustQrPoint(Point * pointSrc, Point * pointDest)
 {
	     bool clockwise;
	     int index1[3] = { 2,1,0 };
	     int index2[3] = { 0,2,1 };
	     int index3[3] = { 0,1,2 };
	
		     for (int i = 0; i < 3; i++)
		     {
		         int* n = index1;
		         if (i == 0)
			             n = index1;
		         else if (i == 1)
			             n = index2;
		         else
			             n = index3;
		
			     if (angle > 80 && angle < 99)
			         {
			             pointDest[0] = pointSrc[n[2]];
			             if (clockwise)
				             {
				                 pointDest[1] = pointSrc[n[0]];
				                 pointDest[2] = pointSrc[n[1]];
				             }
			             else
				             {
				                 pointDest[1] = pointSrc[n[1]];
				                 pointDest[2] = pointSrc[n[0]];
				             }
			             return true;
			         }
		     }
	     return true;
 }

