/**
  ******************************************************************************
  * @file    mode_set.h
  * @author  zcd
  * @version V0.0.1
  * @date    2016-6-25
  * @brief   控制系统的工作模式。
  * 
  ******************************************************************************
  * @verbatim
  * 1.模式包括两种：①手动控制；②自动控制；
  *     系统通过采集遥控器三段开关的位置，来选择不同的控制模式。
  *         三段开关输出状态与模式对照为: 低电平-手动控制模式；高电平-自动控制模式

  * 2.系统使用 CD4053 选择最终传送到飞行器端的数据，选择时通道与控制项的对应关系如下：
  *   PITCH     <---->  CD4053_SWITCH_B
  *   ROLL      <---->  CD4053_SWITCH_C
  *   THROTTLE  <---->  CD4053_SWITCH_A
  *
  * 3. CD4053引脚为高电平时，选择输出x，对应选中手动信号输出；
  *  反之，CD4053引脚为低电平时，选择输出y，对应选中自动控制信号输出。
  *
  *
  * 4.依照模式设定，配置硬件规则如下：
  *  (1)全手动控制模式，利用遥控器摇杆进行控制
  *     油门手动控制 
  *     俯仰手动控制 
  *     横滚手动控制
  *  (2)方向角控制模式，利用遥控器摇杆手动控制油门，根据传感器自动控制方向
  *     油门手动控制 
  *     俯仰自动控制 
  *     横滚自动控制 
  *  (3)方向角控制模式，利用遥控器摇杆手动控制方向，根据传感器自动控制油门
  *     油门自动控制 
  *     俯仰手动控制 
  *     横滚手动控制 
  *  (4)全自动控制模式，根据传感器值对油门、俯仰、偏航进行全面控制
  *     油门自动控制 
  *     俯仰自动控制 
  *     横滚自动控制 
  ******************************************************************************
  *
  ******************************************************************************
  */ 
  
#ifndef  __MODE_SET_H__
#define  __MODE_SET_H__

#include "cmsis_os.h"
#include "stm32f1xx_hal.h"
#include "data_typedef.h"
#include "bsp.h"
#include "data_out.h"



/**********************************宏定义*********************************************/
/**
  * @brief  定义控制模式
  */
typedef enum 
{
	CONTROL_MODE_MANUL = 0,           /*!< (1)全手动控制模式，利用遥控器摇杆进行控制 */
	CONTROL_MODE_AUTO_PITCH_ROLL ,    /*!< (2)方向角控制模式，利用遥控器摇杆手动控制油门，根据传感器自动控制方向 */
	CONTROL_MODE_AUTO_THROTTLE ,      /*!< (3)方向角控制模式，利用遥控器摇杆手动控制方向，根据传感器自动控制油门 */
	CONTROL_MODE_AUTO_ALL ,           /*!< (4)全自动控制模式，根据传感器值对油门、俯仰、偏航进行全面控制*/
	CONTROL_MODE_MAX 
}ControlMode_t;


/* 定义手动模式时，模式选择开关电平 */
#define MODE_MANUL_SELECT_PIN_STATE   GPIO_PIN_SET

/************************* 导出的函数定义 ****************************/
/**
  * @brief  初始化模式控制相关变量
  * @param  无
  * @retval 无
  */
uint8_t ModeControl_Init( void );

/**
  * @brief  读取模式切换开关状态，并切换到合适模式
  * @param  无
  * @retval 无
  */
uint8_t ModeControl_CheckAndSetAutoMode( ControlMode_t auto_mode );


#endif
