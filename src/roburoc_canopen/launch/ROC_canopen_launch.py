from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='roburoc_canopen',
            executable='robuROC_CANOpen.py',
            name='ROC_CAN',
            parameters=[
                {'bustype':'pcan'},
                {'channel':'PCAN_USBBUS1'},
                {'bitrate':1000000}
            ]
        )
    ])