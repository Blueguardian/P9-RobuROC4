import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


from launch_ros.actions import Node
import xacro


def generate_launch_description():

    robotXacroName = 'robot'
    # Specify the name of the package and path to xacro file within the package
    namePackage = 'urdf_example'

    modelFileRelativePath = 'description/my_example_robot_v2.urdf.xacro'
    worldFileRelativePath = 'worlds/empty_world.world'

    pathModelFile = os.path.join(get_package_share_directory(namePackage),modelFileRelativePath)

    pathWolrdFile = os.path.join(get_package_share_directory(namePackage),worldFileRelativePath)

    robotDescription = xacro.process_file(pathModelFile).toxml()

    gazebo_rosPackageLaunch=PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'),'launch','gazebo.launch.py'))

    gazeboLaunch=IncludeLaunchDescription(gazebo_rosPackageLaunch,launch_arguments={'world': pathWolrdFile}.items())

    spawnModelNode = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic','robot_description','-entity',robotXacroName],
        output='screen'
    )

    nodeRobotStatePublisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description':robotDescription,
        'use_sim_time': True}] # add other parameters here if required
    )

    # ####################################################
    # joint_state_publisher = Node(
    #     package='joint_state_publisher',
    #     executable='joint_state_publisher',
    #     output='screen', # add other parameters here if required
    # )    

    # joint_state_publisher_gui = Node(
    #     package='joint_state_publisher_gui',
    #     executable='joint_state_publisher_gui',
    #     output='screen', # add other parameters here if required
    # )  

    # LaunchDescriptionObject.add_action(joint_state_publisher)

    # ####################################################

    # LaunchDescriptionObject = LaunchDescription()

    # LaunchDescriptionObject.add_action(joint_state_publisher)

    # LaunchDescriptionObject.add_action(gazeboLaunch)

    # LaunchDescriptionObject.add_action(spawnModelNode)

    # LaunchDescriptionObject.add_action(nodeRobotStatePublisher)
    #########################################################



    # LaunchDescriptionObject.add_action(joint_state_publisher_gui)

    # Run the node
    # return LaunchDescriptionObject

    return LaunchDescription([
        gazeboLaunch,
        spawnModelNode,
        nodeRobotStatePublisher
    ])

