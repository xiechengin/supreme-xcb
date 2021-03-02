#ifndef CAN_SOCKET_H
#define CAN_SOCKET_H


#include <linux/can.h>
#include "can_port.h"

#define MAXFILTER   256


class CanSocket : public CanPort
{
public:
    CanSocket(int id);

    virtual ~CanSocket();


    int SetParam(const std::string& name, const std::string& value);

    int Open(int param);

    int Close(int waitms);


    int AddCanFilter(uint can_id, uint mask);

    int ResetCanFilter();

    int ReadData(uint8_t* data, uint32_t max, int waitms);

    int WriteData(const uint8_t* data, uint32_t len);

    int ReadFrame(CanData* data, int waitms);

    int WriteFrame(const CanData* data);

private:
    int setNonBlocking(int sfd);
    int logCanData(int rw, const CanData* pdata);
private:

    struct can_filter   filter_list_[MAXFILTER];
    int                 filter_count_;
};


#endif // CAN_SOCKET_H
