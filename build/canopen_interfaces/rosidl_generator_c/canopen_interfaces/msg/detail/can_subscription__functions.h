// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from canopen_interfaces:msg/CANSubscription.idl
// generated code does not contain a copyright notice

#ifndef CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__FUNCTIONS_H_
#define CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "canopen_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "canopen_interfaces/msg/detail/can_subscription__struct.h"

/// Initialize msg/CANSubscription message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * canopen_interfaces__msg__CANSubscription
 * )) before or use
 * canopen_interfaces__msg__CANSubscription__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
bool
canopen_interfaces__msg__CANSubscription__init(canopen_interfaces__msg__CANSubscription * msg);

/// Finalize msg/CANSubscription message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
void
canopen_interfaces__msg__CANSubscription__fini(canopen_interfaces__msg__CANSubscription * msg);

/// Create msg/CANSubscription message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * canopen_interfaces__msg__CANSubscription__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
canopen_interfaces__msg__CANSubscription *
canopen_interfaces__msg__CANSubscription__create();

/// Destroy msg/CANSubscription message.
/**
 * It calls
 * canopen_interfaces__msg__CANSubscription__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
void
canopen_interfaces__msg__CANSubscription__destroy(canopen_interfaces__msg__CANSubscription * msg);

/// Check for msg/CANSubscription message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
bool
canopen_interfaces__msg__CANSubscription__are_equal(const canopen_interfaces__msg__CANSubscription * lhs, const canopen_interfaces__msg__CANSubscription * rhs);

/// Copy a msg/CANSubscription message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
bool
canopen_interfaces__msg__CANSubscription__copy(
  const canopen_interfaces__msg__CANSubscription * input,
  canopen_interfaces__msg__CANSubscription * output);

/// Initialize array of msg/CANSubscription messages.
/**
 * It allocates the memory for the number of elements and calls
 * canopen_interfaces__msg__CANSubscription__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
bool
canopen_interfaces__msg__CANSubscription__Sequence__init(canopen_interfaces__msg__CANSubscription__Sequence * array, size_t size);

/// Finalize array of msg/CANSubscription messages.
/**
 * It calls
 * canopen_interfaces__msg__CANSubscription__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
void
canopen_interfaces__msg__CANSubscription__Sequence__fini(canopen_interfaces__msg__CANSubscription__Sequence * array);

/// Create array of msg/CANSubscription messages.
/**
 * It allocates the memory for the array and calls
 * canopen_interfaces__msg__CANSubscription__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
canopen_interfaces__msg__CANSubscription__Sequence *
canopen_interfaces__msg__CANSubscription__Sequence__create(size_t size);

/// Destroy array of msg/CANSubscription messages.
/**
 * It calls
 * canopen_interfaces__msg__CANSubscription__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
void
canopen_interfaces__msg__CANSubscription__Sequence__destroy(canopen_interfaces__msg__CANSubscription__Sequence * array);

/// Check for msg/CANSubscription message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
bool
canopen_interfaces__msg__CANSubscription__Sequence__are_equal(const canopen_interfaces__msg__CANSubscription__Sequence * lhs, const canopen_interfaces__msg__CANSubscription__Sequence * rhs);

/// Copy an array of msg/CANSubscription messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_canopen_interfaces
bool
canopen_interfaces__msg__CANSubscription__Sequence__copy(
  const canopen_interfaces__msg__CANSubscription__Sequence * input,
  canopen_interfaces__msg__CANSubscription__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // CANOPEN_INTERFACES__MSG__DETAIL__CAN_SUBSCRIPTION__FUNCTIONS_H_
