// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from canopen_interfaces:srv/CANRead.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "canopen_interfaces/srv/detail/can_read__struct.h"
#include "canopen_interfaces/srv/detail/can_read__type_support.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace canopen_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _CANRead_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _CANRead_Request_type_support_ids_t;

static const _CANRead_Request_type_support_ids_t _CANRead_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _CANRead_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _CANRead_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _CANRead_Request_type_support_symbol_names_t _CANRead_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, canopen_interfaces, srv, CANRead_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANRead_Request)),
  }
};

typedef struct _CANRead_Request_type_support_data_t
{
  void * data[2];
} _CANRead_Request_type_support_data_t;

static _CANRead_Request_type_support_data_t _CANRead_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _CANRead_Request_message_typesupport_map = {
  2,
  "canopen_interfaces",
  &_CANRead_Request_message_typesupport_ids.typesupport_identifier[0],
  &_CANRead_Request_message_typesupport_symbol_names.symbol_name[0],
  &_CANRead_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t CANRead_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_CANRead_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace canopen_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, canopen_interfaces, srv, CANRead_Request)() {
  return &::canopen_interfaces::srv::rosidl_typesupport_c::CANRead_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "canopen_interfaces/srv/detail/can_read__struct.h"
// already included above
// #include "canopen_interfaces/srv/detail/can_read__type_support.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace canopen_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _CANRead_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _CANRead_Response_type_support_ids_t;

static const _CANRead_Response_type_support_ids_t _CANRead_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _CANRead_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _CANRead_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _CANRead_Response_type_support_symbol_names_t _CANRead_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, canopen_interfaces, srv, CANRead_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANRead_Response)),
  }
};

typedef struct _CANRead_Response_type_support_data_t
{
  void * data[2];
} _CANRead_Response_type_support_data_t;

static _CANRead_Response_type_support_data_t _CANRead_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _CANRead_Response_message_typesupport_map = {
  2,
  "canopen_interfaces",
  &_CANRead_Response_message_typesupport_ids.typesupport_identifier[0],
  &_CANRead_Response_message_typesupport_symbol_names.symbol_name[0],
  &_CANRead_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t CANRead_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_CANRead_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace canopen_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, canopen_interfaces, srv, CANRead_Response)() {
  return &::canopen_interfaces::srv::rosidl_typesupport_c::CANRead_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "canopen_interfaces/srv/detail/can_read__type_support.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace canopen_interfaces
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _CANRead_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _CANRead_type_support_ids_t;

static const _CANRead_type_support_ids_t _CANRead_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _CANRead_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _CANRead_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _CANRead_type_support_symbol_names_t _CANRead_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, canopen_interfaces, srv, CANRead)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, canopen_interfaces, srv, CANRead)),
  }
};

typedef struct _CANRead_type_support_data_t
{
  void * data[2];
} _CANRead_type_support_data_t;

static _CANRead_type_support_data_t _CANRead_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _CANRead_service_typesupport_map = {
  2,
  "canopen_interfaces",
  &_CANRead_service_typesupport_ids.typesupport_identifier[0],
  &_CANRead_service_typesupport_symbol_names.symbol_name[0],
  &_CANRead_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t CANRead_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_CANRead_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace canopen_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, canopen_interfaces, srv, CANRead)() {
  return &::canopen_interfaces::srv::rosidl_typesupport_c::CANRead_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif
