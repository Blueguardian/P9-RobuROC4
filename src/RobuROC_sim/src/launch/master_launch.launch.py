import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource


from launch_ros.actions import Node
import xacro


def generate_launch_description():

    robotXacroName = 'RobuROC'  # Must have same name as in xacro file

    # Specify the name of the package and path to xacro file within the package
    namePackage = 'RobuROC_sim'
    RTABPackage = 'rtabmap_launch'
    d345Package = 'realsense2_camera'
    PointcloudPackage = 'velodyne_pointcloud'
    VelDriverPackage = 'velodyne_driver'
    # Path to rviz config
    my_base_path = 'src/RobuROC_sim/src/rviz'   #path to all config files
    my_rviz_path = my_base_path+'/RobuROC_vis.rviz'       #config file for rviz


    modelFileRelativePath = 'description/RobuROC_model.urdf.xacro'


    pathModelFile = os.path.join(get_package_share_directory(namePackage),modelFileRelativePath)
    robotDescription = xacro.process_file(pathModelFile).toxml()



    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        # output='screen',
        output='screen',
        parameters=[{'robot_description':robotDescription,
        'use_sim_time': True}] # add other parameters here if required
    )


    rviz = Node(
            package='rviz2',
            # namespace='',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', str(my_rviz_path)]
    )






    return LaunchDescription([        
        # gazeboLaunch,
        # spawnModelNode,
        node_robot_state_publisher,
        # joint_state_publisher,
        # joint_state_publisher_gui,
        rviz
        # realsense
        # Pointcloud,
        # VelDriver
        # Dual_camera
        # LIDAR
        # RTAB,
        # SLAM

    ])





    # return LaunchDescription([
    #     DeclareLaunchArgument(
    #         'use_sim_time',
    #         default_value='false',
    #         description='Use sim time if true'),        
        
    #     # gazeboLaunch,
    #     # spawnModelNode,
    #     node_robot_state_publisher,
    #     # joint_state_publisher,
    #     # joint_state_publisher_gui,
    #     rviz
    #     # realsense
    #     # Pointcloud,
    #     # VelDriver
    #     # Dual_camera
    #     # LIDAR
    #     # RTAB,
    #     # SLAM

    # ])