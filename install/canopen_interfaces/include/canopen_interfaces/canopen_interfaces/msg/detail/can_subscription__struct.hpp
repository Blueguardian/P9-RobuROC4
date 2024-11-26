// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from canopen_interfaces:msg/CANSubscription.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__STRUCT_HPP_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__canopen_interfaces__msg__CANSubscription __attribute__((deprecated))
#else
# define DEPRECATED__canopen_interfaces__msg__CANSubscription __declspec(deprecated)
#endif

namespace canopen_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CANSubscription_
{
  using Type = CANSubscription_<ContainerAllocator>;

  explicit CANSubscription_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cobid = 0;
    }
  }

  explicit CANSubscription_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cobid = 0;
    }
  }

  // field types and members
  using _cobid_type =
    int16_t;
  _cobid_type cobid;
  using _data_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _data_type data;

  // setters for named parameter idiom
  Type & set__cobid(
    const int16_t & _arg)
  {
    this->cobid = _arg;
    return *this;
  }
  Type & set__data(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    canopen_interfaces::msg::CANSubscription_<ContainerAllocator> *;
  using ConstRawPtr =
    const canopen_interfaces::msg::CANSubscription_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::msg::CANSubscription_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::msg::CANSubscription_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__canopen_interfaces__msg__CANSubscription
    std::shared_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__canopen_interfaces__msg__CANSubscription
    std::shared_ptr<canopen_interfaces::msg::CANSubscription_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CANSubscription_ & other) const
  {
    if (this->cobid != other.cobid) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const CANSubscription_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CANSubscription_

// alias to use template instance with default allocator
using CANSubscription =
  canopen_interfaces::msg::CANSubscription_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__STRUCT_HPP_
