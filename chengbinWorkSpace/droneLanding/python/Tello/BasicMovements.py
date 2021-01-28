'''
brief: 
Version: 
Autor: shuike
Date: 2021-01-09 14:03:51
LastEditors: shuike
LastEditTime: 2021-01-12 18:56:16
FilePath: /droneLanding/python/Tello/BasicMovements.py
pip install djitellopy
pip install pygame
'''


from djitellopy import tello

from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()

me.send_rc_control(0, 50, 0, 0)

sleep(2)

me.send_rc_control(0, 0, 0, 30)

sleep(2)

me.send_rc_control(0, 0, 0, 0)

me.land()