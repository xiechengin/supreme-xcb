#include "base_controller/can_socket.h"

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>
#include <libgen.h>
#include <signal.h>
#include <limits.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <linux/can.h>
#include <linux/can/raw.h>
#include <fcntl.h>
#include <errno.h>

#define TAG     "CanSocket"

#define LogE(tag,fmt, ...) fprintf(stderr, "[" tag "] " fmt " in %s :%d""\n", ##__VA_ARGS__, __FILE__, __LINE__ )
#define LogI(tag,fmt, ...) fprintf(stdout, "[" tag "] " fmt "\n", ##__VA_ARGS__ )
#define LogD(tag,fmt, ...) fprintf(stdout, "[" tag "] " fmt "\n", ##__VA_ARGS__ )
#define LogW(tag,fmt, ...) fprintf(stdout, "[" tag "] " fmt "\n", ##__VA_ARGS__ )


CanSocket::CanSocket(int id) : CanPort (id)
{
    device_fd_ = -1;
    is_block_ = true;//*********************文件操作，select函数
    baudrate_ = 1000000;
    filter_count_ = 0;
    //dev_name_ = StringUtil::Format("can%d", id);
    char tmp[256] = {0};
    //fprintf(stderr, "[" TAG "] " fmt " in %s :%d""\n", ##__VA_ARGS__, __FILE__, __LINE__ );

    snprintf(tmp, sizeof(tmp), "can%d", id);
    dev_name_  = tmp;
}

CanSocket::~CanSocket()
{
    Close(0);
}

int CanSocket::SetParam(const std::string &name, const std::string &value)
{

    if (name.compare("baudrate") == 0) {
        baudrate_ = atoi(value.c_str());
    } else if (name.compare("block") == 0) {
        is_block_ = atoi(value.c_str());
    } else {
        return -1;
    }
    LogI(TAG, "Set %s = %s ", name.c_str(), value.c_str());
    return 0;
}

int CanSocket::Open(int param)
{
    char cmd[256] = {0};
    struct ifreq  ifr;
    struct sockaddr_can  addr;

    // check can is opend
    snprintf(cmd, sizeof(cmd), "ifconfig %s", dev_name_.c_str());


    if (system(cmd) != 0) {
        LogW(TAG, "CAN interface %s not open yet", dev_name_.c_str());

        snprintf(cmd, sizeof(cmd), "ifconfig %s down", dev_name_.c_str());
        if (system(cmd) < 0) {
            LogE(TAG, "Close CAN interface failed!");
            return -1;
        }

//sudo ********************************权限不够怎么办？
        snprintf(cmd, sizeof(cmd), "ip link set %s up type can bitrate %d",
                 dev_name_.c_str(), baudrate_);
        if (-1 == system(cmd)) {
            LogE(TAG, "Set CAN bus baudrate %d failed!", baudrate_);
            return -2;
        }
    } else {
        LogI(TAG, "CAN interface %s is already opened!", dev_name_.c_str());
    }

    device_fd_ = socket (PF_CAN, SOCK_RAW, CAN_RAW); //创建套接字

    if (device_fd_ < 0) {
        LogE(TAG, "CanSocket Init error: %s", strerror(errno));
        return -3;
    }

    addr.can_family = PF_CAN;
    strncpy(ifr.ifr_name, dev_name_.c_str(), 16);

//指定can0设备
    if ( ioctl (device_fd_, SIOCGIFINDEX, &ifr) ) {
        LogE(TAG, "CanSocket get index error %s", strerror(errno));
        return -4;
    }

//将套接字与can0绑定
    addr.can_ifindex = ifr.ifr_ifindex;
    if (bind ( device_fd_, (struct sockaddr *)&addr, sizeof(addr) ) < 0) {
        LogE(TAG, "Binding socket error: %s", strerror(errno));
        return -5;
    }

    if (!is_block_) {
        if (setNonBlocking (device_fd_) != 0) {
            LogE(TAG, "CanSocket set NonBlocking failed");
            return -6;
        }
    }

    LogI(TAG, "Init CAN socket[%d] baudrate=%d block=%d ok!",
                can_channel_, baudrate_, is_block_);
    is_ready_ = true;
    return 0;
}

int CanSocket::Close(int waitms)
{
    if (device_fd_ > 0) {
        if (-1 == close (device_fd_)) {
            LogE (TAG, "CanSocket Close error: %s", strerror(errno));
            return -1;
        }
        device_fd_ = 0;
        LogI(TAG, "CanSocket closed...");
    }
    is_ready_ = false;

    return 0;
}

int CanSocket::AddCanFilter(uint can_id, uint mask)
{
    bool exist = false;
    for (int i = 0; i < filter_count_; i++) {
        if (filter_list_[i].can_id == can_id) {
            filter_list_[i].can_mask = mask;
            exist = true;
            break;
        }
    }

    if (!exist) {
        if (filter_count_ >= MAXFILTER - 1) {
            LogE(TAG, "CanSocket filter's count is the overflow now!");
            return -2;
        }

        filter_list_[filter_count_].can_id = can_id;
        filter_list_[filter_count_].can_mask = mask;
        filter_count_++;
    }

    if (setsockopt ( device_fd_,
                     SOL_CAN_RAW,
                     CAN_RAW_FILTER,
                     filter_list_,
                     filter_count_ * sizeof(struct can_filter)) != 0) {
        LogE(TAG, "CanSocket set filter error: %s", strerror(errno));
        return -1; //
    }
    LogI(TAG, "CanSocket add filter with canid=%08X mask=%08X OK!",
                can_id, mask);
    return 0;
}

int CanSocket::ResetCanFilter()
{
    memset(filter_list_, 0, sizeof(filter_list_));
    filter_count_ = 0;

    if (setsockopt ( device_fd_, SOL_CAN_RAW, CAN_RAW_FILTER, nullptr, 0) < 0) {
        LogE(TAG, "CanSocket reset filter error: %s", strerror(errno));
        return -1; //
    }
    LogI(TAG, "Clear all CAN filters");
    return 0;
}

int CanSocket::ReadData(uint8_t *data, uint32_t max, int waitms)
{
    int ret = -1;
    if (data == nullptr || max == 0 || max % sizeof(CanData) != 0) {
        return -1;
    }

    int loops = max / sizeof (CanData);
    int readed = 0;
    CanData* can_data = (CanData*)data;
    do {
        ret = ReadFrame(can_data + readed, waitms);
        if (ret > 0) {
            readed += ret;
        } else {
            break;
        }
    }while (--loops);


    return readed;
}


int CanSocket::WriteData(const uint8_t *data, uint32_t len)
{
    int ret = -1;
    if (data == nullptr || len == 0 || len % sizeof(CanData) != 0) {
        return -1;
    }

    int loops = len / sizeof(CanData);
    CanData* can_data = (CanData*)data;

    do {
        ret = WriteFrame(can_data);
        if (ret > 0) {
            can_data += ret;
        } else {
            break;
        }
    }while(--loops);

    return 0;
}

int CanSocket::ReadFrame(CanData *data, int waitms)
{
    if (data == nullptr) {
        return -1;
    }

    int ret = -1;

    struct can_frame  frame;
    memset( &frame, 0, sizeof(struct can_frame) );
    //*******************************************************************
    if (is_block_ && waitms > 0) {
        fd_set canfd_set;
        FD_ZERO(&canfd_set);
        FD_SET(device_fd_, &canfd_set);

        struct timeval tout;
        tout.tv_sec = waitms / 1000;
        tout.tv_usec = (waitms % 1000) * 1000;

        ret = select(device_fd_ + 1, &canfd_set, NULL, NULL, &tout);
        if (ret < 0) {
            LogE(TAG, "CanSocket read select error: %s", strerror(errno));
            if (errno != EINTR && errno != EAGAIN) {
                return -3;
            } else {
                return 0;
            }
        } else if (ret == 0) {
            return 0;
        }

        if (!FD_ISSET(device_fd_, &canfd_set)) {
            return 0;
        }
    }

    ret = read (device_fd_, &frame, sizeof(struct can_frame));

    if (ret < 0) {

        if (errno == EAGAIN || errno == EWOULDBLOCK || EINTR) {
            return 0;
        }

        LogE(TAG, "CanSocket read error: %s", strerror(errno));
        return -4;

    } else if (ret > 0) {
        if (frame.can_id & CAN_EFF_FLAG) {
            data->type = CAN_FRAME_EXTERN;
            data->id = frame.can_id & CAN_EFF_MASK;
        } else if (frame.can_id & CAN_RTR_FLAG){
            data->type = CAN_FRAME_REMOTE;
            data->id = frame.can_id & CAN_ERR_MASK;
        } else if (frame.can_id & CAN_ERR_FLAG) {
            data->type = CAN_FRAME_ERROR;
            data->id = frame.can_id & CAN_ERR_MASK;
        } else {
            data->id = CAN_FRAME_STAND;
            data->id = frame.can_id & CAN_SFF_MASK;
        }

        data->len = frame.can_dlc;

        memcpy(data->data, frame.data, frame.can_dlc);

        logCanData(0, data);

        return sizeof(CanData);
    }

    return 0;
}

int CanSocket::WriteFrame(const CanData *data)
{
    if (data == nullptr) {
        return -1;
    }
    int ret = -1;
    struct can_frame frame;
    memset ( &frame, 0, sizeof(struct can_frame));

    frame.can_id = data->id;
    switch (data->type) {
        case CAN_FRAME_STAND:
            frame.can_id &= CAN_SFF_MASK;
            break;
        case CAN_FRAME_EXTERN:
            frame.can_id &= CAN_EFF_MASK;
            frame.can_id |= CAN_EFF_FLAG; //
            break;
        case CAN_FRAME_REMOTE:
            frame.can_dlc &= CAN_ERR_MASK;
            frame.can_id |= CAN_RTR_FLAG;
            break;
        case CAN_FRAME_ERROR:
            frame.can_id &= CAN_ERR_MASK;
            frame.can_id |= CAN_ERR_FLAG;
            break;
    }
    frame.can_dlc = data->len;
    memcpy(frame.data, data->data, data->len);

    ret = write(device_fd_, &frame, sizeof(frame));
    if ( ret != sizeof(frame)) {
        LogE(TAG, "CanSocket Write data error: %s", strerror(errno));
        return -2;
    }
    logCanData(1, data);

    return sizeof(CanData);
}


int CanSocket::setNonBlocking(int sfd)
{
    int  flags = 1;
    int  res;


    flags = fcntl(sfd, F_GETFL, 0);

    if (flags == -1) {
        LogE(TAG, "Get CAN socket flag failed! %s", strerror(errno));
        return -1;
    }

    flags |= O_NONBLOCK;
    res    = fcntl (sfd, F_SETFL, flags);

    if (res == -1){
        LogE(TAG, "Set CAN socket nonblock failed! %s", strerror(errno));
        return -2;
    }

    is_block_ = false;
    LogI(TAG, "Set CAN socket noblock ok!");
    return 0;
}

int CanSocket::logCanData(int rw, const CanData* pdata)
{
    char dstr[64] = {0};
    for (int i = 0, l = 0; i < pdata->len; i++) {
        l += snprintf(dstr + l, sizeof(dstr) - l, "%02X ", pdata->data[i]);
    }
    LogD(TAG, "%s [%s] CAN DATA[%d]: %s",
                rw == 0 ? "=====> Read" : ">>>>>> Sent",
                gCanFrameTypeString[pdata->type],
                pdata->len,
                dstr);
    return 0;
}



