#include "base_controller/motec_motor_driver.h"


#include "ros/ros.h"
#include <iostream>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/can.h>
#include <linux/can/raw.h>
#include <string>




bool debug_enable = 0;


////////////////////////////////////////////////////////////////////////////////////

unsigned short MOTECMotorDriver::swap_half_16(unsigned short in)
{
	unsigned short out = 0;
	out = in >> 8 | in << 8;
	return out;
}

unsigned short MOTECMotorDriver::getCRC16(unsigned char* ptr, unsigned char len)
{
	unsigned char i;
	unsigned short crc = 0xFFFF;
	if (len == 0)
	{
		len = 1;
	}
	while (len--)
	{
		crc ^= *ptr;
		for (i = 0; i < 8; i++)
		{
			if (crc & 1)
			{
				crc >>= 1;
				crc ^= 0xA001;
			}
			else
			{
				crc >>= 1;
			}
		}
		ptr++;
	}
	return(crc);
}
int MOTECMotorDriver::PackCmdData(int id, int cmd, short funcode, short data, unsigned char* ret_buf, int max_size)
{
	if (ret_buf == nullptr || max_size < sizeof(CmdData)) {
		return -1;
	}

	CmdData cmd_data;
	cmd_data.address = id;
	cmd_data.cmd = cmd;
	cmd_data.funcode = swap_half_16(funcode);
	cmd_data.data = swap_half_16(data);
	cmd_data.crc = getCRC16((unsigned char*)&cmd_data, sizeof(CmdData) - 2);

	int ret = -1;
	mempcpy(ret_buf, &cmd_data, sizeof(CmdData));
	ret = sizeof(CmdData);
	return ret;
}


int MOTECMotorDriver::PackSetSpeedCmdData(int id, short rpm, unsigned char* ret_buf, int max_size)
{
	
	if (rpm < 0)
	{
		return PackCmdData(id, 0x6f, 0xFFFF, rpm, ret_buf, max_size);
	}
	else
	{
		return PackCmdData(id, 0x6f, 0x0000, rpm, ret_buf, max_size);
	}
	
}


///////////////////////////////////////////////////

MOTECMotorDriver::MOTECMotorDriver(int id)
{
	//com_device_ = new SerialDevice();
	can_port_ = new CanSocket(id);    
	last_left_rpm = 0;
	last_right_rpm = 0;

	runnable_ = true;
	com_thread_ = new std::thread(threadRoutine, this);
}

MOTECMotorDriver::~MOTECMotorDriver()
{
	close();
	delete com_thread_;
	if (can_port_!= nullptr) {
		delete can_port_;
	}
}

/////////////////////////////////////////////////////////////////////////////////////
bool MOTECMotorDriver::setParams(const std::string& params)
{
	return 0;
	//后期改
	//return can_port_->SetParam(params,);
	//return com_device_->setParams(params);   
}

int MOTECMotorDriver::init()
{	
	ROS_INFO_STREAM("Start init driver...");

	int ret =can_port_->Open(1);
	//int ret = com_device_->open();
	if (ret != 0) {
		ROS_INFO_STREAM("CAN OPEN failed!");
		return -1;
	}
	//speedloop 00 96 00 25 00 01 98 0D 
	 unsigned char buf[8] = {0x00,0x96,0x00,0x25,0x00,0x01,0x98,0x0D};
	CanData can_data1;
	CanData can_data2;

	can_data1.type =  CAN_FRAME_STAND;
	can_data2.type =  CAN_FRAME_STAND;
	
	can_data1.id = 0x01;
	can_data2.id = 0x02;
	can_data1.len = 8;
	can_data2.len = 8;
	memcpy(can_data1.data,buf,8);
    memcpy(can_data2.data,buf,8);

	ret = can_port_->WriteFrame(&can_data1);
	ret = can_port_->ReadFrame(&can_data1,10);

	ret = can_port_->WriteFrame(&can_data2);
	ret = can_port_->ReadFrame(&can_data2,10);
	
	if (ret < 0)
	{
		ROS_INFO_STREAM("Driver init failed!");
	}
	
	ROS_INFO_STREAM("Driver init successfully!");
	return 0;
}

int MOTECMotorDriver::close()
{
	runnable_ = false;
	if (com_thread_ != nullptr) {
		if (com_thread_->joinable()) {
			com_thread_->join();
		}
	}
	return can_port_->Close(0);
	//return com_device_->close();
}

int MOTECMotorDriver::setEnable(const EnableCmd* cmds, int count)
{
	if (cmds == nullptr || count <= 0) {
		return -1;
	}
	if (!can_port_->isReady()) {
		return -2;
	}
	CanData can_data1;
	CanData can_data2;
	can_data1.type =  CAN_FRAME_STAND;
	can_data2.type =  CAN_FRAME_STAND;
	can_data1.id = 0x01;
	can_data2.id = 0x02;
	can_data1.len = 8;
	can_data2.len = 8;

	int ret = -1;
	std::string cmd_str;
	if (cmds[0].enable == true) {
		//enable00 15 00 00 00 00 0D D8 
		unsigned char buf[256] = {0x00,0x15, 0x00, 0x00, 0x00, 0x00, 0x0D, 0xD8 ,};
		memcpy(can_data1.data,buf,sizeof(can_data2.data));
        memcpy(can_data2.data,buf,8);

	ret = can_port_->WriteFrame(&can_data1);
	ret = can_port_->ReadFrame(&can_data1,10);

	ret = can_port_->WriteFrame(&can_data2);
	ret = can_port_->ReadFrame(&can_data2,10);
	

		if (ret < 0)
		{
			ROS_INFO_STREAM("Motor enable failed!");
		}
		ROS_INFO_STREAM("Send enable open");
	}
	else {
		unsigned char buf[256] = {0x00,0x16, 0x00, 0x00, 0x00, 0x00, 0x49, 0xD8 ,};
		memcpy(can_data1.data,buf,sizeof(can_data2.data));
        memcpy(can_data2.data,buf,8);

	ret = can_port_->WriteFrame(&can_data1);
	ret = can_port_->ReadFrame(&can_data1,10);

	ret = can_port_->WriteFrame(&can_data2);
	ret = can_port_->ReadFrame(&can_data2,10);

		if (ret < 0)
		{
			ROS_INFO_STREAM("Motor disenable failed!");
		}
		ROS_INFO_STREAM("Send enable close");
	}

	return ret;
} 


int MOTECMotorDriver::stop(const StopCmd* cmds, int count)
{
	if (cmds == nullptr || count <= 0) {
		return -1;
	}
	if (!can_port_->isReady()) {
		return -2;
	}
	ROS_INFO_STREAM("Stop moto driver...");
	return  0;
}



 
int MOTECMotorDriver::setSpeed(const SpeedCmd* cmds, int count)    
{	
	if (cmds == nullptr || count <= 0) {
		return -1;
	}
	if (!can_port_->isReady()) {
		return -2;
	}
	int ret = -1;
	CanData can_data1;
	CanData can_data2;
	can_data1.type =  CAN_FRAME_STAND;
	can_data2.type =  CAN_FRAME_STAND;
	can_data1.id = 0x01;
	can_data2.id = 0x02;
	can_data1.len = 8;
	can_data2.len = 8;

//	std::cout<<"cmds[0].rpm is:"<<cmds[0].rpm<<" cmds[1].rpm is:"<<cmds[1].rpm<<std::endl;
	

	CmdData cmd;
	ret = PackSetSpeedCmdData(cmds[0].id, (short)cmds[0].rpm, (unsigned char*)&cmd, sizeof(cmd));
	memcpy(can_data1.data,&cmd,sizeof(can_data2.data));

	ret = PackSetSpeedCmdData(cmds[1].id, (short)cmds[1].rpm, (unsigned char*)&cmd, sizeof(cmd));
	memcpy(can_data2.data,&cmd,8);
	
	ret = can_port_->WriteFrame(&can_data1);
	ret = can_port_->ReadFrame(&can_data1,10);

	ret = can_port_->WriteFrame(&can_data2);
	ret = can_port_->ReadFrame(&can_data2,10);
	
	ROS_INFO_STREAM("Set moto speed...");

	return 0;
}


int MOTECMotorDriver::getSpeed(SpeedCmd* cmds, int count)
{
//多线程　收和发用不同的线程　避免延迟　
	if (cmds == nullptr || count <= 0) {
		return -1;
	}
	if (!can_port_->isReady()) {
		return -2;
	}
	ROS_INFO_STREAM("Get moto speed...");
	unsigned char cmd_buf1[256] = {0x01, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x15, 0xCF, };	
	unsigned char cmd_buf2[256] = {0x02, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x15, 0xFC, };

	int ret = -1;
	CanData can_data1;
	CanData can_data2;
	can_data1.type =  CAN_FRAME_STAND;
	can_data2.type =  CAN_FRAME_STAND;
	can_data1.id = 0x01;
	can_data2.id = 0x02;
	can_data1.len = 8;
	can_data2.len = 8;
	memcpy(can_data1.data,cmd_buf1,8);
	memcpy(can_data2.data,cmd_buf2,8);

	ret = can_port_->WriteFrame(&can_data1);
	ret = can_port_->ReadFrame(&can_data1,10);

	ret = can_port_->WriteFrame(&can_data2);
	ret = can_port_->ReadFrame(&can_data2,10);

cmds[0].rpm = ((short)(can_data1.data[4]*256) + can_data1.data[5]);
cmds[1].rpm = ((short)(can_data2.data[4]*256) + can_data2.data[5]);
return 0;

}

int MOTECMotorDriver::getError(int id)
{
	return 0;
}

int MOTECMotorDriver::sendCmd(const std::string& cmd)
{
	return 0;
}

int MOTECMotorDriver::onGetCmdResult(const std::string& cmd)
{
	return 0;
}

void MOTECMotorDriver::run()
{
}

void MOTECMotorDriver::threadRoutine(void* data)
{

}

