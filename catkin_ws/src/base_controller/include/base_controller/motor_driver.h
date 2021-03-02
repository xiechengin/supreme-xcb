#ifndef MOTO_DRIVER_H
#define MOTO_DRIVER_H

#include <string>


class MotorDriver
{
public:
  typedef struct stSpeedCmd {
    int   id;
    int   rpm;
  }SpeedCmd;

  typedef struct stEnableCmd {
    int   id;
    bool  enable;
  }EnableCmd;

  typedef struct stStopCmd {
    int   id;
    bool  brake;
  }StopCmd;

  MotorDriver() {}

  virtual ~MotorDriver() {}

  /**
   * @brief setParams
   * @param params
   * @return
   */
  virtual bool setParams(const std::string &params) = 0;

  /**
   * @brief init
   */
  virtual int init() = 0;

  /**
   * @brief close
   */
  virtual int close() = 0;

  /**
   * @brief setEnable
   * @param id
   * @param enable
   * @return
   */
  virtual int setEnable(const EnableCmd* cmds, int count) = 0;

  /**
   * @brief setSpeed
   * @param id
   * @param rpm
   * @return
   */
  virtual int setSpeed(const SpeedCmd* cmds, int count) = 0;

  /**
   * @brief stop
   * @param id
   * @param brake
   * @return
   */
  virtual int stop(const StopCmd* cmds, int count) = 0;

  /**
   * @brief getSpeed
   * @param id
   * @param rpm
   * @return
   */
  virtual int getSpeed(SpeedCmd* cmds, int count) = 0;

  /**
   * @brief getError
   * @param id
   * @return
   */
  virtual int getError(int id) = 0;

};


#endif // MOTO_DRIVER_H
