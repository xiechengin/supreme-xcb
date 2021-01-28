/**
  ******************************************************************************
  * @file    data_process.c
  * @author  zcd
  * @version V0.0.1
  * @date    2016-6-24
  * @brief   �����ƺ���
  ******************************************************************************
  * @attention
  *
  ******************************************************************************
  */ 
#include "data_typedef.h"
#include "cmsis_os.h"
#include "data_process.h"
#include "data_out.h"
#include "bsp.h"

#define ARM_MATH_CM3
#include <math.h>
#include "arm_math.h"

/* ����ֵ����  */
#define my_abs(x)   (((x)<0)?(-x):(x))

/**
  * @brief  �������ƽṹ��
  */
typedef struct gP_ControlParamStruct
{
  float p;  
}P_ControlParam_t;


/**
  * @brief  ������λ�ý綨��
  */
/* ��Ч�뾶���塣�뾶С�ڴ˷�Χ���ǲ����������ƣ�������ԭλ�õȴ�*/
#define   DATAPROCESS_VALID_CONTROL_RADIUS          300       /*!< ��ذ뾶��С�ڴ˰뾶�������ơ���λ��cm */    

/* ��Ч�߶ȶ��塣�߶��ڴ˷�Χ���ǲ����������ƣ�������ԭλ�õȴ�*/
#define   DATAPROCESS_VALID_CONTROL_ALTITUDE_MIN    50       /*!< �߶����ޡ���λ��cm                      */    
#define   DATAPROCESS_VALID_CONTROL_ALTITUDE_MAX    500       /*!< �߶����ޡ���λ��cm                      */    



/**
  * @brief  �ٶȽ綨��
  */
/* XY�����ƶ��ٶȣ������ڶ���ģʽ�£� */
#define   DATAPROCESS_XY_MOVE_VELOCITY_MAX        (0.80f)      /*!< ����ƶ��ٶȣ���λ��m/s,TODO::��ɿز����趨һ��  */    
#define   DATAPROCESS_XY_MOVE_VELOCITY_LIMIT      (0.32f)      /*!< �ƶ��ٶ����ƣ���λ��m/s  */ 

/* Z�����ƶ��ٶȣ������ڶ���ģʽ�£� */
#define   DATAPROCESS_Z_MOVE_VELOCITY_MAX         (0.60f)      /*!< ����ƶ��ٶȣ���λ��m/s,TODO::��ɿز����趨һ��  */    
#define   DATAPROCESS_Z_MOVE_VELOCITY_LIMIT       (0.20f)      /*!< �ƶ��ٶ����ƣ���λ��m/s  */ 



/**
  * @brief ���������綨��
  */
/* X������� */
#define   DATAPROCESS_X_CONTROL_VALUE_P_MIN       (0.00f)           /*!< ��������-P������Сֵ           */
#define   DATAPROCESS_X_CONTROL_VALUE_P_MAX       (0.50f)           /*!< ��������-P�������ֵ           */
#define   DATAPROCESS_X_CONTROL_VALUE_P_DEFAULT   (0.18f)           /*!< ��������-P����Ĭ��ֵ           */      
//TODO::ϸ�µ���DEFAULT����

/* Y������� */
#define   DATAPROCESS_Y_CONTROL_VALUE_P_MIN       (0.00f)           /*!< ��������-P������Сֵ           */
#define   DATAPROCESS_Y_CONTROL_VALUE_P_MAX       (0.50f)           /*!< ��������-P�������ֵ           */
#define   DATAPROCESS_Y_CONTROL_VALUE_P_DEFAULT   (0.16f)           /*!< ��������-P����Ĭ��ֵ           */      

/* Z������Ʋ��� */
#define   DATAPROCESS_Z_CONTROL_VALUE_P_MIN       (0.00f)           /*!< ��������-P������Сֵ           */
#define   DATAPROCESS_Z_CONTROL_VALUE_P_MAX       (0.40f )          /*!< ��������-P�������ֵ           */
#define   DATAPROCESS_Z_CONTROL_VALUE_P_DEFAULT   (0.05f)           /*!< ��������-P����Ĭ��ֵ           */      




/*************************** ȫ�ֱ����ṹ�� ****************************/
/* �������ƽṹ�� */
static P_ControlParam_t*   P_ControlParam_X;
static P_ControlParam_t*   P_ControlParam_Y;
static P_ControlParam_t*   P_ControlParam_Z;

/* �������ݴ���ʱ��� */
static uint32_t    gLast_Processtime;
#define   MAX_SENSOR_LOSE_TIME    800 /*!< ���������������ʧʱ��(��������ʧ�����ݴ�����Ӧֹͣ)����λ:ms  */

/****************************** �������� *******************************/
/**
  * @brief  ��ʼ���������ƵĽṹ��
  * @param  control_param: ���������ṹ��
  * @param  input: ����ֵ
  * @param  param_p: �趨������ʼֵ
  * 
  * @retval float: ������
  */
static void   DataProcess_InitPControlParam( P_ControlParam_t* control_param,float param_p )
{
  assert_param( control_param != NULL );
  
  /* ��ֵ */
  if( param_p > DATAPROCESS_X_CONTROL_VALUE_P_MAX)
  {
    control_param->p  = DATAPROCESS_X_CONTROL_VALUE_P_MAX ;
  }else if( param_p < DATAPROCESS_X_CONTROL_VALUE_P_MIN)
  {
    control_param->p  = DATAPROCESS_X_CONTROL_VALUE_P_MIN ;
  }else
  {
    control_param->p  = param_p ;
  }

}



/**
  * @brief  �ж��Ƿ��ڿɿط�Χ��
  * @param  pSensorData: ������ֵ
  * @retval uint8_t: �жϽ���� ��ȫ����=pdTRUE,��ȫ����=pdFALSE;
  */
static uint8_t    DataProcess_isInSaftyZone( SensorData_t* pSensorData )
{
  assert_param( pSensorData != NULL );
  
  /* �жϷ������Ƿ��ڰ�ȫ�뾶���� */
  if( my_abs( pSensorData->x ) > DATAPROCESS_VALID_CONTROL_RADIUS )
  {
    return pdFALSE;
  }
  if( my_abs(pSensorData->y) > DATAPROCESS_VALID_CONTROL_RADIUS )
  {
    return pdFALSE;
  }
  
  /* �жϷ������Ƿ��ڰ�ȫ�߶��� */
  if( pSensorData->z > DATAPROCESS_VALID_CONTROL_ALTITUDE_MAX )
  {
    return pdFALSE;
  }else  if( pSensorData->z < DATAPROCESS_VALID_CONTROL_ALTITUDE_MIN )
  {
    return pdFALSE;
  }
  
  
  return pdTRUE;
}



/**
  * @brief  ����Ŀ���͵�ǰ��ľ�����ϱ����������������ֵ
  * @param  control_param: ���������ṹ��
  * @param  input: ����ֵ
  * @param  setpoint: Ŀ��ֵ
  * 
  * @retval float: ������
  */
static float   DataProcess_CalcPControlValue( P_ControlParam_t* control_param,int16_t input , int16_t  setpoint  )
{
  float  err;
  float  out;

  assert_param( control_param != NULL );
  
 
  /* 1.���㵱ǰֵ��Ŀ��ֵ�Ĳ�� */
  err = setpoint - input;
  
  /* 2.����������ͱ���ϵ���ĳ˻�������� */
  out = control_param->p * err ;
 
 
  return out;
}




/****************************** �����ĺ��� ���� *******************************/


/**
  * @brief  ��ʼ������ģ��
  * @param  none
  * @retval uint8_t: ִ��״̬
  */
uint8_t   DataProcess_Init( void )
{
  /* Ϊ�ṹ������ռ� */
  P_ControlParam_X = pvPortMalloc(sizeof(P_ControlParam_t));
  P_ControlParam_Y = pvPortMalloc(sizeof(P_ControlParam_t));
  P_ControlParam_Z = pvPortMalloc(sizeof(P_ControlParam_t));
  
  /* ��ʼ���ṹ�� */
  if( (P_ControlParam_X != NULL)&&(P_ControlParam_Y != NULL)&&(P_ControlParam_Z != NULL) )
  {
    DataProcess_InitPControlParam( P_ControlParam_X, DATAPROCESS_X_CONTROL_VALUE_P_DEFAULT );
    DataProcess_InitPControlParam( P_ControlParam_Y, DATAPROCESS_Y_CONTROL_VALUE_P_DEFAULT );
    DataProcess_InitPControlParam( P_ControlParam_Z, DATAPROCESS_Z_CONTROL_VALUE_P_DEFAULT );
  }
  else
  {
    SYS_DEBUG("pvPortMalloc Fail!!\n");
    return pdFAIL;
  }
  
  return pdPASS;
}




/**
  * @brief  �����λ��ѹ��ʹ����������λ��
  * @param  pControlData: �����ѹֵ
  * @retval none
  */
void   DataProcess_SetDataForRelease(  ControlData_t* pControlData   )
{
  assert_param( pControlData != NULL );

  /* roll���У�ʹx����ֹͣ�ƶ� */
  pControlData->roll     = DAC_ROLL_UOUT_CENTER;
  
  /* pitch���У�ʹy����ֹͣ�ƶ� */
  pControlData->pitch    = DAC_PITCH_UOUT_CENTER;
  
  /* ���Ż��У�ʹ��ֱ����ֹͣ�ƶ� */
  pControlData->throttle = DAC_THROTTLE_UOUT_CONTER;
}



/**
  * @brief   ����ϵͳ����������ִ��ʱ�䣬�����ʱ��û���յ����ݻ���û�д��������ͷŷ����� 
  * @note     �˺��������DAC��ע���������߳�ʹ��ʱ��������������̲߳���ͬһʱ��ִ��
  */
void   DataProcess_CheackProcessTime(  void  )
{
  uint32_t    current_Processtime;

  /* ��ȡ��ǰʱ�� */
  current_Processtime  = osKernelSysTick();
  
  /* �ж��Ƿ�ʱ */
  if(  (current_Processtime - gLast_Processtime)*portTICK_PERIOD_MS > MAX_SENSOR_LOSE_TIME )
  {
    /* ��ʱ���ͷſ��� */
    ControlOut_ReleaseControl();
  }
  
}




/**
  * @brief  �Դ��������ݽ��д����������������
  * @param  ptr: ��У������ָ��
  * @param  len: ��У�����ݳ���
  *                     
  *                 (Y) [pitch]    
  *                  ^                                   
  *                  |                                   
  *                  |                                  
  *           <------0-----> (X) [roll]                              
  *                  |                                  
  *                  |                                  
  *                  V                                  
  *                                                     
  * @retval uint8_t: У��ֵ
  */
uint8_t   DataProcess_DoProcess( SensorData_t* pSensorData, ControlData_t* pControlData  )
{
  /* ����������ڽ�� */
  float XV_POut;
  float YV_POut;
  float ZV_POut;

  /* ���水�ջ�����̬�ķ�����*/
  float XV_Out;
  float YV_Out;
  float ZV_Out;
  
  float dYaw;       /* ������������ھֲ�����ϵ����ת�� */
  dYaw = 0;         /* ������������ھֲ�����ϵһ��ʱ, dYawΪ0*/
  
  /* ����Ƿ�Ϊ�� */
  assert_param( pSensorData != NULL );
  assert_param( pControlData != NULL );
  
#if 0   
    SYS_DEBUG("Sensor Data=(%d,%d,%d)\n",pSensorData->x,pSensorData->y,pSensorData->z);
#endif

  /* ִ�п��� */
  if(  DataProcess_isInSaftyZone( pSensorData ) == pdTRUE )
  {
    
    /* 1.���ݵ�ǰλ�á�Ŀ��λ�ã��������Ŀ���ƶ����ٶȿ�����  */
    XV_POut = DataProcess_CalcPControlValue( P_ControlParam_X  , pSensorData->x , 0 );       // x������ƣ�ͨ��roll ͨ������x����
    YV_POut = DataProcess_CalcPControlValue( P_ControlParam_Y  , pSensorData->y , 0 );       // y������ƣ�ͨ��pitchͨ������y����
    ZV_POut = DataProcess_CalcPControlValue( P_ControlParam_Z  , pSensorData->z , 0 );       // z������ƣ�ͨ��Throttleͨ������z����

#if 0   
  SYS_DEBUG("XV_POut=%f,YV_POut=%f,ZV_POut=%f\n",XV_POut,YV_POut,ZV_POut);
#endif
 
    /* ��λת����cm--->m    */
    XV_POut = XV_POut/100.0;
    YV_POut = YV_POut/100.0;
    ZV_POut = ZV_POut/100.0;
    
    /* 2.�����������䵽 ��������ϵ�� X,Y,Z����ӦRoll��Pitch��Throttle�� ���� */
    XV_Out  = +XV_POut * cos(dYaw) - YV_POut*sin(dYaw) ;
    YV_Out  = +XV_POut * sin(dYaw) + YV_POut*cos(dYaw) ;
    ZV_Out  = ZV_POut;
    
#if 0   
    SYS_DEBUG("XV_Out  = +%f * cos(%f) - %f*sin(%f) = %f ;\n",XV_POut,dYaw, YV_POut,dYaw,XV_Out );
    SYS_DEBUG("YV_Out  = +%f * sin(%f) + %f*cos(%f) = %f ;\n",XV_POut,dYaw, YV_POut,dYaw,YV_Out );
    SYS_DEBUG("ZV_Out  = %f\n", ZV_Out );
#endif
    
    /* ��Χ����  */
    if( XV_Out > +DATAPROCESS_XY_MOVE_VELOCITY_LIMIT )   { XV_Out = +DATAPROCESS_XY_MOVE_VELOCITY_LIMIT;  }
    if( XV_Out < -DATAPROCESS_XY_MOVE_VELOCITY_LIMIT )   { XV_Out = -DATAPROCESS_XY_MOVE_VELOCITY_LIMIT;  }
    if( YV_Out > +DATAPROCESS_XY_MOVE_VELOCITY_LIMIT )   { YV_Out = +DATAPROCESS_XY_MOVE_VELOCITY_LIMIT;  }
    if( YV_Out < -DATAPROCESS_XY_MOVE_VELOCITY_LIMIT )   { YV_Out = -DATAPROCESS_XY_MOVE_VELOCITY_LIMIT;  }
    if( ZV_Out > +DATAPROCESS_Z_MOVE_VELOCITY_LIMIT  )   { ZV_Out = +DATAPROCESS_Z_MOVE_VELOCITY_LIMIT ;  }
    if( ZV_Out < -DATAPROCESS_Z_MOVE_VELOCITY_LIMIT  )   { ZV_Out = -DATAPROCESS_Z_MOVE_VELOCITY_LIMIT ;  }
    
    /* 3.������������ɿ��Ƶ�ѹ */
    pControlData->roll      = (XV_Out/DATAPROCESS_XY_MOVE_VELOCITY_MAX)*DAC_ROLL_UOUT_CONTROL_ZONE*DAC_ROLL_UOUT_DIRECTIOPN\
                              + DAC_ROLL_UOUT_CENTER    ;
    pControlData->pitch     = (YV_Out/DATAPROCESS_XY_MOVE_VELOCITY_MAX)*DAC_PITCH_UOUT_CONTROL_ZONE*DAC_PITCH_UOUT_DIRECTIOPN\
                              + DAC_PITCH_UOUT_CENTER   ;
    pControlData->throttle  = (ZV_Out/DATAPROCESS_Z_MOVE_VELOCITY_MAX )*DAC_THROTTLE_UOUT_CONTROL_ZONE*DAC_THROTTLE_UOUT_DIRECTIOPN\
                              + DAC_THROTTLE_UOUT_CONTER;  
    
    
    
    /* ������� */
#if 1   
    SYS_DEBUG("roll     = (%f/%f)*%f*%d+%f=%f\n", XV_Out, DATAPROCESS_XY_MOVE_VELOCITY_MAX, DAC_ROLL_UOUT_CONTROL_ZONE    ,DAC_ROLL_UOUT_DIRECTIOPN    ,DAC_ROLL_UOUT_CENTER    , pControlData->roll);
    SYS_DEBUG("pitch    = (%f/%f)*%f*%d+%f=%f\n", YV_Out, DATAPROCESS_XY_MOVE_VELOCITY_MAX, DAC_PITCH_UOUT_CONTROL_ZONE   ,DAC_PITCH_UOUT_DIRECTIOPN   ,DAC_PITCH_UOUT_CENTER   , pControlData->pitch);
    SYS_DEBUG("throttle = (%f/%f)*%f*%d+%f=%f\n", ZV_Out, DATAPROCESS_Z_MOVE_VELOCITY_MAX, DAC_THROTTLE_UOUT_CONTROL_ZONE ,DAC_THROTTLE_UOUT_DIRECTIOPN,DAC_THROTTLE_UOUT_CONTER , pControlData->throttle);
#endif
    
    /* ˢ�´���ʱ��� */
    gLast_Processtime = osKernelSysTick();
  
  }else
  {
    /* ��д��λ��ֵ��ʹ���������ֲ��� */
    DataProcess_SetDataForRelease( pControlData );
    
    /* �����ʾ */
    SYS_DEBUG("Not in safety area, holding...\n");

  }
  
  
  return 0;
}
