// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from canopen_interfaces:msg/CANSubscription.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__BUILDER_HPP_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "canopen_interfaces/msg/detail/can_subscription__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace canopen_interfaces
{

namespace msg
{

namespace builder
{

class Init_CANSubscription_data
{
public:
  explicit Init_CANSubscription_data(::canopen_interfaces::msg::CANSubscription & msg)
  : msg_(msg)
  {}
  ::canopen_interfaces::msg::CANSubscription data(::canopen_interfaces::msg::CANSubscription::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::canopen_interfaces::msg::CANSubscription msg_;
};

class Init_CANSubscription_cobid
{
public:
  Init_CANSubscription_cobid()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CANSubscription_data cobid(::canopen_interfaces::msg::CANSubscription::_cobid_type arg)
  {
    msg_.cobid = std::move(arg);
    return Init_CANSubscription_data(msg_);
  }

private:
  ::canopen_interfaces::msg::CANSubscription msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::canopen_interfaces::msg::CANSubscription>()
{
  return canopen_interfaces::msg::builder::Init_CANSubscription_cobid();
}

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__BUILDER_HPP_
