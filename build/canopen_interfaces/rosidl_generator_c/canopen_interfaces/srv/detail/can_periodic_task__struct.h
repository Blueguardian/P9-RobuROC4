// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from canopen_interfaces:srv/CANPeriodicTask.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__STRUCT_H_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'command'
#include "rosidl_runtime_c/string.h"
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/CANPeriodicTask in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANPeriodicTask_Request
{
  rosidl_runtime_c__String command;
  int16_t cobid;
  rosidl_runtime_c__int32__Sequence data;
  float period;
} canopen_interfaces__srv__CANPeriodicTask_Request;

// Struct for a sequence of canopen_interfaces__srv__CANPeriodicTask_Request.
typedef struct canopen_interfaces__srv__CANPeriodicTask_Request__Sequence
{
  canopen_interfaces__srv__CANPeriodicTask_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANPeriodicTask_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/CANPeriodicTask in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANPeriodicTask_Response
{
  bool success;
} canopen_interfaces__srv__CANPeriodicTask_Response;

// Struct for a sequence of canopen_interfaces__srv__CANPeriodicTask_Response.
typedef struct canopen_interfaces__srv__CANPeriodicTask_Response__Sequence
{
  canopen_interfaces__srv__CANPeriodicTask_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANPeriodicTask_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__STRUCT_H_
