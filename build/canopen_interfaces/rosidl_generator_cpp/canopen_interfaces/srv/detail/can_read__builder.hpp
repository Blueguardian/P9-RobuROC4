// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from canopen_interfaces:srv/CANRead.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_READ__BUILDER_HPP_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_READ__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "canopen_interfaces/srv/detail/can_read__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace canopen_interfaces
{

namespace srv
{

namespace builder
{

class Init_CANRead_Request_indices
{
public:
  explicit Init_CANRead_Request_indices(::canopen_interfaces::srv::CANRead_Request & msg)
  : msg_(msg)
  {}
  ::canopen_interfaces::srv::CANRead_Request indices(::canopen_interfaces::srv::CANRead_Request::_indices_type arg)
  {
    msg_.indices = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::srv::CANRead_Request msg_;
};

class Init_CANRead_Request_node_id
{
public:
  explicit Init_CANRead_Request_node_id(::canopen_interfaces::srv::CANRead_Request & msg)
  : msg_(msg)
  {}
  Init_CANRead_Request_indices node_id(::canopen_interfaces::srv::CANRead_Request::_node_id_type arg)
  {
    msg_.node_id = std::move(arg);
    return Init_CANRead_Request_indices(msg_);
  }

private:
  ::canopen_interfaces::srv::CANRead_Request msg_;
};

class Init_CANRead_Request_cobid
{
public:
  explicit Init_CANRead_Request_cobid(::canopen_interfaces::srv::CANRead_Request & msg)
  : msg_(msg)
  {}
  Init_CANRead_Request_node_id cobid(::canopen_interfaces::srv::CANRead_Request::_cobid_type arg)
  {
    msg_.cobid = std::move(arg);
    return Init_CANRead_Request_node_id(msg_);
  }

private:
  ::canopen_interfaces::srv::CANRead_Request msg_;
};

class Init_CANRead_Request_command
{
public:
  Init_CANRead_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CANRead_Request_cobid command(::canopen_interfaces::srv::CANRead_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return Init_CANRead_Request_cobid(msg_);
  }

private:
  ::canopen_interfaces::srv::CANRead_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::srv::CANRead_Request>()
{
  return canopen_interfaces::srv::builder::Init_CANRead_Request_command();
}

}  // namespace canopen_interfaces


namespace canopen_interfaces
{

namespace srv
{

namespace builder
{

class Init_CANRead_Response_success
{
public:
  explicit Init_CANRead_Response_success(::canopen_interfaces::srv::CANRead_Response & msg)
  : msg_(msg)
  {}
  ::canopen_interfaces::srv::CANRead_Response success(::canopen_interfaces::srv::CANRead_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::srv::CANRead_Response msg_;
};

class Init_CANRead_Response_data
{
public:
  explicit Init_CANRead_Response_data(::canopen_interfaces::srv::CANRead_Response & msg)
  : msg_(msg)
  {}
  Init_CANRead_Response_success data(::canopen_interfaces::srv::CANRead_Response::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_CANRead_Response_success(msg_);
  }

private:
  ::canopen_interfaces::srv::CANRead_Response msg_;
};

class Init_CANRead_Response_indices
{
public:
  Init_CANRead_Response_indices()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CANRead_Response_data indices(::canopen_interfaces::srv::CANRead_Response::_indices_type arg)
  {
    msg_.indices = std::move(arg);
    return Init_CANRead_Response_data(msg_);
  }

private:
  ::canopen_interfaces::srv::CANRead_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::srv::CANRead_Response>()
{
  return canopen_interfaces::srv::builder::Init_CANRead_Response_indices();
}

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_READ__BUILDER_HPP_