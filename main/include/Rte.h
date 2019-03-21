/*
 * Generated: 2019-03-11 13:05:16
 * User: malcolmhall
*/
#ifndef TRACKEDROBOTVEHICLE_RTE_H
#define  TRACKEDROBOTVEHICLE_RTE_H
/****************************************************************************************
* HEADER FILES
****************************************************************************************/


/****************************************************************************************
* DEFINES
****************************************************************************************/


/****************************************************************************************
* RTE VARIABLES
****************************************************************************************/
uint8_t Rte_EncoderSysState;
float Rte_MotorPositionLeft;
float Rte_MotorPositionRight;
uint32_t Rte_EncoderPreviousTime;
uint32_t Rte_EncoderCurrentTime;
float Rte_TrackSpeedLeft;
float Rte_TrackSpeedRight;
float Rte_EncoderFilValLeft;
float Rte_EncoderFilValRight;
uint8_t Rte_MotorCtrlSysState;
float Rte_speed_cmd;
float Rte_steer_cmd;
float Rte_left_track_pwm;
float Rte_right_track_pwm;

/****************************************************************************************
* RTE INTERFACE FUNCTIONS
****************************************************************************************/
inline uint8_t Rte_Read_EncoderSysState() { return  Rte_EncoderSysState; }
inline void Rte_Write_EncoderSysState(uint8_t x) { Rte_EncoderSysState = x }

inline float Rte_Read_MotorPositionLeft() { return  Rte_MotorPositionLeft; }
inline void Rte_Write_MotorPositionLeft(float x) { Rte_MotorPositionLeft = x }

inline float Rte_Read_MotorPositionRight() { return  Rte_MotorPositionRight; }
inline void Rte_Write_MotorPositionRight(float x) { Rte_MotorPositionRight = x }

inline uint32_t Rte_Read_EncoderPreviousTime() { return  Rte_EncoderPreviousTime; }
inline void Rte_Write_EncoderPreviousTime(uint32_t x) { Rte_EncoderPreviousTime = x }

inline uint32_t Rte_Read_EncoderCurrentTime() { return  Rte_EncoderCurrentTime; }
inline void Rte_Write_EncoderCurrentTime(uint32_t x) { Rte_EncoderCurrentTime = x }

inline float Rte_Read_TrackSpeedLeft() { return  Rte_TrackSpeedLeft; }
inline void Rte_Write_TrackSpeedLeft(float x) { Rte_TrackSpeedLeft = x }

inline float Rte_Read_TrackSpeedRight() { return  Rte_TrackSpeedRight; }
inline void Rte_Write_TrackSpeedRight(float x) { Rte_TrackSpeedRight = x }

inline float Rte_Read_EncoderFilValLeft() { return  Rte_EncoderFilValLeft; }
inline void Rte_Write_EncoderFilValLeft(float x) { Rte_EncoderFilValLeft = x }

inline float Rte_Read_EncoderFilValRight() { return  Rte_EncoderFilValRight; }
inline void Rte_Write_EncoderFilValRight(float x) { Rte_EncoderFilValRight = x }

inline uint8_t Rte_Read_MotorCtrlSysState() { return  Rte_MotorCtrlSysState; }
inline void Rte_Write_MotorCtrlSysState(uint8_t x) { Rte_MotorCtrlSysState = x }

inline float Rte_Read_speed_cmd() { return  Rte_speed_cmd; }
inline void Rte_Write_speed_cmd(float x) { Rte_speed_cmd = x }

inline float Rte_Read_steer_cmd() { return  Rte_steer_cmd; }
inline void Rte_Write_steer_cmd(float x) { Rte_steer_cmd = x }

inline float Rte_Read_left_track_pwm() { return  Rte_left_track_pwm; }
inline void Rte_Write_left_track_pwm(float x) { Rte_left_track_pwm = x }

inline float Rte_Read_right_track_pwm() { return  Rte_right_track_pwm; }
inline void Rte_Write_right_track_pwm(float x) { Rte_right_track_pwm = x }


#endif //TRACKEDROBOTVEHICLE_RTE_H
/****************************************************************************************
* END OF FILE
****************************************************************************************/
