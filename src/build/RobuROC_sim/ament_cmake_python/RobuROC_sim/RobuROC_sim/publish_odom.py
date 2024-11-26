#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  publish_odom.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MC(Node):
    def __init__(self):
        super().__init__('driver')
        
        # Parameters and initialization
        self.track_width = 0.5  # example value, set appropriately
        self.sub = self.create_subscription(Twist, '/odom', self.odom_callback, 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def odom_callback(self, twist_msg):
        # Calculate wheel speeds based on received Twist message
        self.pub.publish(twist_msg)

    # def run(self):
    #     # Main loop to keep running the command loop and odometry loop
    #     while rclpy.ok():
    #         self.cmdvel_loop()
    #         self.odom_loop()

def main(args=None):
    rclpy.init(args=args)
    node = MC()

    # Using a single-threaded executor for simplicity
    executor = rclpy.executors.SingleThreadedExecutor()
    executor.add_node(node)

    try:
        rclpy.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()