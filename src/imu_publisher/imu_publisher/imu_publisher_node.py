import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Header
import serial
import time


class IMUPublisherNode(Node):

    def __init__(self):
        super().__init__('imu_publisher_node')

        # Initialize the serial connection (adjust port and baud rate as needed)
        self.serial_port = '/dev/ttyUSB2'  # might change when plugging and unplugging imu on the usb hub
        self.baud_rate = 115200
        self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)

        # Create a publisher for the IMU data
        self.imu_pub = self.create_publisher(Imu, 'imu/data', 10)

        # Timer to read data periodically
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10Hz

    def timer_callback(self):
        if self.ser.in_waiting > 0:
            # Read the serial data (comma-separated values)

            line = self.ser.readline().decode('utf-8')
            try:
                # Parse the incoming data string in the format:
                # gx=0.0681,gy=0.2355,gz=-0.1903,d1=1478,d2=3386
                data = {item.split('=')[0]: float(item.split('=')[1]) for item in line.split(',')}

                # Extract the gyroscope values (gx, gy, gz)
                gx = data.get('gx', 0.0)
                gy = data.get('gy', 0.0)
                gz = data.get('gz', 0.0)

                # Optionally extract d1 and d2 values if you need them
                d1 = data.get('d1', 0)
                d2 = data.get('d2', 0)

                # Create IMU message
                imu_msg = Imu()
                imu_msg.header = Header()
                imu_msg.header.stamp = self.get_clock().now().to_msg()

                # Assign the gyroscope data (convert to rad/s if needed)
                imu_msg.angular_velocity.x = gx  # Assume the units are rad/s
                imu_msg.angular_velocity.y = gy  # Assuming the same unit
                imu_msg.angular_velocity.z = gz  # Assuming the same unit

                # You can also use accelerometer data if available
                # imu_msg.linear_acceleration.x = ax / 16384.0  # Example scaling for MPU6050

                # Publish the IMU message
                self.imu_pub.publish(imu_msg)
            except ValueError as e:
                self.get_logger().warn(f"Failed to parse line: {line}. Error: {e}")


def main(args=None):
    rclpy.init(args=args)
    imu_publisher_node = IMUPublisherNode()

    rclpy.spin(imu_publisher_node)

    imu_publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()