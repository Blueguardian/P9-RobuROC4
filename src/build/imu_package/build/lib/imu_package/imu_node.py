import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import serial

class IMUNode(Node):
    def __init__(self):
        super().__init__('imu_node')
        self.publisher = self.create_publisher(Imu, 'imu/data', 10)
        self.serial_port = '/dev/ttyUSB0'  # Adjust based on your setup
        self.baud_rate = 57600
        self.ser = serial.Serial(self.serial_port, self.baud_rate)
        self.timer = self.create_timer(0.01, self.publish_imu_data)  # 100Hz

    def publish_imu_data(self):
        try:
            line = self.ser.readline().decode('utf-8').strip()
            ax, ay, az, gx, gy, gz = [float(x) for x in line.split(',')]

            msg = Imu()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = "imu_link"
            msg.linear_acceleration.x = ax
            msg.linear_acceleration.y = ay
            msg.linear_acceleration.z = az
            msg.angular_velocity.x = gx
            msg.angular_velocity.y = gy
            msg.angular_velocity.z = gz

            self.publisher.publish(msg)
        except Exception as e:
            self.get_logger().error(f"Error reading serial data: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = IMUNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
