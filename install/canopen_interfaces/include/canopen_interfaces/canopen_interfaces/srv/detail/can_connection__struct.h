// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from canopen_interfaces:srv/CANConnection.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_CONNECTION__STRUCT_H_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_CONNECTION__STRUCT_H_

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

/// Struct defined in srv/CANConnection in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANConnection_Request
{
  rosidl_runtime_c__String command;
} canopen_interfaces__srv__CANConnection_Request;

// Struct for a sequence of canopen_interfaces__srv__CANConnection_Request.
typedef struct canopen_interfaces__srv__CANConnection_Request__Sequence
{
  canopen_interfaces__srv__CANConnection_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANConnection_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'node_list'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/CANConnection in the package canopen_interfaces.
typedef struct canopen_interfaces__srv__CANConnection_Response
{
  rosidl_runtime_c__int8__Sequence node_list;
  bool success;
} canopen_interfaces__srv__CANConnection_Response;

// Struct for a sequence of canopen_interfaces__srv__CANConnection_Response.
typedef struct canopen_interfaces__srv__CANConnection_Response__Sequence
{
  canopen_interfaces__srv__CANConnection_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} canopen_interfaces__srv__CANConnection_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_CONNECTION__STRUCT_H_
