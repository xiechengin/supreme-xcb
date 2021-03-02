#ifndef MOTEC_MOTO_DRIVER_H
#define MOTEC_MOTO_DRIVER_H

#include "motor_driver.h"
#include "can_socket.h"

#include <string>
#include <thread>
#include <mutex>
#include <queue>





class MOTECMotorDriver : public MotorDriver
{
public:
    MOTECMotorDriver(int id);

    ~MOTECMotorDriver();

    bool setParams(const std::string& params);  //�������

    int init();                                 //��ʼ��  �� 

    int close();                                //�رա�

    int setEnable(const EnableCmd* cmds, int count);    //ʹ�ܡ�

    int setSpeed(const SpeedCmd* cmds, int count);      //���ٶ�

    int stop(const StopCmd* cmds, int count);           //ֹͣ��

    int getSpeed(SpeedCmd* cmds, int count);            //��ȡ�ٶ�

    int getError(int id);                               //�Ų���󣿣�

    int sendCmd(const std::string& cmd);                //���͵Ĵ���

    int onGetCmdResult(const std::string& cmd);         //����ָ��  

    inline bool isRunable() { return runnable_; }       //�����У���
    void run();
    static void threadRoutine(void* data);              //�߳����̣���
private:

    typedef struct CmdData {
        unsigned char   address;
        unsigned char   cmd;
        unsigned short  funcode;
        unsigned short  data;
        unsigned short  crc;
    } CmdData;

    unsigned short getCRC16(unsigned char* ptr, unsigned char len);
    unsigned short swap_half_16(unsigned short in);
    int PackCmdData(int id, int cmd, short funcode, short data, unsigned char* ret_buf, int max_size);
    int PackSetSpeedCmdData(int id, short rpm, unsigned char* ret_buf, int max_size);
//    std::string MOTECMotorDriver::strToHex(std::string str, std::string separator = "");
private:
    bool                               runnable_;
    CanPort*                     can_port_;
    std::thread*               com_thread_;
    std::mutex                  com_mutex_;
    std::mutex                  cmd_mutex_;
    std::queue<std::string>     cmd_queue_;

    float                       last_left_rpm;
    float                       last_right_rpm;

   

};




















#endif // MOTEC_MOTO_DRIVER_H
