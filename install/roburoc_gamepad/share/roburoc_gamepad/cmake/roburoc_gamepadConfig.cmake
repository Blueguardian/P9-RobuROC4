# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_roburoc_gamepad_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED roburoc_gamepad_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(roburoc_gamepad_FOUND FALSE)
  elseif(NOT roburoc_gamepad_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(roburoc_gamepad_FOUND FALSE)
  endif()
  return()
endif()
set(_roburoc_gamepad_CONFIG_INCLUDED TRUE)

# output package information
if(NOT roburoc_gamepad_FIND_QUIETLY)
  message(STATUS "Found roburoc_gamepad: 0.0.0 (${roburoc_gamepad_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'roburoc_gamepad' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${roburoc_gamepad_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(roburoc_gamepad_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${roburoc_gamepad_DIR}/${_extra}")
endforeach()
