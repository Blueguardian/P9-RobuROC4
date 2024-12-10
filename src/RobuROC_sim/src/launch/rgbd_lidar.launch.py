# Program dedicated to launch 2 realsense cameras. D405 were tested!
# (Please note that this program can manage maximum 4 depth cameras)

# Program modified by: Adrian Ricardez (https://github.com/adricort)
# Date: 07.07.2023
# Deutsches Zentrum für Luft- und Raumfahrt

# Requirements:

# Be sure that you did the build on your rtabmap workspace with the -DRTABMAP_SYNC_MULTI_RGBD=ON parameter.

# Launching the 2 realsense cameras (change your serial numbers):
#   $ ros2 launch realsense2_camera rs_multi_camera_launch.py pointcloud.enable1:=true pointcloud.enable2:=true filters:=colorizer align_depth:=true serial_no1:=_128422271521 serial_no2:=_128422272518

# Running the static publishers depending on the position of your cameras:
#   $ ros2 run tf2_ros static_transform_publisher --x 0.039 --y 0 --z 0 --yaw 0 --pitch 0 --roll 1.5708 --frame-id base_link --child-frame-id camera1_link
#   $ ros2 run tf2_ros static_transform_publisher --x -0 --y 0 --z 0.02 --yaw 1.5708 --pitch -1.5708 --roll 0 --frame-id base_link --child-frame-id camera2_link

#   $ ros2 launch rtabmap_examples rtabmap_D405x2.launch.py

# You should be able to visualize now, with the right rviz config, the camera's SLAM
# Have fun!

import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # config_rviz = os.path.join(
    #     get_package_share_directory('rtabmap_examples'), 'launch', 'config', 'slam_D405x2_config.rviz')
    #
    # rviz_node = launch_ros.actions.Node(
    #     package='rviz2', executable='rviz2', output='screen',
    #     arguments=[["-d"], [config_rviz]]
    # )

    # Sync nodes
    # use_sim_time = LaunchConfiguration('use_sim_time')
    # deskewing = LaunchConfiguration('deskewing')

            # Nodes to launch
    Driver_vel = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('velodyne_driver'), 'launch'),
                '/velodyne_driver_node-VLP16-launch.py']),
        )
    Pointcloud_vel = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('velodyne_pointcloud'), 'launch'),
                '/velodyne_transform_node-VLP16-launch.py']),
        )

    rgbd_sync1_node = launch_ros.actions.Node(
        package='rtabmap_sync', executable='rgbd_sync', name='rgbd_sync1', output="screen",
        parameters=[{
            "approx_sync": False
        }],
        remappings=[
            # ("rgb/image", '/camera1/color/image_rect_raw'),
            # ("depth/image", '/camera1/depth/image_rect_raw'),
            # ("rgb/camera_info", '/camera1/color/camera_info'),
            # ("rgbd_image", 'rgbd_image')],
            ("rgb/image", "camera1/color/image_raw"),
            ("depth/image", "camera1/depth/image_rect_raw"),
            ("rgb/camera_info", "camera1/color/camera_info"),
            ("rgbd_image", 'rgbd_image')],
        namespace='camera1'
        # namespace='camera1'
    )

    rgbd_sync2_node = launch_ros.actions.Node(
        package='rtabmap_sync', executable='rgbd_sync', name='rgbd_sync2', output="screen",
        parameters=[{
            "approx_sync": False
        }],
        remappings=[
            # ("rgb/image", '/camera2/color/image_rect_raw'),
            # ("depth/image", '/camera2/depth/image_rect_raw'),
            # ("rgb/camera_info", '/camera2/color/camera_info'),
            # ("rgbd_image", 'rgbd_image')],
            ("rgb/image", "camera2/color/image_raw"),
            ("depth/image", "camera2/depth/image_rect_raw"),
            ("rgb/camera_info", "camera2/color/camera_info"),
            ("rgbd_image", 'rgbd_image')],
        namespace='camera2'
    # namespace ='camera2'
    )

    # RGB-D odometry
    rgbd_odometry_node = launch_ros.actions.Node(
        package='rtabmap_odom', executable='rgbd_odometry', output="screen",
        parameters=[{
            "frame_id": 'base_link',
            "odom_frame_id": 'odom',
            "publish_tf": True,
            "approx_sync": True,
            "subscribe_rgbd": True,
            # "subscribe_scan_cloud": True

            # "subscribe_imu" : True,
            'use_sim_time': False,
            # RGB-D odometry parameters
            'RGBD/LinearUpdate': '0.1',
            'RGBD/AngularUpdate': '0.05',
        }],
        remappings=[
            ("rgbd_image", '/camera1/rgbd_image'),
            # ("rgbd_image", '/camera1/rgbd_image'),
            ('odom', '/odom'),
            # ('imu','/imu/data'),
            ],

        arguments=["--delete_db_on_start", ''],
        prefix='',
        namespace='rtabmap'
    )

    # Lidar
    scan_cloud =launch_ros.actions.Node(
            package='rtabmap_odom', executable='icp_odometry', output='screen',
            parameters=[{
              'frame_id':'base_link',
              'odom_frame_id':'odom',
              'wait_for_transform':0.2,
              'expected_update_rate':15.0,
              'deskewing':False,
              'use_sim_time':False,
              # RTAB-Map's internal parameters are strings:
              'Icp/PointToPlane': 'true',
              'Icp/Iterations': '10',
              'Icp/VoxelSize': '0.1',
              'Icp/Epsilon': '0.001',
              'Icp/PointToPlaneK': '20',
              'Icp/PointToPlaneRadius': '0',
              'Icp/MaxTranslation': '2',
              'Icp/MaxCorrespondenceDistance': '1',
              'Icp/Strategy': '1',
              'Icp/OutlierRatio': '0.7',
              'Icp/CorrespondenceRatio': '0.01',
              'Odom/ScanKeyFrameThr': '0.4',
              'OdomF2M/ScanSubtractRadius': '0.1',
              'OdomF2M/ScanMaxSize': '15000',
              'OdomF2M/BundleAdjustment': 'false'
            }],
            remappings=[
              ('scan_cloud', '/velodyne_points'),
              ('scan', 'dummy1'),
              ('odom', '/odom'),
            ])
    
    # SLAM
    slam_node = launch_ros.actions.Node(
        package='rtabmap_slam', executable='rtabmap', output="screen",
        parameters=[{
            "rgbd_cameras": 2,
            "subscribe_depth": False,
            "subscribe_rgbd": True,
            # "subscribe_rgb": True,
            'subscribe_scan_cloud':True,
            "subscribe_odom_info": True,
            'odom_frame_id': 'odom',
            "frame_id": 'base_link',
            "map_frame_id": 'map',
            "publish_tf": True,
            "database_path": '~/.ros/rtabmap.db',
            "approx_sync": True,
            "Mem/IncrementalMemory": "true",
            "Mem/InitWMWithAllNodes": "true"
        }],
        remappings=[
            ("rgbd_image0", '/camera1/rgbd_image'),
            ("rgbd_image1", '/camera2/rgbd_image'),
            # ("rgbd_image0", '/camera1/rgbd_image'),
            # ("rgbd_image1", '/camera2/rgbd_image'),
            ("odom", 'odom'),
            ('scan_cloud', '/velodyne_points')],
        arguments=["--delete_db_on_start"],
        prefix='',
        namespace='rtabmap'
    )

    voxelcloud1_node = launch_ros.actions.Node(
        package='rtabmap_util', executable='point_cloud_xyzrgb', name='point_cloud_xyzrgb1', output='screen',
        parameters=[{
            "approx_sync": True,
        }],
        remappings=[
            # ('rgb/image', '/camera1/color/image_rect_raw'),
            # ('depth/image', '/camera1/depth/image_rect_raw'),
            # ('rgb/camera_info', '/camera1/color/camera_info'),
            ("rgb/image", "/camera1/camera1/color/image_raw"),
            ("depth/image", "/camera1/camera1/depth/image_rect_raw"),
            ("rgb/camera_info", "/camera1/camera1/color/camera_info"),
            ('rgbd_image', 'rgbd_image'),
            ('cloud', 'voxel_cloud1')]
    )

    voxelcloud2_node = launch_ros.actions.Node(
        package='rtabmap_util', executable='point_cloud_xyzrgb', name='point_cloud_xyzrgb2', output='screen',
        parameters=[{
            "approx_sync": True,
        }],
        remappings=[
            ("rgbd_image0", '/camera1/rgbd_image'),
            ("rgbd_image1", '/camera2/rgbd_image'),
            # ("rgbd_image0", '/camera1/rgbd_image'),
            # ("rgbd_image1", '/camera2/rgbd_image'),
            ('scan_cloud', '/velodyne_points')],
    )

    rtab_vis = launch_ros.actions.Node(
            package='rtabmap_viz', executable='rtabmap_viz', output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'odom_frame_id': 'odom',
                'subscribe_odom_info': True,
                'subscribe_scan_cloud': True,
                'use_sim_time': False
            }],
            remappings=[
                ('scan_cloud', '/velodyne_points'),
                ('rgb/image', '/camera1/camera1/color/image_raw'),
                ('depth/image', '/camera1/camera1/depth/image_rect_raw')
            ])

    return launch.LaunchDescription(
        [
            Driver_vel,
            Pointcloud_vel,
            rgbd_sync1_node,
            rgbd_sync2_node,
            # rgbd_odometry_node,
            scan_cloud,
            slam_node,
            # voxelcloud1_node,
            # voxelcloud2_node,
            # rtab_vis
        ]
    )