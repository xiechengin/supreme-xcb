import KeyPressModule as kp

from time import sleep

kp.init()

me = tello.Tello()

me.connect()

aruco.m_aruco_center[2]

aruco.m_camera_center[2]

print(me.get_battery())

def aruco_x_error():

    return aruco.m_camera_center[0]-aruco.m_aruco_center[0]

def aruco_y_error():

    return aruco.m_camera_center[1]-aruco.m_aruco_center[1]

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

    return [lr, fb, ud, yv]  #-左+右，+前-后，+上-下，-逆时针+顺时针

while True:
    
    vals = getKeyboardInput()

    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    sleep(0.05)

    if aruco_x_error>10
    
        vals = (-50,0,0,0)
    
    if aruco_x_error<-10
    
        vals = (50,0,0,0)










    
    
