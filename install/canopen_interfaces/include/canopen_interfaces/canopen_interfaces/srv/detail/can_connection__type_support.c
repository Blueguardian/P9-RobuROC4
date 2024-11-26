// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from canopen_interfaces:srv/CANConnection.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "canopen_interfaces/srv/detail/can_connection__rosidl_typesupport_introspection_c.h"
#include "canopen_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "canopen_interfaces/srv/detail/can_connection__functions.h"
#include "canopen_interfaces/srv/detail/can_connection__struct.h"


// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  canopen_interfaces__srv__CANConnection_Request__init(message_memory);
}

void canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_fini_function(void * message_memory)
{
  canopen_interfaces__srv__CANConnection_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_member_array[1] = {
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(canopen_interfaces__srv__CANConnection_Request, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_members = {
  "canopen_interfaces__srv",  // message namespace
  "CANConnection_Request",  // message name
  1,  // number of fields
  sizeof(canopen_interfaces__srv__CANConnection_Request),
  canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_member_array,  // message members
  canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_type_support_handle = {
  0,
  &canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_canopen_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANConnection_Request)() {
  if (!canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_type_support_handle.typesupport_identifier) {
    canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &canopen_interfaces__srv__CANConnection_Request__rosidl_typesupport_introspection_c__CANConnection_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "canopen_interfaces/srv/detail/can_connection__rosidl_typesupport_introspection_c.h"
// already included above
// #include "canopen_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "canopen_interfaces/srv/detail/can_connection__functions.h"
// already included above
// #include "canopen_interfaces/srv/detail/can_connection__struct.h"


// Include directives for member types
// Member `node_list`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  canopen_interfaces__srv__CANConnection_Response__init(message_memory);
}

void canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_fini_function(void * message_memory)
{
  canopen_interfaces__srv__CANConnection_Response__fini(message_memory);
}

size_t canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__size_function__CANConnection_Response__node_list(
  const void * untyped_member)
{
  const rosidl_runtime_c__int8__Sequence * member =
    (const rosidl_runtime_c__int8__Sequence *)(untyped_member);
  return member->size;
}

const void * canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__get_const_function__CANConnection_Response__node_list(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int8__Sequence * member =
    (const rosidl_runtime_c__int8__Sequence *)(untyped_member);
  return &member->data[index];
}

void * canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__get_function__CANConnection_Response__node_list(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int8__Sequence * member =
    (rosidl_runtime_c__int8__Sequence *)(untyped_member);
  return &member->data[index];
}

void canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__fetch_function__CANConnection_Response__node_list(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int8_t * item =
    ((const int8_t *)
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__get_const_function__CANConnection_Response__node_list(untyped_member, index));
  int8_t * value =
    (int8_t *)(untyped_value);
  *value = *item;
}

void canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__assign_function__CANConnection_Response__node_list(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int8_t * item =
    ((int8_t *)
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__get_function__CANConnection_Response__node_list(untyped_member, index));
  const int8_t * value =
    (const int8_t *)(untyped_value);
  *item = *value;
}

bool canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__resize_function__CANConnection_Response__node_list(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int8__Sequence * member =
    (rosidl_runtime_c__int8__Sequence *)(untyped_member);
  rosidl_runtime_c__int8__Sequence__fini(member);
  return rosidl_runtime_c__int8__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_member_array[2] = {
  {
    "node_list",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(canopen_interfaces__srv__CANConnection_Response, node_list),  // bytes offset in struct
    NULL,  // default value
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__size_function__CANConnection_Response__node_list,  // size() function pointer
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__get_const_function__CANConnection_Response__node_list,  // get_const(index) function pointer
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__get_function__CANConnection_Response__node_list,  // get(index) function pointer
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__fetch_function__CANConnection_Response__node_list,  // fetch(index, &value) function pointer
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__assign_function__CANConnection_Response__node_list,  // assign(index, value) function pointer
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__resize_function__CANConnection_Response__node_list  // resize(index) function pointer
  },
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(canopen_interfaces__srv__CANConnection_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_members = {
  "canopen_interfaces__srv",  // message namespace
  "CANConnection_Response",  // message name
  2,  // number of fields
  sizeof(canopen_interfaces__srv__CANConnection_Response),
  canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_member_array,  // message members
  canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_type_support_handle = {
  0,
  &canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_canopen_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANConnection_Response)() {
  if (!canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_type_support_handle.typesupport_identifier) {
    canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &canopen_interfaces__srv__CANConnection_Response__rosidl_typesupport_introspection_c__CANConnection_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "canopen_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "canopen_interfaces/srv/detail/can_connection__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_service_members = {
  "canopen_interfaces__srv",  // service namespace
  "CANConnection",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_Request_message_type_support_handle,
  NULL  // response message
  // canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_Response_message_type_support_handle
};

static rosidl_service_type_support_t canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_service_type_support_handle = {
  0,
  &canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANConnection_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANConnection_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_canopen_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANConnection)() {
  if (!canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_service_type_support_handle.typesupport_identifier) {
    canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANConnection_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANConnection_Response)()->data;
  }

  return &canopen_interfaces__srv__detail__can_connection__rosidl_typesupport_introspection_c__CANConnection_service_type_support_handle;
}