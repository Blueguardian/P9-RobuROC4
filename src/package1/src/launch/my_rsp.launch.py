import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'urdf_example'
    file_subpath = 'description/my_example_robot.urdf.xacro'
    pkg_dir = os.popen('/bin/bash -c "source /usr/share/colcon_cd/function/colcon_cd.sh && \
        colcon_cd %s && pwd"' % pkg_name).read().strip()
    # base_path = os.path.realpath(get_package_share_directory('package')) # also tried without realpath
    # rviz_path=base_path+'/config/config.rviz'

    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()


    # Configure the node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}] # add other parameters here if required
    )
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen', # add other parameters here if required
    )    
    # Node(
    #         package='rviz2',
    #         # namespace='',
    #         executable='rviz2',
    #         name='rviz2',
    #         output='sreen',
    #         arguments=['-d', str(rviz_path)]
    # )
            # arguments=['-d', [os.path.join(pkg_dir, 'config', 'config_file.rviz')]])
    
    # package='rviz2', executable='rviz2', name="rviz2", output='screen'

    # Run the node
    return LaunchDescription([
        node_robot_state_publisher,joint_state_publisher
    ])
