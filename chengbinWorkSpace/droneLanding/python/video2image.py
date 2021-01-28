'''
brief: 
Version: 
Autor: shuike
Date: 2021-01-18 11:39:21
LastEditors: shuike
LastEditTime: 2021-01-18 17:48:46
FilePath: /droneLanding/python/video2image.py
'''
import cv2

imagePath = "/Users/shuike/Desktop/work/svn/droneLanding/python/Tello/imageYu2/"
cap = cv2.VideoCapture('/Users/shuike/Desktop/work/svn/droneLanding/video/DJI_0006.MP4')

index =0
while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('s'):
        index = index + 1;
        cv2.imwrite(imagePath+str(index) + ".jpg",frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()