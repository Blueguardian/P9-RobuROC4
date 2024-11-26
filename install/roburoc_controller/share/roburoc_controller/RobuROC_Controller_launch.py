from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='roburoc_canopen',
            executable='robuROC_CANOpen.py',
            name='ROC_CAN',
            parameters=[
                {'bustype': 'pcan'},
                {'channel': 'PCAN_USBBUS1'},
                {'bitrate': 1000000}
            ]
        ),
        Node(
            package='roburoc_controller',
            executable='robuROC_CTRL.py',
            name='ROC_CTRL'
        ),
        Node(
            package='joy',
            executable='joy_node',
            name='ROC_PAD'
        )
    ])