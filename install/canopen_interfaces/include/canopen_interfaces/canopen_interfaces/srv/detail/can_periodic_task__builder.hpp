// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from canopen_interfaces:srv/CANPeriodicTask.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__BUILDER_HPP_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "canopen_interfaces/srv/detail/can_periodic_task__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace canopen_interfaces
{

namespace srv
{

namespace builder
{

class Init_CANPeriodicTask_Request_period
{
public:
  explicit Init_CANPeriodicTask_Request_period(::canopen_interfaces::srv::CANPeriodicTask_Request & msg)
  : msg_(msg)
  {}
  ::canopen_interfaces::srv::CANPeriodicTask_Request period(::canopen_interfaces::srv::CANPeriodicTask_Request::_period_type arg)
  {
    msg_.period = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::srv::CANPeriodicTask_Request msg_;
};

class Init_CANPeriodicTask_Request_data
{
public:
  explicit Init_CANPeriodicTask_Request_data(::canopen_interfaces::srv::CANPeriodicTask_Request & msg)
  : msg_(msg)
  {}
  Init_CANPeriodicTask_Request_period data(::canopen_interfaces::srv::CANPeriodicTask_Request::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_CANPeriodicTask_Request_period(msg_);
  }

private:
  ::canopen_interfaces::srv::CANPeriodicTask_Request msg_;
};

class Init_CANPeriodicTask_Request_cobid
{
public:
  explicit Init_CANPeriodicTask_Request_cobid(::canopen_interfaces::srv::CANPeriodicTask_Request & msg)
  : msg_(msg)
  {}
  Init_CANPeriodicTask_Request_data cobid(::canopen_interfaces::srv::CANPeriodicTask_Request::_cobid_type arg)
  {
    msg_.cobid = std::move(arg);
    return Init_CANPeriodicTask_Request_data(msg_);
  }

private:
  ::canopen_interfaces::srv::CANPeriodicTask_Request msg_;
};

class Init_CANPeriodicTask_Request_command
{
public:
  Init_CANPeriodicTask_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CANPeriodicTask_Request_cobid command(::canopen_interfaces::srv::CANPeriodicTask_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return Init_CANPeriodicTask_Request_cobid(msg_);
  }

private:
  ::canopen_interfaces::srv::CANPeriodicTask_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::srv::CANPeriodicTask_Request>()
{
  return canopen_interfaces::srv::builder::Init_CANPeriodicTask_Request_command();
}

}  // namespace canopen_interfaces


namespace canopen_interfaces
{

namespace srv
{

namespace builder
{

class Init_CANPeriodicTask_Response_success
{
public:
  Init_CANPeriodicTask_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::canopen_interfaces::srv::CANPeriodicTask_Response success(::canopen_interfaces::srv::CANPeriodicTask_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::srv::CANPeriodicTask_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::srv::CANPeriodicTask_Response>()
{
  return canopen_interfaces::srv::builder::Init_CANPeriodicTask_Response_success();
}

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__BUILDER_HPP_
