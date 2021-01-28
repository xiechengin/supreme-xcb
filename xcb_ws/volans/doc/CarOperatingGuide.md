 # **实体小车使用指南**

- 准备
- 运行demo

## 准备

第一步：安装ssh

远程端电脑以及本地电脑（小车上面的板载计算机）都要安装好''**ssh**''

```
sudo apt-get install ssh
```

第二步：远程端电脑以及本地电脑连接wifi数传上的wifi，名字是''**lepus-uav20xxx**''，密码是"lepus20xxx"，其中xxx是小车的编号，最好是小车上的板载计算机先连接wifi，使用“**ifconfig**”终端命令查看ip，确保小车上的板载计算机被分配的ip为"**192.168.10.100**"。测试ssh，在远程端电脑终端上输入

```
ssh lepus@192.168.10.100
```

密码是：**lepus**

如果一切顺利将会进入板载计算机的终端。

第三步：配置ros

1.远程端电脑配置：在终端中打开**.bashrc**

```
gedit ~/.bashrc
```

在最后添加

```
export ROS_MASTER_URI=http://192.168.10.100:11311
export ROS_IP=192.168.10.100
```

2.本地电脑配置：在终端中打开**.bashrc**

```
gedit ~/.bashrc
```

在最后添加

```
export ROS_MASTER_URI=http://192.168.10.100:11311
export ROS_IP=192.168.10.100
```

## 运行demo

第一步：用ssh连接板载计算机

在远程端电脑终端里输入：

```
ssh lepus@192.168.10.100
```

密码是：**lepus**

第二步：运行t265_to_mavros demo

在已打开的终端中运行板载计算机的launch文件

```
lepusv@lepus:~$ roslaunch lepus t265_position_to_mavros.launch 
```

**ctrl+shift+t**打开新的终端，运行

```
rostopic list
```

即可在远程端电脑中查看板载计算机中的topic的消息。