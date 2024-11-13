cmake_minimum_required(VERSION 3.8)
project(roburoc_controller)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/CANWrite.msg"
    "msg/CANSignal.msg"
    "msg/CANSubscribe.msg"
    "msg/CANSubscribe.msg"
    "msg/CANSubscription.msg"
    "srv/CANRead.srv"
    DEPENDENCIES std_msgs
    )
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

ament_python_install_package(scripts)

install(PROGRAMS
  scripts/robuROC_CTRL.py
  scripts/gamepad.py
  DESTINATION lib/${PROJECT_NAME}
)

install(
    DIRECTORY scripts/utils
    DESTINATION lib/${PROJECT_NAME}
)
ament_package()
