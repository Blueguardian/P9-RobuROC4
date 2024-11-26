// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from canopen_interfaces:msg/CANSubscription.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__STRUCT_H_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/CANSubscription in the package canopen_interfaces.
typedef struct canopen_interfaces__msg__CANSubscription
{
  int16_t cobid;
  rosidl_runtime_c__int32__Sequence data;
} canopen_interfaces__msg__CANSubscription;

// Struct for a sequence of canopen_interfaces__msg__CANSubscription.
typedef struct canopen_interfaces__msg__CANSubscription__Sequence
{
  canopen_interfaces__msg__CANSubscription * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__msg__CANSubscription__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__STRUCT_H_
