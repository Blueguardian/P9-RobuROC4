import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        Node(
            package='rtabmap_slam',
            executable='rtabmap',
            output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom',
                'subscribe_depth': True,
                'subscribe_rgb': True,
                'subscribe_scan_cloud': True,
                'use_sim_time': use_sim_time,
                'RGBD/CreateOccupancyGrid': True,
            }],
            remappings=[
                ('rgb/image', '/camera1/camera1/color/image_raw'),
                ('depth/image', '/camera1/camera1/depth/image_rect_raw'),
                ('rgb/camera_info', '/camera1/camera1/color/camera_info'),
                ('scan_cloud', '/velodyne_points'),
                ('odom', '/odom'),
            ],
            arguments=['-d']  # Clear database
        ),
        Node(
            package='rtabmap_viz',
            executable='rtabmap_viz',
            output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom',
                'use_sim_time': use_sim_time,
            }],
            remappings=[
                ('scan_cloud', '/velodyne_points')
            ]
        )
    ])
