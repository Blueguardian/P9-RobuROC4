import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'urdf_example'
    file_subpath = 'description/my_example_robot_v2.urdf.xacro'
    # pkg_dir = os.popen('/bin/bash -c "source /usr/share/colcon_cd/function/colcon_cd.sh && \
        # colcon_cd %s && pwd"' % pkg_name).read().strip()
    # base_path = os.path.realpath(get_package_share_directory('urdf_example')) # also tried without realpath
    # rviz_path=base_path+'/config/config.rviz'
    my_base_path = 'src/urdf_example-main/src/rviz'   #path to all config files
    my_rviz_path = my_base_path+'/my_config.rviz'       #config file for rviz

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
    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen', # add other parameters here if required
    )  
    rviz = Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', str(my_rviz_path)]
    )

    # Run the nodes
    return LaunchDescription([
        node_robot_state_publisher,joint_state_publisher,joint_state_publisher_gui,rviz
    ])
