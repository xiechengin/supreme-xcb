'''
brief: 
Version: 
Autor: shuike
Date: 2021-01-09 14:04:34
LastEditors: shuike
LastEditTime: 2021-01-19 20:12:03
FilePath: /droneLanding/python/Tello/ImageCapture.py
'''
from djitellopy import tello

import cv2

me = tello.Tello()

me.connect()

print(me.get_battery())

me.streamon()

while True:

    img = me.get_frame_read().frame

    img = cv2.resize(img, (360, 240))

    cv2.imshow("Image", img)
    cv2.waitKey(1)

