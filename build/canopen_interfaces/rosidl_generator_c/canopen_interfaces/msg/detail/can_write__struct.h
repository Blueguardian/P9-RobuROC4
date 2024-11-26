// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from canopen_interfaces:msg/CANWrite.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__STRUCT_H_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__STRUCT_H_

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
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/CANWrite in the package canopen_interfaces.
typedef struct canopen_interfaces__msg__CANWrite
{
  rosidl_runtime_c__String command;
  int16_t cobid;
  int8_t node_id;
  rosidl_runtime_c__int32__Sequence indices;
  rosidl_runtime_c__int32__Sequence data;
} canopen_interfaces__msg__CANWrite;

// Struct for a sequence of canopen_interfaces__msg__CANWrite.
typedef struct canopen_interfaces__msg__CANWrite__Sequence
{
  canopen_interfaces__msg__CANWrite * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__msg__CANWrite__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__STRUCT_H_
