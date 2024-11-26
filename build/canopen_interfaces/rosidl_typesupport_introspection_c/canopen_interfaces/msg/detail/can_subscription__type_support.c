// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from canopen_interfaces:msg/CANSubscription.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "canopen_interfaces/msg/detail/can_subscription__rosidl_typesupport_introspection_c.h"
#include "canopen_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "canopen_interfaces/msg/detail/can_subscription__functions.h"
#include "canopen_interfaces/msg/detail/can_subscription__struct.h"


// Include directives for member types
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  canopen_interfaces__msg__CANSubscription__init(message_memory);
}

void canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_fini_function(void * message_memory)
{
  canopen_interfaces__msg__CANSubscription__fini(message_memory);
}

size_t canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__size_function__CANSubscription__data(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__get_const_function__CANSubscription__data(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__get_function__CANSubscription__data(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__fetch_function__CANSubscription__data(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__get_const_function__CANSubscription__data(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__assign_function__CANSubscription__data(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__get_function__CANSubscription__data(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__resize_function__CANSubscription__data(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_member_array[2] = {
  {
    "cobid",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(canopen_interfaces__msg__CANSubscription, cobid),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(canopen_interfaces__msg__CANSubscription, data),  // bytes offset in struct
    NULL,  // default value
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__size_function__CANSubscription__data,  // size() function pointer
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__get_const_function__CANSubscription__data,  // get_const(index) function pointer
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__get_function__CANSubscription__data,  // get(index) function pointer
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__fetch_function__CANSubscription__data,  // fetch(index, &value) function pointer
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__assign_function__CANSubscription__data,  // assign(index, value) function pointer
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__resize_function__CANSubscription__data  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_members = {
  "canopen_interfaces__msg",  // message namespace
  "CANSubscription",  // message name
  2,  // number of fields
  sizeof(canopen_interfaces__msg__CANSubscription),
  canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_member_array,  // message members
  canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_init_function,  // function to initialize message memory (memory has to be allocated)
  canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_type_support_handle = {
  0,
  &canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_canopen_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, msg, CANSubscription)() {
  if (!canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_type_support_handle.typesupport_identifier) {
    canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &canopen_interfaces__msg__CANSubscription__rosidl_typesupport_introspection_c__CANSubscription_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
