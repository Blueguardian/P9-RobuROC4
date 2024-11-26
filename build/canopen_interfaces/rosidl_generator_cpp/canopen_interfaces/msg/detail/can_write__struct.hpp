// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from canopen_interfaces:msg/CANWrite.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__STRUCT_HPP_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__canopen_interfaces__msg__CANWrite __attribute__((deprecated))
#else
# define DEPRECATED__canopen_interfaces__msg__CANWrite __declspec(deprecated)
#endif

namespace canopen_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CANWrite_
{
  using Type = CANWrite_<ContainerAllocator>;

  explicit CANWrite_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = "";
      this->cobid = 0;
      this->node_id = 0;
    }
  }

  explicit CANWrite_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = "";
      this->cobid = 0;
      this->node_id = 0;
    }
  }

  // field types and members
  using _command_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _command_type command;
  using _cobid_type =
    int16_t;
  _cobid_type cobid;
  using _node_id_type =
    int8_t;
  _node_id_type node_id;
  using _indices_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _indices_type indices;
  using _data_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _data_type data;

  // setters for named parameter idiom
  Type & set__command(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->command = _arg;
    return *this;
  }
  Type & set__cobid(
    const int16_t & _arg)
  {
    this->cobid = _arg;
    return *this;
  }
  Type & set__node_id(
    const int8_t & _arg)
  {
    this->node_id = _arg;
    return *this;
  }
  Type & set__indices(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->indices = _arg;
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
    canopen_interfaces::msg::CANWrite_<ContainerAllocator> *;
  using ConstRawPtr =
    const canopen_interfaces::msg::CANWrite_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::msg::CANWrite_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::msg::CANWrite_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__canopen_interfaces__msg__CANWrite
    std::shared_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__canopen_interfaces__msg__CANWrite
    std::shared_ptr<canopen_interfaces::msg::CANWrite_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CANWrite_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    if (this->cobid != other.cobid) {
      return false;
    }
    if (this->node_id != other.node_id) {
      return false;
    }
    if (this->indices != other.indices) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const CANWrite_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CANWrite_

// alias to use template instance with default allocator
using CANWrite =
  canopen_interfaces::msg::CANWrite_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__STRUCT_HPP_
