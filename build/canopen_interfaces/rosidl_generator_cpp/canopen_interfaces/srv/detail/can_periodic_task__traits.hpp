// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from canopen_interfaces:srv/CANPeriodicTask.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__TRAITS_HPP_
#define CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "canopen_interfaces/srv/detail/can_periodic_task__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace canopen_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const CANPeriodicTask_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: command
  {
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << ", ";
  }

  // member: cobid
  {
    out << "cobid: ";
    rosidl_generator_traits::value_to_yaml(msg.cobid, out);
    out << ", ";
  }

  // member: data
  {
    if (msg.data.size() == 0) {
      out << "data: []";
    } else {
      out << "data: [";
      size_t pending_items = msg.data.size();
      for (auto item : msg.data) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: period
  {
    out << "period: ";
    rosidl_generator_traits::value_to_yaml(msg.period, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CANPeriodicTask_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << "\n";
  }

  // member: cobid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cobid: ";
    rosidl_generator_traits::value_to_yaml(msg.cobid, out);
    out << "\n";
  }

  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.data.size() == 0) {
      out << "data: []\n";
    } else {
      out << "data:\n";
      for (auto item : msg.data) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: period
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "period: ";
    rosidl_generator_traits::value_to_yaml(msg.period, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CANPeriodicTask_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace canopen_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use canopen_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const canopen_interfaces::srv::CANPeriodicTask_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  canopen_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use canopen_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const canopen_interfaces::srv::CANPeriodicTask_Request & msg)
{
  return canopen_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<canopen_interfaces::srv::CANPeriodicTask_Request>()
{
  return "canopen_interfaces::srv::CANPeriodicTask_Request";
}

template<>
inline const char * name<canopen_interfaces::srv::CANPeriodicTask_Request>()
{
  return "canopen_interfaces/srv/CANPeriodicTask_Request";
}

template<>
struct has_fixed_size<canopen_interfaces::srv::CANPeriodicTask_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<canopen_interfaces::srv::CANPeriodicTask_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<canopen_interfaces::srv::CANPeriodicTask_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace canopen_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const CANPeriodicTask_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CANPeriodicTask_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CANPeriodicTask_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace canopen_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use canopen_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const canopen_interfaces::srv::CANPeriodicTask_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  canopen_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use canopen_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const canopen_interfaces::srv::CANPeriodicTask_Response & msg)
{
  return canopen_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<canopen_interfaces::srv::CANPeriodicTask_Response>()
{
  return "canopen_interfaces::srv::CANPeriodicTask_Response";
}

template<>
inline const char * name<canopen_interfaces::srv::CANPeriodicTask_Response>()
{
  return "canopen_interfaces/srv/CANPeriodicTask_Response";
}

template<>
struct has_fixed_size<canopen_interfaces::srv::CANPeriodicTask_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<canopen_interfaces::srv::CANPeriodicTask_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<canopen_interfaces::srv::CANPeriodicTask_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<canopen_interfaces::srv::CANPeriodicTask>()
{
  return "canopen_interfaces::srv::CANPeriodicTask";
}

template<>
inline const char * name<canopen_interfaces::srv::CANPeriodicTask>()
{
  return "canopen_interfaces/srv/CANPeriodicTask";
}

template<>
struct has_fixed_size<canopen_interfaces::srv::CANPeriodicTask>
  : std::integral_constant<
    bool,
    has_fixed_size<canopen_interfaces::srv::CANPeriodicTask_Request>::value &&
    has_fixed_size<canopen_interfaces::srv::CANPeriodicTask_Response>::value
  >
{
};

template<>
struct has_bounded_size<canopen_interfaces::srv::CANPeriodicTask>
  : std::integral_constant<
    bool,
    has_bounded_size<canopen_interfaces::srv::CANPeriodicTask_Request>::value &&
    has_bounded_size<canopen_interfaces::srv::CANPeriodicTask_Response>::value
  >
{
};

template<>
struct is_service<canopen_interfaces::srv::CANPeriodicTask>
  : std::true_type
{
};

template<>
struct is_service_request<canopen_interfaces::srv::CANPeriodicTask_Request>
  : std::true_type
{
};

template<>
struct is_service_response<canopen_interfaces::srv::CANPeriodicTask_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CANOPEN_INTERFACES__SRV__DETAIL__CAN_PERIODIC_TASK__TRAITS_HPP_
