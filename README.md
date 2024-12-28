# RobuROC - Mapping and Localising
### Table of contents
- [General info](#p1)
    - [1Mapping.launch.py](#p1.1)
    - [2Mapping.launch.py](#p1.2)
- [Setup](#p2)

## General info <a name="p1">
This code has been used for for testing of the RobuROC platform.
RTAB-Map has been used for mapping and localising. The outputs from sensors and RTAB-Map is being visualised in Rviz.
Furthermore platform has been controlled through joystick.
For testing purposes two mapping algorithms has been created:

### 1Mapping.launch.py <a name="p1.1">
This algorithm utilises RGB-D camera for visual odometry and dual RGB-D camera mapping.

### 2Mapping.launch.py <a name="p1.2">
This algorithm utilises LiDAR for ICP odometry LiDAR based mapping.

## Setup <a name="p2">
### How to run Platform
1. Build the package with `colcon build`
2. Source packages `source instalL/setup.bash`
3. Choose mapping algorithm
4. Launch file with `ros2 launch RobuROC_sim 1Mapping.launch.py` or `ros2 launch RobuROC_sim 2Mapping.launch.py`
5. To controll robot with controller. Open new terminal
6. Run `ros2 launch roburoc_comtroller RobuROC_Controller_launch.py`

### How to run Simulation
1. Build the package with `colcon build`.
2. Source packages `source instalL/setup.bash`
3. Launch file with `ros2 launch RobuROC_sim RobuROC_sim.launch.py`
4. Open new terminal
5. Run `ros2 run teleop_twist_keyboard teleop_twist_keyboard`