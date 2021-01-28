 # **实体小车配置指南**

- 驱动安装

- 项目下载编译

## 驱动安装

### realsense 驱动安装

第一步：添加密钥

```
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
```
第二步：添加源
```
sudo add-apt-repository "deb http://realsense-hw-public.s3.amazonaws.com/Debian/apt-repo bionic main" -u
```
第三部：安装sdk
```
sudo apt-get install librealsense2-dkms  
sudo apt-get install librealsense2-utils
```
第四部：测试是否安装成功， 插入t265相机，运行如下命令

```
realsense-viewer
```

## 项目下载编译

第一步：下载项目

```
git clone https://gitee.com/bingobinlw/volans
```

或更新已有仓库

```
git pull
```

第二步：更新子模块

```
cd volans
git submodule update --init --recursive
```

第三步：编译

```
cd volans
catkin_make
```

第四步：添加环境路径

```
cd volans
source source_environment.sh
```

第五步：运行demo测试是否成功

```
roslaunch lepus t265_position_to_mavros.launch
```

查看t265是否运行正常，mavros是否与飞控连接正常。