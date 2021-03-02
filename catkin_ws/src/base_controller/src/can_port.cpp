
#include "base_controller/can_port.h"


const char* gCanFrameTypeString[] = {
    "STAND",
    "EXTERN",
    "REMOTE",
    "ERROR"
};


CanPort::CanPort(int channel) : ComInterface ("CanPort", TYPE_CAN)
{
    can_channel_ = channel;
    is_block_ = true;
    baudrate_ = 500000;

}

CanPort::~CanPort()
{

}



