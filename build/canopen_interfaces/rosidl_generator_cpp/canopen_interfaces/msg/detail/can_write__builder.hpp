// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from canopen_interfaces:msg/CANWrite.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__BUILDER_HPP_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "canopen_interfaces/msg/detail/can_write__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace canopen_interfaces
{

namespace msg
{

namespace builder
{

class Init_CANWrite_data
{
public:
  explicit Init_CANWrite_data(::canopen_interfaces::msg::CANWrite & msg)
  : msg_(msg)
  {}
  ::canopen_interfaces::msg::CANWrite data(::canopen_interfaces::msg::CANWrite::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::msg::CANWrite msg_;
};

class Init_CANWrite_indices
{
public:
  explicit Init_CANWrite_indices(::canopen_interfaces::msg::CANWrite & msg)
  : msg_(msg)
  {}
  Init_CANWrite_data indices(::canopen_interfaces::msg::CANWrite::_indices_type arg)
  {
    msg_.indices = std::move(arg);
    return Init_CANWrite_data(msg_);
  }

private:
  ::canopen_interfaces::msg::CANWrite msg_;
};

class Init_CANWrite_node_id
{
public:
  explicit Init_CANWrite_node_id(::canopen_interfaces::msg::CANWrite & msg)
  : msg_(msg)
  {}
  Init_CANWrite_indices node_id(::canopen_interfaces::msg::CANWrite::_node_id_type arg)
  {
    msg_.node_id = std::move(arg);
    return Init_CANWrite_indices(msg_);
  }

private:
  ::canopen_interfaces::msg::CANWrite msg_;
};

class Init_CANWrite_cobid
{
public:
  explicit Init_CANWrite_cobid(::canopen_interfaces::msg::CANWrite & msg)
  : msg_(msg)
  {}
  Init_CANWrite_node_id cobid(::canopen_interfaces::msg::CANWrite::_cobid_type arg)
  {
    msg_.cobid = std::move(arg);
    return Init_CANWrite_node_id(msg_);
  }

private:
  ::canopen_interfaces::msg::CANWrite msg_;
};

class Init_CANWrite_command
{
public:
  Init_CANWrite_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CANWrite_cobid command(::canopen_interfaces::msg::CANWrite::_command_type arg)
  {
    msg_.command = std::move(arg);
    return Init_CANWrite_cobid(msg_);
  }

private:
  ::canopen_interfaces::msg::CANWrite msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::msg::CANWrite>()
{
  return canopen_interfaces::msg::builder::Init_CANWrite_command();
}

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__BUILDER_HPP_
