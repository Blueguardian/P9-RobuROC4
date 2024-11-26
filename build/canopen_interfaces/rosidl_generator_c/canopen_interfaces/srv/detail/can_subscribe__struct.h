// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from canopen_interfaces:srv/CANSubscribe.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_SUBSCRIBE__STRUCT_H_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_SUBSCRIBE__STRUCT_H_

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

/// Struct defined in srv/CANSubscribe in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANSubscribe_Request
{
  rosidl_runtime_c__String command;
  int16_t cobid;
} canopen_interfaces__srv__CANSubscribe_Request;

// Struct for a sequence of canopen_interfaces__srv__CANSubscribe_Request.
typedef struct canopen_interfaces__srv__CANSubscribe_Request__Sequence
{
  canopen_interfaces__srv__CANSubscribe_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANSubscribe_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/CANSubscribe in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANSubscribe_Response
{
  bool success;
} canopen_interfaces__srv__CANSubscribe_Response;

// Struct for a sequence of canopen_interfaces__srv__CANSubscribe_Response.
typedef struct canopen_interfaces__srv__CANSubscribe_Response__Sequence
{
  canopen_interfaces__srv__CANSubscribe_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANSubscribe_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_SUBSCRIBE__STRUCT_H_
