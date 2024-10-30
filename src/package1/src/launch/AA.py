from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        path_to_urdf = get_package_share_path('..') / 'urdf' / 'RobuROC.xacro'
        robot_state_publisher_node = launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
            'robot_description': ParameterValue(
            Command(['xacro ', str(path_to_urdf)]), value_type=str
        )
    }]
)
        Node(
            package='rviz',
            executable='rviz',
            name='rviz'
        )
    ])