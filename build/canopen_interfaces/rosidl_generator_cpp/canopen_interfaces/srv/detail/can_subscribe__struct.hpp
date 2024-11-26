// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from canopen_interfaces:srv/CANSubscribe.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_SUBSCRIBE__STRUCT_HPP_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_SUBSCRIBE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__canopen_interfaces__srv__CANSubscribe_Request __attribute__((deprecated))
#else
# define DEPRECATED__canopen_interfaces__srv__CANSubscribe_Request __declspec(deprecated)
#endif

namespace canopen_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CANSubscribe_Request_
{
  using Type = CANSubscribe_Request_<ContainerAllocator>;

  explicit CANSubscribe_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = "";
      this->cobid = 0;
    }
  }

  explicit CANSubscribe_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = "";
      this->cobid = 0;
    }
  }

  // field types and members
  using _command_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _command_type command;
  using _cobid_type =
    int16_t;
  _cobid_type cobid;

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

  // constant declarations

  // pointer types
  using RawPtr =
    canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__canopen_interfaces__srv__CANSubscribe_Request
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__canopen_interfaces__srv__CANSubscribe_Request
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CANSubscribe_Request_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    if (this->cobid != other.cobid) {
      return false;
    }
    return true;
  }
  bool operator!=(const CANSubscribe_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CANSubscribe_Request_

// alias to use template instance with default allocator
using CANSubscribe_Request =
  canopen_interfaces::srv::CANSubscribe_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace canopen_interfaces


#ifndef _WIN32
# define DEPRECATED__canopen_interfaces__srv__CANSubscribe_Response __attribute__((deprecated))
#else
# define DEPRECATED__canopen_interfaces__srv__CANSubscribe_Response __declspec(deprecated)
#endif

namespace canopen_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CANSubscribe_Response_
{
  using Type = CANSubscribe_Response_<ContainerAllocator>;

  explicit CANSubscribe_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit CANSubscribe_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__canopen_interfaces__srv__CANSubscribe_Response
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__canopen_interfaces__srv__CANSubscribe_Response
    std::shared_ptr<canopen_interfaces::srv::CANSubscribe_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CANSubscribe_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const CANSubscribe_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CANSubscribe_Response_

// alias to use template instance with default allocator
using CANSubscribe_Response =
  canopen_interfaces::srv::CANSubscribe_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace canopen_interfaces

namespace canopen_interfaces
{

namespace srv
{

struct CANSubscribe
{
  using Request = canopen_interfaces::srv::CANSubscribe_Request;
  using Response = canopen_interfaces::srv::CANSubscribe_Response;
};

}  // namespace srv

}  // namespace canopen_interfaces

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_SUBSCRIBE__STRUCT_HPP_
