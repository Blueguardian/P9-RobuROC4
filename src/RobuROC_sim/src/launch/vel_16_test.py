import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    deskewing = LaunchConfiguration('deskewing')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        DeclareLaunchArgument(
            'deskewing', default_value='true',
            description='Enable lidar deskewing'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('velodyne_driver'), 'launch'),
                '/velodyne_driver_node-VLP16-launch.py']),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('velodyne_pointcloud'), 'launch'),
                '/velodyne_transform_node-VLP16-launch.py']),
        ),
        Node(
            package='rtabmap_odom',
            executable='icp_odometry',
            output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom',
                'deskewing': deskewing,
                'use_sim_time': use_sim_time,
            }],
            remappings=[
                ('scan_cloud', '/velodyne_points')
            ]
        )
    ])
