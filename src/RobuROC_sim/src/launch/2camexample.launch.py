#
# To avoid log buffering:
# "stdbuf -o L ros2 launch rtabmap_launch rtabmap.launch.py ..."
#

import os

from launch import LaunchDescription, Substitution, LaunchContext
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, LogInfo, OpaqueFunction
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir, PythonExpression
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node
from launch_ros.actions import SetParameter
from typing import Text
from ament_index_python.packages import get_package_share_directory

#Based on https://answers.ros.org/question/363763/ros2-how-best-to-conditionally-include-a-prefix-in-a-launchpy-file/
class ConditionalText(Substitution):
    def __init__(self, text_if, text_else, condition):
        self.text_if = text_if
        self.text_else = text_else
        self.condition = condition

    def perform(self, context: 'LaunchContext') -> Text:
        if self.condition == True or self.condition == 'true' or self.condition == 'True':
            return self.text_if
        else:
            return self.text_else
            
class ConditionalBool(Substitution):
    def __init__(self, text_if, text_else, condition):
        self.text_if = text_if
        self.text_else = text_else
        self.condition = condition

    def perform(self, context: 'LaunchContext') -> bool:
        if self.condition:
            return self.text_if
        else:
            return self.text_else
            
def launch_setup(context, *args, **kwargs):      
               
    return [
        DeclareLaunchArgument('depth', default_value=ConditionalText('false', 'true', IfCondition(PythonExpression(["'", LaunchConfiguration('stereo'), "' == 'true'"]))._predicate_func(context)), description=''),
        DeclareLaunchArgument('subscribe_rgb', default_value=LaunchConfiguration('depth'), description=''),
        DeclareLaunchArgument('args',  default_value=LaunchConfiguration('rtabmap_args'), description='Can be used to pass RTAB-Map\'s parameters or other flags like --udebug and --delete_db_on_start/-d'),
        DeclareLaunchArgument('qos_image',       default_value=LaunchConfiguration('qos'), description='Specific QoS used for image input data: 0=system default, 1=Reliable, 2=Best Effort.'),
        DeclareLaunchArgument('qos_camera_info', default_value=LaunchConfiguration('qos'), description='Specific QoS used for camera info input data: 0=system default, 1=Reliable, 2=Best Effort.'),
        DeclareLaunchArgument('qos_odom',        default_value=LaunchConfiguration('qos'), description='Specific QoS used for odometry input data: 0=system default, 1=Reliable, 2=Best Effort.'),
        DeclareLaunchArgument('qos_user_data',   default_value=LaunchConfiguration('qos'), description='Specific QoS used for user input data: 0=system default, 1=Reliable, 2=Best Effort.'),
    
        SetParameter(name='use_sim_time', value=LaunchConfiguration('use_sim_time')),
        # 'use_sim_time' will be set on all nodes following the line above
    
        # Relays RGB-Depth
        Node(
            package='image_transport', executable='republish', name='republish_rgb1',
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('stereo'), "' != 'true' and ('", LaunchConfiguration('subscribe_rgbd'), "' != 'true' or '", LaunchConfiguration('rgbd_sync'),"'=='true') and '", LaunchConfiguration('compressed'), "' == 'true'"])),
            remappings=[
                (['in/', LaunchConfiguration('rgb_image_transport')], [LaunchConfiguration('rgb_topic1'), '/', LaunchConfiguration('rgb_image_transport')]),
                ('out', LaunchConfiguration('rgb_topic1'))], 
            arguments=[LaunchConfiguration('rgb_image_transport'), 'raw'],
            namespace='realsense_camera1'),
        Node(
            package='image_transport', executable='republish', name='republish_rgb2',
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('stereo'), "' != 'true' and ('", LaunchConfiguration('subscribe_rgbd'), "' != 'true' or '", LaunchConfiguration('rgbd_sync'),"'=='true') and '", LaunchConfiguration('compressed'), "' == 'true'"])),
            remappings=[
                (['in/', LaunchConfiguration('rgb_image_transport')], [LaunchConfiguration('rgb_topic2'), '/', LaunchConfiguration('rgb_image_transport')]),
                ('out', LaunchConfiguration('rgb_topic2'))], 
            arguments=[LaunchConfiguration('rgb_image_transport'), 'raw'],
            namespace='realsense_camera2'),
        Node(
            package='image_transport', executable='republish', name='republish_depth1',
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('stereo'), "' != 'true' and ('", LaunchConfiguration('subscribe_rgbd'), "' != 'true' or '", LaunchConfiguration('rgbd_sync'),"'=='true') and '", LaunchConfiguration('compressed'), "' == 'true'"])),
            remappings=[
                (['in/', LaunchConfiguration('depth_image_transport')], [LaunchConfiguration('depth_topic1'), '/', LaunchConfiguration('depth_image_transport')]),
                ('out', LaunchConfiguration('depth_topic1'))], 
            arguments=[LaunchConfiguration('depth_image_transport'), 'raw'],
            namespace='realsense_camera1'),
        Node(
            package='image_transport', executable='republish', name='republish_depth2',
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('stereo'), "' != 'true' and ('", LaunchConfiguration('subscribe_rgbd'), "' != 'true' or '", LaunchConfiguration('rgbd_sync'),"'=='true') and '", LaunchConfiguration('compressed'), "' == 'true'"])),
            remappings=[
                (['in/', LaunchConfiguration('depth_image_transport')], [LaunchConfiguration('depth_topic2'), '/', LaunchConfiguration('depth_image_transport')]),
                ('out', LaunchConfiguration('depth_topic2'))], 
            arguments=[LaunchConfiguration('depth_image_transport'), 'raw'],
            namespace='realsense_camera2'),

        Node(
            package='rtabmap_sync', executable='rgbd_sync', name='rgbd_sync1', output="screen",
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('stereo'), "' != 'true' and '", LaunchConfiguration('rgbd_sync'), "' == 'true'"])),
            parameters=[{
                "approx_sync": False,
                "approx_sync_max_interval": LaunchConfiguration('approx_sync_max_interval'),
                "queue_size": LaunchConfiguration('queue_size'),
                "qos": LaunchConfiguration('qos_image'),
                "qos_camera_info": LaunchConfiguration('qos_camera_info'),
                "depth_scale": LaunchConfiguration('depth_scale')}],
            remappings=[
                ("rgb/image", LaunchConfiguration('rgb_topic1')),
                ("depth/image", LaunchConfiguration('depth_topic1')),
                ("rgb/camera_info", LaunchConfiguration('camera_info_topic1')),
                ("rgbd_image", LaunchConfiguration('rgbd_topic'))],
            namespace='/realsense_camera1'),
        Node(
            package='rtabmap_sync', executable='rgbd_sync', name='rgbd_sync2', output="screen",
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('stereo'), "' != 'true' and '", LaunchConfiguration('rgbd_sync'), "' == 'true'"])),
            parameters=[{
                "approx_sync": False,
                "approx_sync_max_interval": LaunchConfiguration('approx_sync_max_interval'),
                "queue_size": LaunchConfiguration('queue_size'),
                "qos": LaunchConfiguration('qos_image'),
                "qos_camera_info": LaunchConfiguration('qos_camera_info'),
                "depth_scale": LaunchConfiguration('depth_scale')}],
            remappings=[
                ("rgb/image", LaunchConfiguration('rgb_topic2')),
                ("depth/image", LaunchConfiguration('depth_topic2')),
                ("rgb/camera_info", LaunchConfiguration('camera_info_topic2')),
                ("rgbd_image", LaunchConfiguration('rgbd_topic'))],
            namespace='/realsense_camera2'),
            
        # Relay rgbd_image
        Node(
            package='rtabmap_util', executable='rgbd_relay', output="screen",
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('rgbd_sync'), "' != 'true' and '", LaunchConfiguration('subscribe_rgbd'), "' == 'true' and '", LaunchConfiguration('compressed'), "' != 'true'"])),
            remappings=[
                ("rgbd_image", LaunchConfiguration('rgbd_topic'))],
            namespace=LaunchConfiguration('namespace')),
        Node(
            package='rtabmap_util', executable='rgbd_relay', output="screen",
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('rgbd_sync'), "' != 'true' and '", LaunchConfiguration('subscribe_rgbd'), "' == 'true' and '", LaunchConfiguration('compressed'), "' == 'true'"])),
            parameters=[{
                "uncompress": True,
                "qos": LaunchConfiguration('qos_image')}],
            remappings=[
                ("rgbd_image", [LaunchConfiguration('rgbd_topic'), "/compressed"]),
                ([LaunchConfiguration('rgbd_topic'), "/compressed_relay"], LaunchConfiguration('rgbd_topic'))],
            namespace=LaunchConfiguration('namespace')),
                
        # RGB-D odometry
        Node(
            package='rtabmap_odom', executable='rgbd_odometry', output="screen",
            condition=IfCondition(PythonExpression(["'", LaunchConfiguration('icp_odometry'), "' != 'true' and '", LaunchConfiguration('visual_odometry'), "' == 'true' and '", LaunchConfiguration('stereo'), "' != 'true'"])),
            parameters=[{
                "rgbd_cameras":2,
                "frame_id": LaunchConfiguration('frame_id'),
                "odom_frame_id": LaunchConfiguration('vo_frame_id'),
                "publish_tf": LaunchConfiguration('publish_tf_odom'),
                "ground_truth_frame_id": LaunchConfiguration('ground_truth_frame_id').perform(context),
                "ground_truth_base_frame_id": LaunchConfiguration('ground_truth_base_frame_id').perform(context),
                "wait_for_transform": LaunchConfiguration('wait_for_transform'),
                "wait_imu_to_init": LaunchConfiguration('wait_imu_to_init'),
                "approx_sync": LaunchConfiguration('approx_sync'),
                "approx_sync_max_interval": LaunchConfiguration('approx_sync_max_interval'),
                "config_path": LaunchConfiguration('cfg').perform(context),
                "queue_size": LaunchConfiguration('queue_size'),
                "qos": LaunchConfiguration('qos_image'),
                "qos_camera_info": LaunchConfiguration('qos_camera_info'),
                "subscribe_rgbd": LaunchConfiguration('subscribe_rgbd'),
                "guess_frame_id": LaunchConfiguration('odom_guess_frame_id').perform(context),
                "guess_min_translation": LaunchConfiguration('odom_guess_min_translation'),
                "guess_min_rotation": LaunchConfiguration('odom_guess_min_rotation')}],
            remappings=[
                ("rgb/image", LaunchConfiguration('rgb_topic1')),
                ("depth/image", LaunchConfiguration('depth_topic1')),
                ("rgb/camera_info", LaunchConfiguration('camera_info_topic1')),
                ("rgbd_image0", '/realsense_camera1/rgbd_image'),
                ("rgbd_image1", '/realsense_camera2/rgbd_image'),
                ("odom", LaunchConfiguration('odom_topic'))],
            arguments=[LaunchConfiguration("args"), LaunchConfiguration("odom_args")],
            prefix=LaunchConfiguration('launch_prefix'),
            namespace=LaunchConfiguration('namespace')),

        Node(
            package='rtabmap_slam', executable='rtabmap', output="screen",
            parameters=[{
                "rgbd_cameras":1,
                "subscribe_depth": LaunchConfiguration('depth'),
                "subscribe_rgbd": LaunchConfiguration('subscribe_rgbd'),
                "subscribe_rgb": True,
                "subscribe_stereo": LaunchConfiguration('stereo'),
                "subscribe_user_data": LaunchConfiguration('subscribe_user_data'),
                "subscribe_odom_info": ConditionalBool(True, False, IfCondition(PythonExpression(["'", LaunchConfiguration('icp_odometry'), "' == 'true' or '", LaunchConfiguration('visual_odometry'), "' == 'true'"]))._predicate_func(context)).perform(context),
                "frame_id": LaunchConfiguration('frame_id'),
                "map_frame_id": LaunchConfiguration('map_frame_id'),
                "odom_frame_id": LaunchConfiguration('odom_frame_id').perform(context),
                "publish_tf": LaunchConfiguration('publish_tf_map'),
                "initial_pose": LaunchConfiguration('initial_pose'),
                "ground_truth_frame_id": LaunchConfiguration('ground_truth_frame_id').perform(context),
                "ground_truth_base_frame_id": LaunchConfiguration('ground_truth_base_frame_id').perform(context),
                "odom_tf_angular_variance": LaunchConfiguration('odom_tf_angular_variance'),
                "odom_tf_linear_variance": LaunchConfiguration('odom_tf_linear_variance'),
                "odom_sensor_sync": LaunchConfiguration('odom_sensor_sync'),
                "wait_for_transform": LaunchConfiguration('wait_for_transform'),
                "database_path": LaunchConfiguration('database_path'),
                "approx_sync": True,
                "config_path": LaunchConfiguration('cfg').perform(context),
                "queue_size": LaunchConfiguration('queue_size'),
                "qos_image": LaunchConfiguration('qos_image'),
                "qos_odom": LaunchConfiguration('qos_odom'),
                "qos_camera_info": LaunchConfiguration('qos_camera_info'),
                "qos_user_data": LaunchConfiguration('qos_user_data'),
                "Mem/IncrementalMemory": ConditionalText("true", "false", IfCondition(PythonExpression(["'", LaunchConfiguration('localization'), "' != 'true'"]))._predicate_func(context)).perform(context),
                "Mem/InitWMWithAllNodes": ConditionalText("true", "false", IfCondition(PythonExpression(["'", LaunchConfiguration('localization'), "' == 'true'"]))._predicate_func(context)).perform(context)
            }],
            remappings=[
                ("rgb/image", LaunchConfiguration('rgb_topic1')),
                ("depth/image", LaunchConfiguration('depth_topic1')),
                ("rgb/camera_info", LaunchConfiguration('camera_info_topic1')),
                ("rgbd_image", LaunchConfiguration('rgbd_topic')),
                ("left/image_rect", LaunchConfiguration('left_image_topic')),
                ("right/image_rect", LaunchConfiguration('right_image_topic')),
                ("left/camera_info", LaunchConfiguration('left_camera_info_topic')),
                ("right/camera_info", LaunchConfiguration('right_camera_info_topic')),
                ("user_data", LaunchConfiguration('user_data_topic')),
                ("user_data_async", LaunchConfiguration('user_data_async_topic')),
                ("odom", LaunchConfiguration('odom_topic'))],
            arguments=[LaunchConfiguration("args")],
            prefix=LaunchConfiguration('launch_prefix'),
            namespace=LaunchConfiguration('namespace')),

        Node(
            package='rtabmap_viz', executable='rtabmap_viz', output='screen',
            parameters=[{
                "subscribe_depth": LaunchConfiguration('depth'),
                "subscribe_rgbd": LaunchConfiguration('subscribe_rgbd'),
                "subscribe_rgb": LaunchConfiguration('subscribe_rgb'),
                "subscribe_stereo": LaunchConfiguration('stereo'),
                "subscribe_user_data": LaunchConfiguration('subscribe_user_data'),
                "subscribe_odom_info": ConditionalBool(True, False, IfCondition(PythonExpression(["'", LaunchConfiguration('icp_odometry'), "' == 'true' or '", LaunchConfiguration('visual_odometry'), "' == 'true'"]))._predicate_func(context)).perform(context),
                "frame_id": LaunchConfiguration('frame_id'),
                "odom_frame_id": LaunchConfiguration('odom_frame_id').perform(context),
                "wait_for_transform": LaunchConfiguration('wait_for_transform'),
                "approx_sync": LaunchConfiguration('approx_sync'),
                "queue_size": LaunchConfiguration('queue_size'),
                "qos_image": LaunchConfiguration('qos_image'),
                "qos_odom": LaunchConfiguration('qos_odom'),
                "qos_camera_info": LaunchConfiguration('qos_camera_info'),
                "qos_user_data": LaunchConfiguration('qos_user_data')
            }],
            remappings=[
                ("rgb/image", LaunchConfiguration('rgb_topic1')),
                ("depth/image", LaunchConfiguration('depth_topic1')),
                ("rgb/camera_info", LaunchConfiguration('camera_info_topic1')),
                ("rgbd_image", LaunchConfiguration('rgbd_topic')),
                ("left/image_rect", LaunchConfiguration('left_image_topic')),
                ("right/image_rect", LaunchConfiguration('right_image_topic')),
                ("left/camera_info", LaunchConfiguration('left_camera_info_topic')),
                ("right/camera_info", LaunchConfiguration('right_camera_info_topic')),
                ("odom", LaunchConfiguration('odom_topic'))],
            condition=IfCondition(LaunchConfiguration("rtabmapviz")),
            arguments=[LaunchConfiguration("gui_cfg")],
            prefix=LaunchConfiguration('launch_prefix'),
            namespace=LaunchConfiguration('namespace')),
        Node(
            package='rviz2', executable='rviz2', output='screen',
            condition=IfCondition(LaunchConfiguration("rviz")),
            arguments=[["-d"], [LaunchConfiguration("rviz_cfg")]]),
        Node(
            package='rtabmap_util', executable='point_cloud_xyzrgb', output='screen',
            condition=IfCondition(LaunchConfiguration("rviz")),
            parameters=[{
                "decimation": 4,
                "voxel_size": 0.0,
                "approx_sync": LaunchConfiguration('approx_sync'),
                "approx_sync_max_interval": LaunchConfiguration('approx_sync_max_interval')
            }],
            remappings=[
                ('left/image', LaunchConfiguration('left_image_topic')),
                ('right/image', LaunchConfiguration('right_image_topic')),
                ('left/camera_info', LaunchConfiguration('left_camera_info_topic')),
                ('right/camera_info', LaunchConfiguration('right_camera_info_topic')),
                ('rgb/image', LaunchConfiguration('rgb_topic1')),
                ('depth/image', LaunchConfiguration('depth_topic1')),
                ('rgb/camera_info', LaunchConfiguration('camera_info_topic1')),
                ('rgbd_image', LaunchConfiguration('rgbd_topic')),
                ('cloud', 'voxel_cloud')]),
        ]

def generate_launch_description():
    
    config_rviz = os.path.join(
        get_package_share_directory('rtabmap_launch'), 'launch', 'config', 'pC_rtabmap_2cameras.rviz'
    )
    
    return LaunchDescription([
        
        # Arguments
        DeclareLaunchArgument('stereo', default_value='false', description='Use stereo input instead of RGB-D.'),

        DeclareLaunchArgument('localization', default_value='false', description='Launch in localization mode.'),
        DeclareLaunchArgument('rtabmapviz',   default_value='false',  description='Launch RTAB-Map UI (optional).'),
        DeclareLaunchArgument('rviz',         default_value='false', description='Launch RVIZ (optional).'),

        DeclareLaunchArgument('use_sim_time', default_value='false', description='Use simulation (Gazebo) clock if true'),

        # Config files
        DeclareLaunchArgument('cfg',      default_value='',                        description='To change RTAB-Map\'s parameters, set the path of config file (*.ini) generated by the standalone app.'),
        DeclareLaunchArgument('gui_cfg',  default_value='~/.ros/rtabmap_gui.ini',  description='Configuration path of rtabmapviz.'),
        DeclareLaunchArgument('rviz_cfg', default_value=config_rviz,               description='Configuration path of rviz2.'),

        DeclareLaunchArgument('frame_id',       default_value='base_link',          description='Fixed frame id of the robot (base frame), you may set "base_link" or "base_footprint" if they are published. For camera-only config, this could be "camera_link".'),
        DeclareLaunchArgument('odom_frame_id',  default_value='',                   description='If set, TF is used to get odometry instead of the topic.'),
        DeclareLaunchArgument('map_frame_id',   default_value='map',                description='Output map frame id (TF).'),
        DeclareLaunchArgument('publish_tf_map', default_value='true',               description='Publish TF between map and odomerty.'),
        DeclareLaunchArgument('namespace',      default_value='rtabmap',            description=''),
        DeclareLaunchArgument('database_path',  default_value='~/.ros/rtabmap.db',  description='Where is the map saved/loaded.'),
        DeclareLaunchArgument('queue_size',     default_value='10',                 description=''),
        DeclareLaunchArgument('qos',            default_value='1',                  description='General QoS used for sensor input data: 0=system default, 1=Reliable, 2=Best Effort.'),
        DeclareLaunchArgument('wait_for_transform', default_value='0.2',            description=''),
        DeclareLaunchArgument('rtabmap_args',   default_value='',                   description='Backward compatibility, use "args" instead.'),
        DeclareLaunchArgument('launch_prefix',  default_value='',                   description='For debugging purpose, it fills prefix tag of the nodes, e.g., "xterm -e gdb -ex run --args"'),
        DeclareLaunchArgument('output',         default_value='screen',             description='Control node output (screen or log).'),
        DeclareLaunchArgument('initial_pose',   default_value='',                   description='Set an initial pose (only in localization mode). Format: "x y z roll pitch yaw" or "x y z qx qy qz qw". Default: see "RGBD/StartAtOrigin" doc'),
        
        DeclareLaunchArgument('ground_truth_frame_id',      default_value='', description='e.g., "world"'),
        DeclareLaunchArgument('ground_truth_base_frame_id', default_value='', description='e.g., "tracker", a fake frame matching the frame "frame_id" (but on different TF tree)'),
        
        DeclareLaunchArgument('approx_sync',  default_value='false',            description='If timestamps of the input topics should be synchronized using approximate or exact time policy.'),
        DeclareLaunchArgument('approx_sync_max_interval',  default_value='0.0', description='(sec) 0 means infinite interval duration (used with approx_sync=true)'),
        
        # Stereo related topics
        DeclareLaunchArgument('stereo_namespace',        default_value='/stereo_camera', description=''),
        DeclareLaunchArgument('left_image_topic',        default_value=[LaunchConfiguration('stereo_namespace'), '/left/image_rect_color'], description=''),
        DeclareLaunchArgument('right_image_topic',       default_value=[LaunchConfiguration('stereo_namespace'), '/right/image_rect'], description='Use grayscale image for efficiency'),
        DeclareLaunchArgument('left_camera_info_topic',  default_value=[LaunchConfiguration('stereo_namespace'), '/left/camera_info'], description=''),
        DeclareLaunchArgument('right_camera_info_topic', default_value=[LaunchConfiguration('stereo_namespace'), '/right/camera_info'], description=''),
        
        # Use Pre-sync RGBDImage format
        DeclareLaunchArgument('rgbd_sync',        default_value='false',      description='Pre-sync rgb_topic, depth_topic, camera_info_topic.'),
        DeclareLaunchArgument('approx_rgbd_sync', default_value='true',       description='false=exact synchronization.'),
        DeclareLaunchArgument('subscribe_rgbd',   default_value=LaunchConfiguration('rgbd_sync'), description='Already synchronized RGB-D related topic, e.g., with rtabmap_sync/rgbd_sync nodelet.'),
        DeclareLaunchArgument('rgbd_topic',       default_value='rgbd_image', description=''),
        DeclareLaunchArgument('depth_scale',      default_value='1.0',        description=''),
        
        # Image topic compression
        DeclareLaunchArgument('compressed',            default_value='false', description='If you want to subscribe to compressed image topics'),
        DeclareLaunchArgument('rgb_image_transport',   default_value='compressed', description='Common types: compressed, theora (see "rosrun image_transport list_transports")'),
        DeclareLaunchArgument('depth_image_transport', default_value='compressedDepth', description='Depth compatible types: compressedDepth (see "rosrun image_transport list_transports")'),
        
        # Odometry
        DeclareLaunchArgument('visual_odometry',            default_value='true',  description='Launch rtabmap visual odometry node.'),
        DeclareLaunchArgument('icp_odometry',               default_value='false', description='Launch rtabmap icp odometry node.'),
        DeclareLaunchArgument('odom_topic',                 default_value='odom',  description='Odometry topic name.'),
        DeclareLaunchArgument('vo_frame_id',                default_value=LaunchConfiguration('odom_topic'), description='Visual/Icp odometry frame ID for TF.'),
        DeclareLaunchArgument('publish_tf_odom',            default_value='true',  description=''),
        DeclareLaunchArgument('odom_tf_angular_variance',   default_value='0.01',    description='If TF is used to get odometry, this is the default angular variance'),
        DeclareLaunchArgument('odom_tf_linear_variance',    default_value='0.001',   description='If TF is used to get odometry, this is the default linear variance'),
        DeclareLaunchArgument('odom_args',                  default_value='',      description='More arguments for odometry (overwrite same parameters in rtabmap_args).'),
        DeclareLaunchArgument('odom_sensor_sync',           default_value='false', description=''),
        DeclareLaunchArgument('odom_guess_frame_id',        default_value='',      description=''),
        DeclareLaunchArgument('odom_guess_min_translation', default_value='0.0',   description=''),
        DeclareLaunchArgument('odom_guess_min_rotation',    default_value='0.0',   description=''),
        
        # User Data
        DeclareLaunchArgument('subscribe_user_data',   default_value='false',            description='User data synchronized subscription.'),
        DeclareLaunchArgument('user_data_topic',       default_value='/user_data',       description=''),
        DeclareLaunchArgument('user_data_async_topic', default_value='/user_data_async', description='User data async subscription (rate should be lower than map update rate).'),

        OpaqueFunction(function=launch_setup)
    ])