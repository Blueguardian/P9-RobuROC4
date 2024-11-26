// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from canopen_interfaces:msg/CANWrite.idl
// generated code does not contain a copyright notice
#include "canopen_interfaces/msg/detail/can_write__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"
// Member `indices`
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
canopen_interfaces__msg__CANWrite__init(canopen_interfaces__msg__CANWrite * msg)
{
  if (!msg) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__init(&msg->command)) {
    canopen_interfaces__msg__CANWrite__fini(msg);
    return false;
  }
  // cobid
  // node_id
  // indices
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->indices, 0)) {
    canopen_interfaces__msg__CANWrite__fini(msg);
    return false;
  }
  // data
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->data, 0)) {
    canopen_interfaces__msg__CANWrite__fini(msg);
    return false;
  }
  return true;
}

void
canopen_interfaces__msg__CANWrite__fini(canopen_interfaces__msg__CANWrite * msg)
{
  if (!msg) {
    return;
  }
  // command
  rosidl_runtime_c__String__fini(&msg->command);
  // cobid
  // node_id
  // indices
  rosidl_runtime_c__int32__Sequence__fini(&msg->indices);
  // data
  rosidl_runtime_c__int32__Sequence__fini(&msg->data);
}

bool
canopen_interfaces__msg__CANWrite__are_equal(const canopen_interfaces__msg__CANWrite * lhs, const canopen_interfaces__msg__CANWrite * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->command), &(rhs->command)))
  {
    return false;
  }
  // cobid
  if (lhs->cobid != rhs->cobid) {
    return false;
  }
  // node_id
  if (lhs->node_id != rhs->node_id) {
    return false;
  }
  // indices
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->indices), &(rhs->indices)))
  {
    return false;
  }
  // data
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->data), &(rhs->data)))
  {
    return false;
  }
  return true;
}

bool
canopen_interfaces__msg__CANWrite__copy(
  const canopen_interfaces__msg__CANWrite * input,
  canopen_interfaces__msg__CANWrite * output)
{
  if (!input || !output) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__copy(
      &(input->command), &(output->command)))
  {
    return false;
  }
  // cobid
  output->cobid = input->cobid;
  // node_id
  output->node_id = input->node_id;
  // indices
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->indices), &(output->indices)))
  {
    return false;
  }
  // data
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->data), &(output->data)))
  {
    return false;
  }
  return true;
}

canopen_interfaces__msg__CANWrite *
canopen_interfaces__msg__CANWrite__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__msg__CANWrite * msg = (canopen_interfaces__msg__CANWrite *)allocator.allocate(sizeof(canopen_interfaces__msg__CANWrite), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(canopen_interfaces__msg__CANWrite));
  bool success = canopen_interfaces__msg__CANWrite__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
canopen_interfaces__msg__CANWrite__destroy(canopen_interfaces__msg__CANWrite * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    canopen_interfaces__msg__CANWrite__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
canopen_interfaces__msg__CANWrite__Sequence__init(canopen_interfaces__msg__CANWrite__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__msg__CANWrite * data = NULL;

  if (size) {
    data = (canopen_interfaces__msg__CANWrite *)allocator.zero_allocate(size, sizeof(canopen_interfaces__msg__CANWrite), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = canopen_interfaces__msg__CANWrite__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        canopen_interfaces__msg__CANWrite__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
canopen_interfaces__msg__CANWrite__Sequence__fini(canopen_interfaces__msg__CANWrite__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      canopen_interfaces__msg__CANWrite__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

canopen_interfaces__msg__CANWrite__Sequence *
canopen_interfaces__msg__CANWrite__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__msg__CANWrite__Sequence * array = (canopen_interfaces__msg__CANWrite__Sequence *)allocator.allocate(sizeof(canopen_interfaces__msg__CANWrite__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = canopen_interfaces__msg__CANWrite__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
canopen_interfaces__msg__CANWrite__Sequence__destroy(canopen_interfaces__msg__CANWrite__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    canopen_interfaces__msg__CANWrite__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
canopen_interfaces__msg__CANWrite__Sequence__are_equal(const canopen_interfaces__msg__CANWrite__Sequence * lhs, const canopen_interfaces__msg__CANWrite__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!canopen_interfaces__msg__CANWrite__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
canopen_interfaces__msg__CANWrite__Sequence__copy(
  const canopen_interfaces__msg__CANWrite__Sequence * input,
  canopen_interfaces__msg__CANWrite__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(canopen_interfaces__msg__CANWrite);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    canopen_interfaces__msg__CANWrite * data =
      (canopen_interfaces__msg__CANWrite *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!canopen_interfaces__msg__CANWrite__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          canopen_interfaces__msg__CANWrite__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!canopen_interfaces__msg__CANWrite__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
