// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from canopen_interfaces:srv/CANConnection.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_CONNECTION__BUILDER_HPP_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_CONNECTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "canopen_interfaces/srv/detail/can_connection__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace canopen_interfaces
{

namespace srv
{

namespace builder
{

class Init_CANConnection_Request_command
{
public:
  Init_CANConnection_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::canopen_interfaces::srv::CANConnection_Request command(::canopen_interfaces::srv::CANConnection_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::srv::CANConnection_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::srv::CANConnection_Request>()
{
  return canopen_interfaces::srv::builder::Init_CANConnection_Request_command();
}

}  // namespace canopen_interfaces


namespace canopen_interfaces
{

namespace srv
{

namespace builder
{

class Init_CANConnection_Response_success
{
public:
  explicit Init_CANConnection_Response_success(::canopen_interfaces::srv::CANConnection_Response & msg)
  : msg_(msg)
  {}
  ::canopen_interfaces::srv::CANConnection_Response success(::canopen_interfaces::srv::CANConnection_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::srv::CANConnection_Response msg_;
};

class Init_CANConnection_Response_node_list
{
public:
  Init_CANConnection_Response_node_list()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CANConnection_Response_success node_list(::canopen_interfaces::srv::CANConnection_Response::_node_list_type arg)
  {
    msg_.node_list = std::move(arg);
    return Init_CANConnection_Response_success(msg_);
  }

private:
  ::canopen_interfaces::srv::CANConnection_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::srv::CANConnection_Response>()
{
  return canopen_interfaces::srv::builder::Init_CANConnection_Response_node_list();
}

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_CONNECTION__BUILDER_HPP_
