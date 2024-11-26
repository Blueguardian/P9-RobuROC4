// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from canopen_interfaces:srv/CANPeriodicTask.idl
// generated code does not contain a copyright notice
#include "canopen_interfaces/srv/detail/can_periodic_task__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
canopen_interfaces__srv__CANPeriodicTask_Request__init(canopen_interfaces__srv__CANPeriodicTask_Request * msg)
{
  if (!msg) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__init(&msg->command)) {
    canopen_interfaces__srv__CANPeriodicTask_Request__fini(msg);
    return false;
  }
  // cobid
  // data
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->data, 0)) {
    canopen_interfaces__srv__CANPeriodicTask_Request__fini(msg);
    return false;
  }
  // period
  return true;
}

void
canopen_interfaces__srv__CANPeriodicTask_Request__fini(canopen_interfaces__srv__CANPeriodicTask_Request * msg)
{
  if (!msg) {
    return;
  }
  // command
  rosidl_runtime_c__String__fini(&msg->command);
  // cobid
  // data
  rosidl_runtime_c__int32__Sequence__fini(&msg->data);
  // period
}

bool
canopen_interfaces__srv__CANPeriodicTask_Request__are_equal(const canopen_interfaces__srv__CANPeriodicTask_Request * lhs, const canopen_interfaces__srv__CANPeriodicTask_Request * rhs)
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
  // data
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->data), &(rhs->data)))
  {
    return false;
  }
  // period
  if (lhs->period != rhs->period) {
    return false;
  }
  return true;
}

bool
canopen_interfaces__srv__CANPeriodicTask_Request__copy(
  const canopen_interfaces__srv__CANPeriodicTask_Request * input,
  canopen_interfaces__srv__CANPeriodicTask_Request * output)
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
  // data
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->data), &(output->data)))
  {
    return false;
  }
  // period
  output->period = input->period;
  return true;
}

canopen_interfaces__srv__CANPeriodicTask_Request *
canopen_interfaces__srv__CANPeriodicTask_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__srv__CANPeriodicTask_Request * msg = (canopen_interfaces__srv__CANPeriodicTask_Request *)allocator.allocate(sizeof(canopen_interfaces__srv__CANPeriodicTask_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(canopen_interfaces__srv__CANPeriodicTask_Request));
  bool success = canopen_interfaces__srv__CANPeriodicTask_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
canopen_interfaces__srv__CANPeriodicTask_Request__destroy(canopen_interfaces__srv__CANPeriodicTask_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    canopen_interfaces__srv__CANPeriodicTask_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__init(canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__srv__CANPeriodicTask_Request * data = NULL;

  if (size) {
    data = (canopen_interfaces__srv__CANPeriodicTask_Request *)allocator.zero_allocate(size, sizeof(canopen_interfaces__srv__CANPeriodicTask_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = canopen_interfaces__srv__CANPeriodicTask_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        canopen_interfaces__srv__CANPeriodicTask_Request__fini(&data[i - 1]);
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
canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__fini(canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * array)
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
      canopen_interfaces__srv__CANPeriodicTask_Request__fini(&array->data[i]);
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

canopen_interfaces__srv__CANPeriodicTask_Request__Sequence *
canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * array = (canopen_interfaces__srv__CANPeriodicTask_Request__Sequence *)allocator.allocate(sizeof(canopen_interfaces__srv__CANPeriodicTask_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__destroy(canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__are_equal(const canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * lhs, const canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!canopen_interfaces__srv__CANPeriodicTask_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
canopen_interfaces__srv__CANPeriodicTask_Request__Sequence__copy(
  const canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * input,
  canopen_interfaces__srv__CANPeriodicTask_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(canopen_interfaces__srv__CANPeriodicTask_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    canopen_interfaces__srv__CANPeriodicTask_Request * data =
      (canopen_interfaces__srv__CANPeriodicTask_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!canopen_interfaces__srv__CANPeriodicTask_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          canopen_interfaces__srv__CANPeriodicTask_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!canopen_interfaces__srv__CANPeriodicTask_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
canopen_interfaces__srv__CANPeriodicTask_Response__init(canopen_interfaces__srv__CANPeriodicTask_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
canopen_interfaces__srv__CANPeriodicTask_Response__fini(canopen_interfaces__srv__CANPeriodicTask_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
canopen_interfaces__srv__CANPeriodicTask_Response__are_equal(const canopen_interfaces__srv__CANPeriodicTask_Response * lhs, const canopen_interfaces__srv__CANPeriodicTask_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
canopen_interfaces__srv__CANPeriodicTask_Response__copy(
  const canopen_interfaces__srv__CANPeriodicTask_Response * input,
  canopen_interfaces__srv__CANPeriodicTask_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

canopen_interfaces__srv__CANPeriodicTask_Response *
canopen_interfaces__srv__CANPeriodicTask_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__srv__CANPeriodicTask_Response * msg = (canopen_interfaces__srv__CANPeriodicTask_Response *)allocator.allocate(sizeof(canopen_interfaces__srv__CANPeriodicTask_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(canopen_interfaces__srv__CANPeriodicTask_Response));
  bool success = canopen_interfaces__srv__CANPeriodicTask_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
canopen_interfaces__srv__CANPeriodicTask_Response__destroy(canopen_interfaces__srv__CANPeriodicTask_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    canopen_interfaces__srv__CANPeriodicTask_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__init(canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__srv__CANPeriodicTask_Response * data = NULL;

  if (size) {
    data = (canopen_interfaces__srv__CANPeriodicTask_Response *)allocator.zero_allocate(size, sizeof(canopen_interfaces__srv__CANPeriodicTask_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = canopen_interfaces__srv__CANPeriodicTask_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        canopen_interfaces__srv__CANPeriodicTask_Response__fini(&data[i - 1]);
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
canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__fini(canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * array)
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
      canopen_interfaces__srv__CANPeriodicTask_Response__fini(&array->data[i]);
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

canopen_interfaces__srv__CANPeriodicTask_Response__Sequence *
canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * array = (canopen_interfaces__srv__CANPeriodicTask_Response__Sequence *)allocator.allocate(sizeof(canopen_interfaces__srv__CANPeriodicTask_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__destroy(canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__are_equal(const canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * lhs, const canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!canopen_interfaces__srv__CANPeriodicTask_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
canopen_interfaces__srv__CANPeriodicTask_Response__Sequence__copy(
  const canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * input,
  canopen_interfaces__srv__CANPeriodicTask_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(canopen_interfaces__srv__CANPeriodicTask_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    canopen_interfaces__srv__CANPeriodicTask_Response * data =
      (canopen_interfaces__srv__CANPeriodicTask_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!canopen_interfaces__srv__CANPeriodicTask_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          canopen_interfaces__srv__CANPeriodicTask_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!canopen_interfaces__srv__CANPeriodicTask_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
