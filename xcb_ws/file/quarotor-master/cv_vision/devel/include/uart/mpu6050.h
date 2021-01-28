// Generated by gencpp from file uart/mpu6050.msg
// DO NOT EDIT!


#ifndef UART_MESSAGE_MPU6050_H
#define UART_MESSAGE_MPU6050_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace uart
{
template <class ContainerAllocator>
struct mpu6050_
{
  typedef mpu6050_<ContainerAllocator> Type;

  mpu6050_()
    : ax(0)
    , ay(0)
    , az(0)
    , gx(0)
    , gy(0)
    , gz(0)  {
    }
  mpu6050_(const ContainerAllocator& _alloc)
    : ax(0)
    , ay(0)
    , az(0)
    , gx(0)
    , gy(0)
    , gz(0)  {
  (void)_alloc;
    }



   typedef int16_t _ax_type;
  _ax_type ax;

   typedef int16_t _ay_type;
  _ay_type ay;

   typedef int16_t _az_type;
  _az_type az;

   typedef int16_t _gx_type;
  _gx_type gx;

   typedef int16_t _gy_type;
  _gy_type gy;

   typedef int16_t _gz_type;
  _gz_type gz;




  typedef boost::shared_ptr< ::uart::mpu6050_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::uart::mpu6050_<ContainerAllocator> const> ConstPtr;

}; // struct mpu6050_

typedef ::uart::mpu6050_<std::allocator<void> > mpu6050;

typedef boost::shared_ptr< ::uart::mpu6050 > mpu6050Ptr;
typedef boost::shared_ptr< ::uart::mpu6050 const> mpu6050ConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::uart::mpu6050_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::uart::mpu6050_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace uart

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'uart': ['/home/odroid/cv_vision/src/uart/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::uart::mpu6050_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::uart::mpu6050_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::uart::mpu6050_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::uart::mpu6050_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uart::mpu6050_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::uart::mpu6050_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::uart::mpu6050_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ee542a682aee2ad96063f7f4b66160ba";
  }

  static const char* value(const ::uart::mpu6050_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xee542a682aee2ad9ULL;
  static const uint64_t static_value2 = 0x6063f7f4b66160baULL;
};

template<class ContainerAllocator>
struct DataType< ::uart::mpu6050_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uart/mpu6050";
  }

  static const char* value(const ::uart::mpu6050_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::uart::mpu6050_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 ax\n\
int16 ay\n\
int16 az\n\
int16 gx\n\
int16 gy\n\
int16 gz\n\
";
  }

  static const char* value(const ::uart::mpu6050_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::uart::mpu6050_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ax);
      stream.next(m.ay);
      stream.next(m.az);
      stream.next(m.gx);
      stream.next(m.gy);
      stream.next(m.gz);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct mpu6050_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::uart::mpu6050_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::uart::mpu6050_<ContainerAllocator>& v)
  {
    s << indent << "ax: ";
    Printer<int16_t>::stream(s, indent + "  ", v.ax);
    s << indent << "ay: ";
    Printer<int16_t>::stream(s, indent + "  ", v.ay);
    s << indent << "az: ";
    Printer<int16_t>::stream(s, indent + "  ", v.az);
    s << indent << "gx: ";
    Printer<int16_t>::stream(s, indent + "  ", v.gx);
    s << indent << "gy: ";
    Printer<int16_t>::stream(s, indent + "  ", v.gy);
    s << indent << "gz: ";
    Printer<int16_t>::stream(s, indent + "  ", v.gz);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UART_MESSAGE_MPU6050_H
