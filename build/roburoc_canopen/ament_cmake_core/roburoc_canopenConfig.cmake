# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_roburoc_canopen_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED roburoc_canopen_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(roburoc_canopen_FOUND FALSE)
  elseif(NOT roburoc_canopen_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(roburoc_canopen_FOUND FALSE)
  endif()
  return()
endif()
set(_roburoc_canopen_CONFIG_INCLUDED TRUE)

# output package information
if(NOT roburoc_canopen_FIND_QUIETLY)
  message(STATUS "Found roburoc_canopen: 0.0.0 (${roburoc_canopen_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'roburoc_canopen' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${roburoc_canopen_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(roburoc_canopen_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${roburoc_canopen_DIR}/${_extra}")
endforeach()
