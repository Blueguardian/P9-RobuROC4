# RobuROC simulation

## How To Run Rviz

1. Build the package with `colcon build`.
2. Source packages `source instalL/setup.bash`
3. Launch file with `ros2 launch RobuROC_sim RobuROC_rviz.launch.py`.

## How To Run Gazebo
1. Build the package with `colcon build`.
2. Source packages `source instalL/setup.bash`
3. Launch file with `ros2 launch RobuROC_sim RobuROC_gazebo.launch.py`.
4. Open new terminal
5. Run `ros2 run teleop_twist_keyboard teleop_twist_keyboard`