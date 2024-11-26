set(_AMENT_PACKAGE_NAME "RobuROC_sim")
set(RobuROC_sim_VERSION "0.0.0")
set(RobuROC_sim_MAINTAINER "ROB962 <es-24-rob-9-962@student.aau.dk>")
set(RobuROC_sim_BUILD_DEPENDS "sensor_msgs" "image_transport" "camera_info_manager" "realsense2_description" "vision_msgs" "velodyne_gazebo_plugins" "velodyne_description")
set(RobuROC_sim_BUILDTOOL_DEPENDS "ament_cmake" "ament_cmake_python")
set(RobuROC_sim_BUILD_EXPORT_DEPENDS "sensor_msgs" "image_transport" "camera_info_manager" "realsense2_description" "vision_msgs" "velodyne_gazebo_plugins" "velodyne_description")
set(RobuROC_sim_BUILDTOOL_EXPORT_DEPENDS )
set(RobuROC_sim_EXEC_DEPENDS "joint_state_publisher" "robot_state_publisher" "gazebo_ros" "xacro" "ros_gz_bridge" "rclpy" "std_msgs" "geometry_msgs" "realsense_gazebo_plugin" "sensor_msgs" "image_transport" "camera_info_manager" "realsense2_description" "vision_msgs" "velodyne_gazebo_plugins" "velodyne_description")
set(RobuROC_sim_TEST_DEPENDS "ament_lint_auto" "ament_lint_common")
set(RobuROC_sim_GROUP_DEPENDS )
set(RobuROC_sim_MEMBER_OF_GROUPS )
set(RobuROC_sim_DEPRECATED "")
set(RobuROC_sim_EXPORT_TAGS)
list(APPEND RobuROC_sim_EXPORT_TAGS "<build_type>ament_cmake</build_type>")