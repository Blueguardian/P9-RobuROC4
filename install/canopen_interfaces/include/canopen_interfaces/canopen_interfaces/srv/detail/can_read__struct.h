// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from canopen_interfaces:srv/CANRead.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_READ__STRUCT_H_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_READ__STRUCT_H_

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
// Member 'indices'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/CANRead in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANRead_Request
{
  rosidl_runtime_c__String command;
  int16_t cobid;
  int8_t node_id;
  rosidl_runtime_c__int32__Sequence indices;
} canopen_interfaces__srv__CANRead_Request;

// Struct for a sequence of canopen_interfaces__srv__CANRead_Request.
typedef struct canopen_interfaces__srv__CANRead_Request__Sequence
{
  canopen_interfaces__srv__CANRead_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANRead_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'indices'
// Member 'data'
// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/CANRead in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANRead_Response
{
  rosidl_runtime_c__int32__Sequence indices;
  rosidl_runtime_c__int32__Sequence data;
  bool success;
} canopen_interfaces__srv__CANRead_Response;

// Struct for a sequence of canopen_interfaces__srv__CANRead_Response.
typedef struct canopen_interfaces__srv__CANRead_Response__Sequence
{
  canopen_interfaces__srv__CANRead_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANRead_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_READ__STRUCT_H_
