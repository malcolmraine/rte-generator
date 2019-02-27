/*
 * Generated: 2019-02-27 16:42:38
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
float Rte_yaw;
float Rte_pitch;
float Rte_roll;

/****************************************************************************************
* RTE INTERFACE FUNCTIONS
****************************************************************************************/
inline float Rte_Read_yaw() { return  Rte_yaw; }
inline void Rte_Write_yaw(float x) { Rte_yaw = x }

inline float Rte_Read_pitch() { return  Rte_pitch; }
inline void Rte_Write_pitch(float x) { Rte_pitch = x }

inline float Rte_Read_roll() { return  Rte_roll; }
inline void Rte_Write_roll(float x) { Rte_roll = x }


#endif //TRACKEDROBOTVEHICLE_RTE_H
/****************************************************************************************
* END OF FILE
****************************************************************************************/