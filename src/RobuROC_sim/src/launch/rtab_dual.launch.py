import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define nodes for synchronization and SLAM
    # rgbd_sync1_node = Node(
    #     package='rtabmap_sync',
    #     executable='rgbd_sync',
    #     name='rgbd_sync1',
    #     output='screen',
    #     parameters=[{
    #         'approx_sync': True,
    #     }],
    #     remappings=[
    #         ('rgb/image', '/camera1/camera1/color/image_raw'),
    #         ('depth/image', '/camera1/camera1/depth/image_rect_raw'),
    #         ('rgb/camera_info', '/camera1/camera1/color/camera_info'),
    #         ('rgbd_image', 'rgbd_image')],
    #     namespace='camera1'
    # )

    # rgbd_sync2_node = Node(
    #     package='rtabmap_sync',
    #     executable='rgbd_sync',
    #     name='rgbd_sync2',
    #     namespace='camera2',
    #     output='screen',
    #     parameters=[{
    #         'approx_sync': True,
    #     }],
    #     remappings=[
    #         ('rgb/image', '/camera2/camera2/color/image_raw'),
    #         ('depth/image', '/camera2/camera2/depth/image_rect_raw'),
    #         ('rgb/camera_info', '/camera2/camera2/color/camera_info'),
    #         ('rgbd_image', 'rgbd_image')]
    # )


    # RTAB-Map SLAM node
    rtabmap_node = Node(
        package='rtabmap_slam',
        executable='rtabmap',
        output='screen',
        parameters=[{
            'rgbd_cameras': 1,  # Specify two cameras
            # 'subscribe_rgbd': True,
            'frame_id': 'base_link',
            'map_frame_id': 'map',
            'odom_frame_id': 'odom',
            'approx_sync': True,
            'subscribe_depth': True,
            # 'subscribe_rgb': True,
            'topic_queue_size': 3,
            'sync_queue_size': 20,
            # 'rgbd_sync': True,
            'qos': 1,
            'subscribe_scan_cloud': True,
            # 'rgb_topic':'/camera/camera/color',
            # 'depth_topic':'/camera/camera/depth',
            # 'rgbd_topic':'/camera/camera/depth/image_rect_raw'
            # 'Mem/IncrementalMemory': True,
            # 'Mem/InitWMWithAllNodes': True,
        }],
        remappings=[
            ('rgb/image', '/camera/camera/color/image_raw'),
            ('depth/image', '/camera/camera/depth/image_rect_raw'),
            ('rgb/camera_info', '/camera/camera/color/camera_info'),
            ('odom', '/odom')]
    )

    # Optional: Point cloud generation for visualization
    # voxelcloud1_node = Node(
    #     package='rtabmap_util',
    #     executable='point_cloud_xyzrgb',
    #     name='point_cloud_xyzrgb1',
    #     output='screen',
    #     parameters=[{
    #         'approx_sync': True,
    #     }],
    #     remappings=[
    #         ('rgb/image', '/camera1/camera1/color/image_raw'),
    #         ('depth/image', '/camera1/camera1/depth/image_rect_raw'),
    #         ('rgb/camera_info', '/camera1/camera1/color/camera_info'),
    #         ('cloud', 'voxel_cloud1')],
    # )

    # voxelcloud2_node = Node(
    #     package='rtabmap_util',
    #     executable='point_cloud_xyzrgb',
    #     name='point_cloud_xyzrgb2',
    #     output='screen',
    #     parameters=[{
    #         'approx_sync': True,
    #     }],
    #     remappings=[
    #         ('rgb/image', '/camera2/camera2/color/image_raw'),
    #         ('depth/image', '/camera2/camera2/depth/image_rect_raw'),
    #         ('rgb/camera_info', '/camera2/camera2/color/camera_info'),
    #         ('cloud', 'voxel_cloud2')],
    # )

    # Visualization with RTAB-Map Viz
    rtabmap_viz_node = Node(
        package='rtabmap_viz',
        executable='rtabmap_viz',
        output='screen',
        parameters=[{
            'frame_id': 'base_link',
            'map_frame_id': 'map',
            'odom_frame_id': 'odom',
        }],
        remappings=[
            ('rgb/image', '/camera/camera/color/image_raw/compressed'),
            ('depth/image', '/camera/camera/depth/image_rect_raw/compressed'),
            ('rgb/camera_info', '/camera/camera/color/camera_info'),
            ('odom', '/odom')],
    )

    return LaunchDescription([
        # rgbd_sync1_node,
        # rgbd_sync2_node,
        rtabmap_node,
        # voxelcloud1_node,
        # voxelcloud2_node,
        rtabmap_viz_node,
    ])
