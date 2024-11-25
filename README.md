# RobuROC simulation - Navigation
This is simulation of the RobuROC platform in Gazebo simulator.
The output from sensors are being visualised in Rviz

## How to run Simulation
1. Build the package with `colcon build`.
2. Source packages `source instalL/setup.bash`
3. Launch file with `ros2 launch RobuROC_sim RobuROC_sim.launch.py`
4. Open new terminal
5. Run `ros2 run teleop_twist_keyboard teleop_twist_keyboard`