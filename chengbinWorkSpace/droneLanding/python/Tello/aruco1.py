'''
brief: 
Version: 
Autor: shuike
Date: 2021-01-20 11:01:17
LastEditors: shuike
LastEditTime: 2021-01-21 20:28:15
FilePath: /droneLanding/python/Tello/aruco1.py

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

import threading


##############################################################################################################################

class arucoProcessThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

        self.video = "/Users/shuike/Downloads/IMG_8427.mp4"   # 手机ip摄像头
        # 根据ip摄像头在你手机上生成的ip地址更改，右上角可修改图像分辨率
        self.cap = cv2.VideoCapture(self.video)

        self.mtx = np.array([[ 1.3658672670450690e+03, 0.,                     5.6223649023204223e+02],
                             [ 0.0,                     1.3418448535820166e+03, 2.6018062192801813e+02], 
                             [ 0.,                     0.,                     1. ]])
            #我的手机拍棋盘的时候图片大小是 4000 x 2250
            #ip摄像头拍视频的时候设置的是 1920 x 1080，长宽比是一样的，
            #ip摄像头设置分辨率的时候注意一下

        self.dist = np.array( [ -3.2683537981903155e-02, 5.0861274015825053e-01,
                               -1.5535713101176836e-02, -1.1522835531598139e-02,
                               -2.8599010633021353e+00 ] )

        self.actual_marker_l = 0.176; #this should be in meters 二维码点长(打印A4)
        
        self.m_aruco_x = 0.0
        self.m_aruco_y = 0.0
        self.m_aruco_z = 0.0
        self.m_aruco_q = 0.0
        self.m_aruco_rx = 0.0
        self.m_aruco_ry = 0.0
        self.m_aruco_rz = 0.0

        self.m_frame_center_x = 0
        self.m_frame_center_y = 0
        self.m_arcuo_center_x = 0
        self.m_arcuo_center_y = 0

        self.m_arcuo2frame_center_distance = 0
        
    # 线程运行函数
    def run(self):
        while(True):
            print('I am {0}'.format(self.num))
            ret, frame = self.cap.read()                        #读取帧
            result = self.process(frame);
            cv2.imshow('frame',result)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #灰度化展示
            # cv2.imshow('frame',result)
            if cv2.waitKey(1) & 0xFF == ord('q'):          #按‘q’退出
                break
    def getLength(self,point_A,point_B):
        sub_x=point_A[0] - point_B[0]
        sub_y=point_A[1] - point_B[1]
        #用math.sqrt（）求平方根
        return math.sqrt((sub_x**2)+(sub_y**2))
    
    def checkPoint(self,frame_h,frame_w,in_point):
        x = in_point[0]
        y = in_point[1]
        if 0< x and x < frame_w and 0 < y and y < frame_h:
            return in_point
        else:
            return (0,0)

    def process(self,frame):
        '''
        brief: 
        param {*}
        return {frame,偏航，俯仰，滚动，世界坐标系x,y,z,[]}
        author: shuike
        '''
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

            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, self.actual_marker_l, self.mtx, self.dist)
            # Estimate pose of each marker and return the values rvet and tvec---different
            # from camera coeficcients
            (rvec-tvec).any() # get rid of that nasty numpy value array error

            #        aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.1) #Draw Axis
            #        aruco.drawDetectedMarkers(frame, corners) #Draw A square around the markers

            for i in range(rvec.shape[0]):
                # aruco.drawAxis(frame, self.mtx, self.dist, rvec[i, :, :], tvec[i, :, :], self.actual_marker_l)
                aruco.drawDetectedMarkers(frame, corners)

                ##计算
                m = self.actual_marker_l / 2
                pts = np.float32([[-m,m,0],[m,m,0],[-m,-m,0],[-m,m,m]])
                pt_dict = {}
                imgpts, _ = cv2.projectPoints(pts, rvec, tvec, self.mtx, self.dist)
                for i in range(len(pts)):
                     pt_dict[tuple(pts[i])] = tuple(imgpts[i].ravel())
                
                src = pt_dict[tuple(pts[0])];   #原点
                dst1 = pt_dict[tuple(pts[1])];  #x
                dst2 = pt_dict[tuple(pts[2])];  #y
                dst3 = pt_dict[tuple(pts[3])];  #z
                
                print(dst1)
                print(dst2)
                print(dst3)

                #中心点 
                centor_x = int((dst1[0] + dst2[0])/2)
                centor_y = int((dst1[1] + dst2[1])/2)
                self.m_arcuo_center_x = centor_x
                self.m_arcuo_center_y = centor_y

                print("centor_x_y:[{0},{0}]",centor_x,centor_y)


                frame = cv2.circle(frame, (centor_x, centor_y), 5, (255, 0, 0), 1, 8, 0) # 圆心其实就是一个半径很小的圆

                h,w,_= frame.shape
                frame = cv2.line(frame,self.checkPoint(h,w,src), self.checkPoint(h,w,dst1), (0,255,0), 4)
                frame = cv2.line(frame, self.checkPoint(h,w,src), self.checkPoint(h,w,dst2), (255,0,0), 4)
                frame = cv2.line(frame, self.checkPoint(h,w,src), self.checkPoint(h,w,dst3), (0,0,255), 4)
                
                # axis = np.float32([[self.actual_marker_l,0,0], [0,self.actual_marker_l,0], [0,0,-self.actual_marker_l]]).reshape(-1,3)
                # imgpts, jac = cv2.projectPoints(axis, rvec, tvec, self.mtx, self.dist)
                # print(imgpts)
                ###### 角度估计 #####
                #print(rvec)
                #考虑Z轴（蓝色）的角度
                deg=rvec[0][0][2]/math.pi*180
                #deg=rvec[0][0][2]/math.pi*180*90/104
                # 旋转矩阵到欧拉角
                R=np.zeros((3,3),dtype=np.float64) #a rotation matrix
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

                cv2.putText(frame,'deg_z:'+str(ry)+str('deg'),(0, 140), cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 255, 0), 2,
                    cv2.LINE_AA)
                print("偏航，俯仰，滚动",rx,ry,rz)
                self.m_aruco_rx = rx
                self.m_aruco_ry = ry
                self.m_aruco_rz = rz


                #世界坐标系x,y,z
                print("#世界坐标系x,y,z",tvec[0][0][0],tvec[0][0][1],tvec[0][0][2])
                self.m_aruco_x = tvec[0][0][0]
                self.m_aruco_y = tvec[0][0][1]
                self.m_aruco_z = tvec[0][0][2]


                ###### 距离估计 #####
                # distance = ((tvec[0][0][2] + 0.02) * 0.0254) * 100  # 单位是米
                # #distance = (tvec[0][0][2]) * 100  # 单位是米


                # # 显示距离
                # cv2.putText(frame, 'distance:' + str(round(distance, 4)) + str('m'), (0, 110), font, 1, (0, 255, 0), 2,
                #         cv2.LINE_AA)

                h,w,_= frame.shape
                self.m_frame_center_x = int(w/2)
                self.m_frame_center_y = int(h/2)
                print("图像中心点x,y:",self.m_frame_center_x,self.m_frame_center_y)
                print(frame.shape)
                cv2.line(frame,(0,int(h/2)),(w,int(h/2)),(255,0,0),2) 
                cv2.line(frame,(int(w/2),0),(int(w/2),h),(255,0,0),2) 

                #像素距离
                self.m_arcuo2frame_center_distance = self.getLength((self.m_frame_center_x,self.m_frame_center_y),(self.m_arcuo_center_x,self.m_arcuo_center_y))
                print("m_arcuo2frame_center_distance: {0}",self.m_arcuo2frame_center_distance)
                ###### DRAW ID #####
                cv2.putText(frame, "Id: " + str(ids), (0,64), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,255,0),2,cv2.LINE_AA)

                ###### ######
            else:
                ##### DRAW "NO IDS" #####
                cv2.putText(frame, "No Ids", (0,64), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,255,0),2,cv2.LINE_AA)
        return frame


##########################################################################################################################################################


########################################################################################################################################################################
def getKeyboardInput():
    
    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 50

    if kp.getKey("LEFT"): lr = -speed

    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed

    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"):ud = speed

    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"):yv = -speed

    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): me.land(); sleep(3)

    if kp.getKey("u"): me.takeoff(); sleep(3)
    
    if kp.getKey("e"): me.takeoff()


    return [lr, fb, ud, yv]
########################################################################################################################################################################



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

        self.send_rc_control = True

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
            frame = arucoProcess(frame)
            # cv2.imshow("frame_read.frame",frame_read.frame)
            
            #按键部分
            # vals = getKeyboardInput()
            # print(self.tello.get_battery())
            # self.tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

            frame = np.rot90(frame)
            frame = np.flipud(frame)
            frame = pygame.surfarray.make_surface(frame)

            #监听 让另一个线程去做事情

            # #这里做图像识别和处理
            # frame =  arucoProcess(frame)

            print("shuike")
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
    # frontend = FrontEnd()

    video = "/Users/shuike/Downloads/IMG_8427.mp4" 
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    t2 = arucoProcessThread(2)
    while True:
        # 逐帧捕获
        ret, frame = cap.read()
        # 如果正确读取帧，ret为True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # 我们在框架上的操作到这里
        frame = t2.process(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 显示结果帧e
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break    
    

if __name__ == '__main__':
    # main()
    t1 = arucoProcessThread(1);
    t1.start();
    main();

    # while(True):
    #     print("INFO:m_aruco_x=={0}",t1.m_aruco_x)
    #     print("INFO:m_aruco_y=={0}",t1.m_aruco_y)
    #     print("INFO:m_aruco_z=={0}",t1.m_aruco_z)

    #     print("INFO:m_aruco_rx=={0}",t1.m_aruco_rx)
    #     print("INFO:m_aruco_ry=={0}",t1.m_aruco_ry)
    #     print("INFO:m_aruco_rz=={0}",t1.m_aruco_rz)

    #     print("INFO:m_frame_center_x=={0}",t1.m_frame_center_x)
    #     print("INFO:m_frame_center_y=={0}",t1.m_frame_center_y)
    #     print("INFO:m_arcuo_center_x=={0}",t1.m_arcuo_center_x)
    #     print("INFO:m_arcuo_center_y=={0}",t1.m_arcuo_center_y)

    #     print("INFO:m_arcuo2frame_center_distance=={0}",t1.m_arcuo2frame_center_distance)


##############################################################################################################################
