// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from canopen_interfaces:msg/CANSubscription.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "canopen_interfaces/msg/detail/can_subscription__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace canopen_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void CANSubscription_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) canopen_interfaces::msg::CANSubscription(_init);
}

void CANSubscription_fini_function(void * message_memory)
{
  auto typed_message = static_cast<canopen_interfaces::msg::CANSubscription *>(message_memory);
  typed_message->~CANSubscription();
}

size_t size_function__CANSubscription__data(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__CANSubscription__data(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__CANSubscription__data(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__CANSubscription__data(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__CANSubscription__data(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__CANSubscription__data(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__CANSubscription__data(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__CANSubscription__data(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember CANSubscription_message_member_array[2] = {
  {
    "cobid",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(canopen_interfaces::msg::CANSubscription, cobid),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "data",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(canopen_interfaces::msg::CANSubscription, data),  // bytes offset in struct
    nullptr,  // default value
    size_function__CANSubscription__data,  // size() function pointer
    get_const_function__CANSubscription__data,  // get_const(index) function pointer
    get_function__CANSubscription__data,  // get(index) function pointer
    fetch_function__CANSubscription__data,  // fetch(index, &value) function pointer
    assign_function__CANSubscription__data,  // assign(index, value) function pointer
    resize_function__CANSubscription__data  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers CANSubscription_message_members = {
  "canopen_interfaces::msg",  // message namespace
  "CANSubscription",  // message name
  2,  // number of fields
  sizeof(canopen_interfaces::msg::CANSubscription),
  CANSubscription_message_member_array,  // message members
  CANSubscription_init_function,  // function to initialize message memory (memory has to be allocated)
  CANSubscription_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t CANSubscription_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &CANSubscription_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace canopen_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<canopen_interfaces::msg::CANSubscription>()
{
  return &::canopen_interfaces::msg::rosidl_typesupport_introspection_cpp::CANSubscription_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, canopen_interfaces, msg, CANSubscription)() {
  return &::canopen_interfaces::msg::rosidl_typesupport_introspection_cpp::CANSubscription_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
