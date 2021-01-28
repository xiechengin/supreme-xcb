#ifndef EASY_TRACER_STATUS_M_H
#define EASY_TRACER_STATUS_M_H

//#define NEED_DEBUG 1

#define IMG_X 0	  //ͼƬx����
#define IMG_Y 0	  //ͼƬy����
#define IMG_W 80 //ͼƬ���
#define IMG_H 60 //ͼƬ�߶�

//#define ALLOW_FAIL_PER 3 //�ݴ��ʣ�ÿ1<<ALLOW_FAIL_PER�����������һ������㣬�ݴ���Խ��Խ����ʶ�𣬵�������Խ��

//#define GUI_ReadBit16Point ST7781_LCD_ReadPoint

typedef struct{
    unsigned char  H_MIN;//Ŀ����Сɫ��
    unsigned char  H_MAX;//Ŀ�����ɫ��	
    
	unsigned char  S_MIN;//Ŀ����С���Ͷ�  
    unsigned char  S_MAX;//Ŀ����󱥺Ͷ�
	
	unsigned char  L_MIN;//Ŀ����С����  
    unsigned char  L_MAX;//Ŀ���������
	
	unsigned int  WIDTH_MIN;//Ŀ����С���
	unsigned int  HIGHT_MIN;//Ŀ����С�߶�

	unsigned int  WIDTH_MAX;//Ŀ�������
	unsigned int  HIGHT_MAX;//Ŀ�����߶�

}TARGET_CONDI;//�ж�Ϊ��Ŀ������

typedef struct{
	unsigned int x;//Ŀ���x����
	unsigned int y;//Ŀ���y����
	unsigned int w;//Ŀ��Ŀ��
	unsigned int h;//Ŀ��ĸ߶�
}RESULT;//ʶ����

typedef struct{
    unsigned char  red;             // [0,255]
    unsigned char  green;           // [0,255]
    unsigned char  blue;            // [0,255]
}COLOR_RGB;//RGB��ʽ��ɫ

typedef struct{
    unsigned char hue;              // [0,240]
    unsigned char saturation;       // [0,240]
    unsigned char luminance;        // [0,240]
}COLOR_HSL;//HSL��ʽ��ɫ

typedef struct{
    unsigned int X_Start;              
    unsigned int X_End;
	unsigned int Y_Start;              
    unsigned int Y_End;
}SEARCH_AREA;//����

typedef enum{
	TS_FIND_IN_FULL_FRAME,//ȫͼʶ��
	TS_FIND_IN_LAST_FRAME,//��һ��ͼ��ʶ��
	TS_TRACING,//����
}TRACE_STATE;

//Ψһ��API���û���ʶ������д��Conditionָ��Ľṹ���У��ú���������Ŀ���x��y����ͳ���
//����1ʶ��ɹ�������1ʶ��ʧ��
int Trace(const TARGET_CONDI *Condition,RESULT *Resu);

void ReadColor(unsigned int x,unsigned int y,COLOR_RGB *Rgb);
void RGBtoHSL(const COLOR_RGB *Rgb, COLOR_HSL *Hsl);

#endif
