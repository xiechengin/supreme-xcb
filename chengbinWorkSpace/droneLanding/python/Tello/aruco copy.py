'''
brief: 
Version: 
Autor: shuike
Date: 2021-01-20 11:01:17
LastEditors: shuike
LastEditTime: 2021-01-20 13:52:44
FilePath: /droneLanding/python/Tello/aruco.py

pip install opencv-python
pip install opencv-contrib-python
'''


import numpy as np
import time
import cv2
import cv2.aruco as aruco
import math


from djitellopy.tello import Tello
import cv2
import pygame
import numpy as np
import time

##############################################################################################################################
#with np.load('webcam_calibration_output.npz') as X:
#    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]

#mtx =
#2946.48    0    1980.53
#0    2945.41    1129.25
#0    0    1

mtx = np.array([[ 1.3658672670450690e+03, 0.,                     5.6223649023204223e+02],
               [ 0.0,                     1.3418448535820166e+03, 2.6018062192801813e+02], 
               [ 0.,                     0.,                     1. ]])
#我的手机拍棋盘的时候图片大小是 4000 x 2250
#ip摄像头拍视频的时候设置的是 1920 x 1080，长宽比是一样的，
#ip摄像头设置分辨率的时候注意一下

dist = np.array( [ -3.2683537981903155e-02, 5.0861274015825053e-01,
                  -1.5535713101176836e-02, -1.1522835531598139e-02,
                  -2.8599010633021353e+00 ] )

video = "/Users/shuike/Downloads/IMG_8427.mp4"   # 手机ip摄像头
# 根据ip摄像头在你手机上生成的ip地址更改，右上角可修改图像分辨率

cap = cv2.VideoCapture(video)


font = cv2.FONT_HERSHEY_SIMPLEX #font for displaying text (below)

actual_marker_l = 0.176; #this should be in meters 二维码点长(打印A4)

#num = 0
while True:
    ret, frame = cap.read()
    # operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_50)
    parameters =  aruco.DetectorParameters_create()

    '''
    detectMarkers(...)
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
    '''

    #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,
                                                          aruco_dict,
                                                          parameters=parameters)

#    if ids != None:
    if ids is not None:

        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, actual_marker_l, mtx, dist)
        # Estimate pose of each marker and return the values rvet and tvec---different
        # from camera coeficcients
        (rvec-tvec).any() # get rid of that nasty numpy value array error

#        aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.1) #Draw Axis
#        aruco.drawDetectedMarkers(frame, corners) #Draw A square around the markers

        for i in range(rvec.shape[0]):
            aruco.drawAxis(frame, mtx, dist, rvec[i, :, :], tvec[i, :, :], actual_marker_l)
            aruco.drawDetectedMarkers(frame, corners)

            ##计算
            ###### 角度估计 #####
            #print(rvec)
            #考虑Z轴（蓝色）的角度
            deg=rvec[0][0][2]/math.pi*180
            #deg=rvec[0][0][2]/math.pi*180*90/104
            # 旋转矩阵到欧拉角
            R=np.zeros((3,3),dtype=np.float64)
            cv2.Rodrigues(rvec,R)
            sy=math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
            singular=sy< 1e-6
            if not singular:#偏航，俯仰，滚动
                x = math.atan2(R[2, 1], R[2, 2])
                y = math.atan2(-R[2, 0], sy)
                z = math.atan2(R[1, 0], R[0, 0])
            else:
                x = math.atan2(-R[1, 2], R[1, 1])
                y = math.atan2(-R[2, 0], sy)
                z = 0
            

            # 偏航，俯仰，滚动换成角度
            rx = x * 180.0 / 3.141592653589793
            ry = y * 180.0 / 3.141592653589793
            rz = z * 180.0 / 3.141592653589793

            cv2.putText(frame,'deg_z:'+str(ry)+str('deg'),(0, 140), font, 1, (0, 255, 0), 2,
                    cv2.LINE_AA)
            print("偏航，俯仰，滚动",rx,ry,rz)

            #世界坐标系x,y,z
            print("#世界坐标系x,y,z",tvec[0][0][0],tvec[0][0][1],tvec[0][0][2])

            ###### 距离估计 #####
            # distance = ((tvec[0][0][2] + 0.02) * 0.0254) * 100  # 单位是米
            # #distance = (tvec[0][0][2]) * 100  # 单位是米


            # # 显示距离
            # cv2.putText(frame, 'distance:' + str(round(distance, 4)) + str('m'), (0, 110), font, 1, (0, 255, 0), 2,
            #         cv2.LINE_AA)


        ###### DRAW ID #####
        cv2.putText(frame, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

        ###### ######


    else:
        ##### DRAW "NO IDS" #####
        cv2.putText(frame, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)

    if key == 27:         # 按esc键退出
        print('esc break...')
        cap.release()
        cv2.destroyAllWindows()
        break

#     if key == ord(' '):   # 按空格键保存
# #        num = num + 1
# #        filename = "frames_%s.jpg" % num  # 保存一张图像
#         # filename = str(time.time())[:10] + ".jpg"
#         # cv2.imwrite(filename, frame)

##########################################################################################################################################################




########################################################################################################################################################################
# Speed of the drone
S = 60
# Frames per second of the pygame window display
FPS = 25


class FrontEnd(object):
    """ Maintains the Tello display and moves it through the keyboard keys.
        Press escape key to quit.
        The controls are:
            - T: Takeoff
            - L: Land
            - Arrow keys: Forward, backward, left and right.
            - A and D: Counter clockwise and clockwise rotations
            - W and S: Up and down.
    """

    def __init__(self):
        # Init pygame
        pygame.init()

        # Creat pygame window
        pygame.display.set_caption("Tello video stream")
        self.screen = pygame.display.set_mode([960, 720])

        # Init Tello object that interacts with the Tello drone
        self.tello = Tello()
        # Drone velocities between -100~100
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 10

        self.send_rc_control = False

        # create update timer
        pygame.time.set_timer(pygame.USEREVENT + 1, 50)

    def run(self):

        if not self.tello.connect():
            print("Tello not connected")
            return

        if not self.tello.set_speed(self.speed):
            print("Not set speed to lowest possible")
            return

        # In case streaming is on. This happens when we quit this program without the escape key.
        if not self.tello.streamoff():
            print("Could not stop video stream")
            return

        if not self.tello.streamon():
            print("Could not start video stream")
            return

        frame_read = self.tello.get_frame_read()

        should_stop = False
        while not should_stop:

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.update()
                elif event.type == pygame.QUIT:
                    should_stop = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        should_stop = True
                    else:
                        self.keydown(event.key)
                elif event.type == pygame.KEYUP:
                    self.keyup(event.key)

            if frame_read.stopped:
                frame_read.stop()
                break

            self.screen.fill([0, 0, 0])
            frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = np.flipud(frame)
            frame = pygame.surfarray.make_surface(frame)

            #这里做图像识别和处理
            
            
            self.screen.blit(frame, (0, 0))
            pygame.display.update()

            time.sleep(1 / FPS)

        # Call it always before finishing. To deallocate resources.
        self.tello.end()

    def keydown(self, key):
        """ Update velocities based on key pressed
        Arguments:
            key: pygame key
        """
        if key == pygame.K_UP:  # set forward velocity
            self.for_back_velocity = S
        elif key == pygame.K_DOWN:  # set backward velocity
            self.for_back_velocity = -S
        elif key == pygame.K_LEFT:  # set left velocity
            self.left_right_velocity = -S
        elif key == pygame.K_RIGHT:  # set right velocity
            self.left_right_velocity = S
        elif key == pygame.K_w:  # set up velocity
            self.up_down_velocity = S
        elif key == pygame.K_s:  # set down velocity
            self.up_down_velocity = -S
        elif key == pygame.K_a:  # set yaw counter clockwise velocity
            self.yaw_velocity = -S
        elif key == pygame.K_d:  # set yaw clockwise velocity
            self.yaw_velocity = S

    def keyup(self, key):
        """ Update velocities based on key released
        Arguments:
            key: pygame key
        """
        if key == pygame.K_UP or key == pygame.K_DOWN:  # set zero forward/backward velocity
            self.for_back_velocity = 0
        elif key == pygame.K_LEFT or key == pygame.K_RIGHT:  # set zero left/right velocity
            self.left_right_velocity = 0
        elif key == pygame.K_w or key == pygame.K_s:  # set zero up/down velocity
            self.up_down_velocity = 0
        elif key == pygame.K_a or key == pygame.K_d:  # set zero yaw velocity
            self.yaw_velocity = 0
        elif key == pygame.K_t:  # takeoff
            self.tello.takeoff()
            self.send_rc_control = True
        elif key == pygame.K_l:  # land
            self.tello.land()
            self.send_rc_control = False

    def update(self):
        """ Update routine. Send velocities to Tello."""
        if self.send_rc_control:
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity, self.up_down_velocity,
                                       self.yaw_velocity)


def main():
    frontend = FrontEnd()

    # run frontend
    frontend.run()

##############################################################################################################################
