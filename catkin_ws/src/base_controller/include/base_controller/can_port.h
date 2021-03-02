#ifndef CAN_PORT_H
#define CAN_PORT_H

#include "com_interface.h"


enum CanFrameType {
    CAN_FRAME_STAND,        //标准帧
    CAN_FRAME_EXTERN,       //扩展帧
    CAN_FRAME_REMOTE,       //远程帧
    CAN_FRAME_ERROR         //错误帧
};

extern const char* gCanFrameTypeString[];

typedef struct stCanData {
    uint8_t   type;           //数据帧类型，
    uint    id;             //CAN id
    uint8_t   len;            //数据长度, 最大为8
    uint8_t   data[8];        //数据
}CanData;

class CanPort : public ComInterface
{
public:
    CanPort(int channel);
    virtual ~CanPort();

    virtual int SetParam(const std::string& name, const std::string& value) = 0;

    virtual int Open(int param) = 0;

    virtual int Close(int waitms) = 0;


    virtual int AddCanFilter(uint can_id, uint mask) = 0;

    virtual int ResetCanFilter() = 0;

    virtual int ReadData(uint8_t* data, uint32_t max, int waitms) = 0;

    virtual int WriteData(const uint8_t* data, uint32_t len) = 0;

    virtual int ReadFrame(CanData* frame, int waitms) = 0;

    virtual int WriteFrame(const CanData* frame) = 0;

    inline const std::string& DeviceName() {return dev_name_;}
    inline int  Channel()   {return can_channel_;}
    inline int  Baudrate()  {return baudrate_;}
    inline bool IsBlock()   {return is_block_;}
protected:
    std::string         dev_name_;
    int                 can_channel_;
    int                 baudrate_;
    bool                is_block_;

};


#endif // CAN_PORT_H
