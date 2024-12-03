from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

"""
Attempt at fusing data from the lidar and a single rgbd camera for odometry and slam.
"""

def generate_launch_description():
    # Launch Arguments
    use_sim_time = LaunchConfiguration('use_sim_time')
    deskewing = LaunchConfiguration('deskewing')

    return LaunchDescription([

        # Launch arguments
        DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        DeclareLaunchArgument(
            'deskewing', default_value='true',
            description='Enable LiDAR deskewing'),

        # LiDAR Nodes
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

        # RGB-D Camera Nodes

        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([os.path.join(
        #         get_package_share_directory('realsense2_camera'), 'launch'),
        #         '/rs_launch.py']),
        # ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('RobuROC_sim'), 'launch'),'/dual_camera.launch.py']), launch_arguments={'serial_no1': "'034422070675'",
                               'camera_name': 'camera1',
                               'camera_namespace': 'camera1',
                               'serial_no2': "'829212072207'",
                               'camera_name': 'camera2',
                               'camera_namespace': 'camera2'}.items()
        ),




        # RTAB-Map Odometry for LiDAR
        Node(
            package='rtabmap_odom', executable='icp_odometry', output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom_lidar',
                'use_sim_time': use_sim_time,
                'deskewing': deskewing,
                # ICP parameters
                'Icp/PointToPlane': 'true',
                'Icp/Iterations': '10',
                'Icp/VoxelSize': '0.1',
                'Icp/Epsilon': '0.001',
                'Icp/MaxCorrespondenceDistance': '1'
            }],
            remappings=[
                ('scan_cloud', '/velodyne_points'),
                ('odom', '/odom_lidar')
            ]),

        # RTAB-Map Odometry for RGB-D
        Node(
            package='rtabmap_odom', executable='rgbd_odometry', output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom_camera',
                'use_sim_time': use_sim_time,
                # RGB-D odometry parameters
                'RGBD/LinearUpdate': '0.1',
                'RGBD/AngularUpdate': '0.05',
                'approx_sync': False,
            }],
            remappings=[
                ('rgb/image', '/camera1/camera1/color/image_raw'),
                ('rgb/camera_info', '/camera1/camera1/color/camera_info'),
                ('depth/image', '/camera1/camera1/depth/image_rect_raw'),
                ('odom', '/odom_camera')
            ]),

        # Unified RTAB-Map SLAM Node
        Node(
            package='rtabmap_slam', executable='rtabmap', output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom',  # Unified odometry frame
                'subscribe_scan_cloud': True,

                # 'subscribe_rgb': True,             #added

                'subscribe_depth': True,
                # 'approx_sync': False,
                'approx_sync': True,
                'sync_queue_size': 30,
                'qos': 1,
                'use_sim_time': use_sim_time,
                # RTAB-Map parameters
                'RGBD/LinearUpdate': '0.1',
                'RGBD/AngularUpdate': '0.05',
                'RGBD/CreateOccupancyGrid': 'true',
                'RGBD/ProximityBySpace': 'true',
                'RGBD/ProximityMaxGraphDepth': '0',
                'Mem/NotLinkedNodesKept': 'false',
                # 'Icp/PointToPlane': 'true',
                # 'Icp/Iterations': '10',
                # 'Icp/VoxelSize': '0.1'
            }],
            remappings=[
                ('scan_cloud', '/velodyne_points'),
                ('rgb/image', '/camera1/camera1/color/image_raw'),
                ('rgb/camera_info', '/camera1/camera1/color/camera_info'),
                ('depth/image', '/camera1/camera1/depth/image_rect_raw')
            ],
            arguments=['d','--database_path', '/path/to/unified_rtabmap.db']    # shared db for all sensor data.
        ),

        # Visualization
        Node(
            package='rtabmap_viz', executable='rtabmap_viz', output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom',
                'subscribe_odom_info': True,
                'subscribe_scan_cloud': True,
                'use_sim_time': use_sim_time
            }],
            remappings=[
                ('scan_cloud', '/velodyne_points'),
                ('rgb/image', '/camera1/camera1/color/image_raw'),
                ('depth/image', '/camera1/camera1/depth/image_rect_raw')
            ]),
    ])
