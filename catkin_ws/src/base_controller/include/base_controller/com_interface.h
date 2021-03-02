#ifndef COM_INTERFACE_H
#define COM_INTERFACE_H

#include <list>
#include <string>



typedef enum eInterfaceTypes{
    TYPE_RS232,         //串口
    TYPE_RS485,         //485接口
    TYPE_CAN,           //CAN接口
    TYPE_USB,           //USB接口
    TYPE_ETHERNET,      //以太网接口
}InterfaceTypes;


class ComListener {
public :
    ComListener();
    virtual ~ComListener();

    virtual void OnInterfaceOpened(int fd) = 0;
    virtual void OnInterfaceError(int error, const char* errstr) = 0;
    virtual void OnInterfaceClosed() = 0;
    virtual int OnReadData(const uint8_t* data, uint32_t len) = 0;
    virtual int OnReadTimeout(int timeout) = 0;

};



class ComInterface {
public:
    ComInterface(const char* name, int type);

    virtual ~ComInterface();

    void AddListener(ComListener* listener);

    void RemoveListener(ComListener* listener);

    virtual int SetParam(const std::string& name, const std::string& value) = 0;

    virtual int Open(int param) = 0;

    virtual int Close(int waitms) = 0;


    virtual int WriteData(const uint8_t* data, uint32_t len) = 0;

    virtual int ReadData(uint8_t* data, uint32_t max, int waitms) = 0;

    inline int type() const             {return type_;}
    inline const std::string &name()    {return name_;}
    inline bool isReady() const         {return is_ready_;}
    inline int status() const           {return status_;}
    inline int lastError() const        {return last_error_;}

protected:
    int                                 type_;
    std::string                         name_;
    std::list<ComListener*>             listener_;
    int                                 device_fd_;
    int                                 status_;
    bool                                is_ready_;
    int                                 last_error_;
};


#endif // COM_INTERFACE_H
