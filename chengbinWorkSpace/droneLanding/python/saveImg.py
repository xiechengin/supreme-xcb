'''
brief: 
Version: 
Autor: shuike
Date: 2020-12-31 15:47:59
LastEditors: shuike
LastEditTime: 2020-12-31 15:56:25
FilePath: /droneLanding/python/saveImg.py
'''
import cv2
capture = cv2.VideoCapture(0)
index = 19;
while True:
    ret, frame = capture.read()
    # frame = cv2.flip(frame,1)   #镜像操作
    cv2.imshow("video", frame)
    key = cv2.waitKey(50)
    #print(key)
    if key == ord('s'):
        index = index + 1;
        cv2.imwrite("/Users/shuike/Desktop/work/svn/droneLanding/python/chessboardimg"+str(index)+".png",frame)
    if key  == ord('q'):  #判断是哪一个键按下
        break
cv2.destroyAllWindows()