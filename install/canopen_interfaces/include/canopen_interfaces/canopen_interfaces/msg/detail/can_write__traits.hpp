// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from canopen_interfaces:msg/CANWrite.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__TRAITS_HPP_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "canopen_interfaces/msg/detail/can_write__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace canopen_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const CANWrite & msg,
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

  // member: node_id
  {
    out << "node_id: ";
    rosidl_generator_traits::value_to_yaml(msg.node_id, out);
    out << ", ";
  }

  // member: indices
  {
    if (msg.indices.size() == 0) {
      out << "indices: []";
    } else {
      out << "indices: [";
      size_t pending_items = msg.indices.size();
      for (auto item : msg.indices) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
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
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CANWrite & msg,
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

  // member: node_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "node_id: ";
    rosidl_generator_traits::value_to_yaml(msg.node_id, out);
    out << "\n";
  }

  // member: indices
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.indices.size() == 0) {
      out << "indices: []\n";
    } else {
      out << "indices:\n";
      for (auto item : msg.indices) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CANWrite & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace canopen_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use canopen_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const canopen_interfaces::msg::CANWrite & msg,
  std::ostream & out, size_t indentation = 0)
{
  canopen_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use canopen_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const canopen_interfaces::msg::CANWrite & msg)
{
  return canopen_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<canopen_interfaces::msg::CANWrite>()
{
  return "canopen_interfaces::msg::CANWrite";
}

template<>
inline const char * name<canopen_interfaces::msg::CANWrite>()
{
  return "canopen_interfaces/msg/CANWrite";
}

template<>
struct has_fixed_size<canopen_interfaces::msg::CANWrite>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<canopen_interfaces::msg::CANWrite>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<canopen_interfaces::msg::CANWrite>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_WRITE__TRAITS_HPP_
