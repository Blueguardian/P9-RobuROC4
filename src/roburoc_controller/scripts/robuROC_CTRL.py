#!/usr/bin/env python3
from utils.CTW import CTW
from utils.COBID import COBID
from canopen_interfaces.msg import CANWrite, CANSubscription
from canopen_interfaces.srv import CANRead, CANConnection, CANPeriodicTask, CANSubscribe
import rclpy.subscription, logging, time
from rclpy.node import Node
from sensor_msgs.msg import Joy
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("CAN_Logs"),
                              logging.StreamHandler()])

class RobuROC_CTRL(Node):
    """

    """
    # Initialize fields to contain periodic status updates
    _CURRENT_PERIODIC = [None, None, None, None]
    _VELOCITY_PERIODIC = [None, None, None, None]
    _STATUS_PERIODIC = [None, None, None, None]
    _TEMPORARY_PERIODIC = [None, None, None, None]

    # Setup fields for status and debugging
    _CONNECTED = False
    _PERIODIC = False
    _HEARTBEAT = False

    # Public variables
    MAX_SPEED = 2  # Meters per second
    WHEEL_RADIUS = 0.28  # Meters

    # Constants
    _SCALE_CURRENT = pow(2, 13) / 40.0  # to Amps
    _SCALE_SETCURRENT = pow(2, 15) / 40.0  # to Amps
    _SCALE_VELOCITY = ((pow(2, 17) / (2 * 20000) * pow(2, 19)) / 1000) * 32  # To RPM
    _SCALE_RPM_TO_MPS = ((2.0 * 3.14) / 60.0) * WHEEL_RADIUS

    _DEADMAN_SWITCH = False

    def __init__(self):
        super().__init__('ROC_CTRL')
        self.logger = self.get_logger()

        # Setup canopen help modules
        self._CTW = CTW()
        self._COBID = COBID()

        # Set up publisher
        self.WritePub = self.create_publisher(CANWrite, 'CANWrite', 10)

        # Set up service clients
        self.ConnectionSrvCli = self.create_client(CANConnection, 'CANConnection')
        self.ConnectionSrvCli.wait_for_service()
        self.PeriodicSrvCli = self.create_client(CANPeriodicTask, 'CANPeriodic')
        self.PeriodicSrvCli.wait_for_service()
        self.SubscribeSrvCli = self.create_client(CANSubscribe, 'CANSubscribe')
        self.SubscribeSrvCli.wait_for_service()
        self.ReadSrvCli = self.create_client(CANRead, 'CANRead')
        self.ReadSrvCli.wait_for_service()

        # Set up subscriptions
        self.SubscriptionSub = self.create_subscription(CANSubscription, 'CANSubscription', self.Subscription_CB, 10)
        self.VelSub = self.create_subscription(Joy, '/joy', self.setSpeed, 10)

        # Set up interface variables
        self._CAN_NODES = []

    def setup(self):
        """
        Setup for the RobuROC-4 (pre-configured) CANBus
        :return: None
        """
        # If the system is already initialized, stop it and reset everything
        request = CANConnection.Request()
        request.command = "Connect"
        while not self._CONNECTED:
            response = self.ConnectionSrvCli.call_async(request)
            rclpy.spin_until_future_complete(self, response)
            self._CONNECTED = response.result().success
            self._CAN_NODES.extend(response.result().node_list)
            self.logger.info(f"Connected to nodes: {self._CAN_NODES}")
        if self._CONNECTED == True:
            # Reset all drives
            # node.nmt.send_command(0x81, 0)
            self.NMT_Write([self._CTW.RESET])
            # Set deceleration on all drives
            # self.NMT_Write([self._CTW.TURNON])
            # # self.SDO_Write(node, [0x2064, 0x04], [0x80, 0x4F, 0x12])
            # # Enable all drives
            # # node.nmt.send_command(0x01, 0)
            # self.NMT_Write([self._CTW.ENABLE])
            # # Turn on all drives
            # # node.nmt.send_command(0x07, 0)
            # self.NMT_Write([self._CTW.TURNON])
            # Enable operatiom on all drives
            # node.nmt.send_command(0x0F, 0)
            self.NMT_Write([self._CTW.ENABLE_OP])
            sleep(2)

            # self.NMT_Write([self._CTW.ENABLE_OP])
            self.NMT_Write([self._CTW.ENABLE])
            for node in self._CAN_NODES:
                # self.CAN.NMTwrite(node.id, self._CTW.ENABLE_OP)
                # self.SDO_Write(node - 1, [0x2062, 0x00], [0x80, 0x4F, 0x12])
                self.SDO_Write(node-1, [0x6040, 0x00], [0x0F, 0x00, 0x00, 0x00])

            if not self._PERIODIC:
                self.InitPeriodic()
            if not self._HEARTBEAT:
                self.InitHeartbeat()
        else:
            Node.get_logger(self).error(f"Unable to connect to CANBUS")
    def InitHeartbeat(self, heartbeat_time_ms: float = 0.2):
        """
        Initialize heartbeat messages where the host (Node 0) is the producer
        and the nodes are consumers.

        :param heartbeat_time_ms: Time interval in seconds for sending heartbeat messages.
        """
        success = self.AddPeriodicTask(0x700+self._COBID.HOST, [0], heartbeat_time_ms)
        if success:
            self._HEARTBEAT = True
        else:
            self._HEARTBEAT = False
    def InitPeriodic(self):
        """
        Initialize periodic read TPDO messages, such that it returns with periodic updates to the state of the drives
        and motors.
        :return: None
        """
        success_vel = []
        success_cur = []
        success_heart = []

        for node in self._CAN_NODES:
            success_vel.append(self.Subscribe(self._COBID.ACT_VELOCITY.ALL[node-1]))
            success_cur.append(self.Subscribe(self._COBID.ACT_CURRENT.ALL[node-1]))
            success_heart.append(self.Subscribe(self._COBID.HEARTBEAT.ALL[node-1]))

        self.logger.debug(f"Successfully subcribed to Velocity for nodes [1, 2, 3, 4]:{success_vel}, Current: {success_cur}, Heartbeat: {success_heart}")
        if all(success_vel) and all(success_cur) and all(success_heart):
            self._PERIODIC = True
        else:
            self._PERIODIC = False

    def setSpeed(self, message):
        """
        Method for setting the speed of the individual wheels
        :param speed: A list of speeds for the individual wheels
        :param type: Speed representation, current supported values: ['MPS', 'RPM']
        :return: None
        """
        if message.buttons[2] == 1:
            left = round(message.axes[1] + message.axes[0] / 4, 4) * 2
            right = round(message.axes[1] - message.axes[0] / 4, 4) * 2
            vel_MPS = int(left * (self._SCALE_VELOCITY / self._SCALE_RPM_TO_MPS))
            vel2_MPS = int(-right * (self._SCALE_VELOCITY / self._SCALE_RPM_TO_MPS))
            self.logger.info(f"Sending velocity commands: {vel_MPS}")
            vel_MPS = list(bytearray(vel_MPS.to_bytes(4, byteorder='little', signed=True)))
            vel2_MPS = list(bytearray(vel2_MPS.to_bytes(4, byteorder='little', signed=True)))
            self.SDO_Write(0,[0x60FF, 0x00], vel_MPS)
            self.SDO_Write(1, [0x60FF, 0x00], vel2_MPS)
            self.SDO_Write(2, [0x60FF, 0x00], vel2_MPS)
            self.SDO_Write(3, [0x60FF, 0x00], vel_MPS)


        # network.send_message(0x514, vel_MPS)
        # network.send_message(0x513, vel2_MPS)
        # network.send_message(0x512, vel2_MPS)
        # network.send_message(0x511, vel_MPS)

            # # Set the mode to velocity mode
            # SDO_msg = CANWrite
            # SDO_msg.command = "SDO"
            # SDO_msg.node_id = nodeSDO_msg = CANWrite
            #     SDO_msg.command = "SDO"
            #     SDO_msg.node_id = node
            #     SDO_msg.indices = [0x20, 0x64, 0x04]
            #     SDO_msg.data = [0x80, 0x4F, 0x12]
            #     self.WritePub.publish(SDO_msg)
            # SDO_msg.indices = [0x20, 0x64, 0x04]
            # SDO_msg.data = [0x80, 0x4F, 0x12]
            # self.WritePub.publish(SDO_msg)
            # self.CAN.SDOwrite(node.id, [0x60, 0x60, 0x00], [0x03])

#             # If the system is not in operation mode
#             if self._STATUS_PERIODIC[node.id-1] == 'OPERATIONAL':
#                 self.recover()
#                 self.CAN.NMTwrite(node.id, self._CTW.ENABLE_OP)

#             data = list(speed.to_bytes(4, byteorder='little', signed=True))
#             self.CAN.SDOwrite(node.id, [0x60, 0xFF, 0x00], data)
    def brake(self):
        """
        Method for braking the RobuROC4 when velocity is set to 0.
        :param node_id: The node for which to change the state to Quickstop
        :return: None
        """
        self.NMT_Write([self._CTW.QUICKSTOP])
        self.NMT_Write([self._CTW.ENABLE])
        for node in self._CAN_NODES:
            # self.CAN.NMTwrite(node.id, self._CTW.ENABLE_OP)
            # self.SDO_Write(node - 1, [0x2062, 0x00], [0x80, 0x4F, 0x12])
            self.SDO_Write(node-1, [0x6040, 0x00], [0x0F, 0x00, 0x00, 0x00])
    def recover(self):
        """
        Recovery method for when a software related issue has arisen. Will not reset the emergency stop
        module.
        :return: None
        TODO: Enable status bit check to enable proper recovery
        """
        self.NMT_Write([self._CTW.RESET])
        self.NMT_Write([self._CTW.ENABLE_OP])
        sleep(2)
        # self.NMT_Write([self._CTW.ENABLE_OP])
        self.NMT_Write([self._CTW.ENABLE])
        for node in self._CAN_NODES:
            # self.CAN.NMTwrite(node.id, self._CTW.ENABLE_OP)
            # self.SDO_Write(node - 1, [0x2062, 0x00], [0x80, 0x4F, 0x12])
            self.SDO_Write(node-1, [0x6040, 0x00], [0x0F, 0x00, 0x00, 0x00])

    def AddPeriodicTask(self, COBID: int, data: list, period: float):
        """

        :param COBID:
        :param data:
        :param period:
        :return:
        """
        request = CANPeriodicTask.Request()
        request.command = "Add"
        request.cobid = COBID # 0x700 + COBID.HOST
        request.data = data
        request.period = period
        response = self.PeriodicSrvCli.call_async(request)
        rclpy.spin_until_future_complete(self, response)
        return response.result().success
    def RemovePeriodicTask(self, COBID:int, data: list=[]):
        """

        :param COBID:
        :param data:
        :return:
        """

        request = CANPeriodicTask.Request()
        request.command = "Remove"
        request.cobid = COBID  # 0x700 + COBID.HOST
        request.data = data
        response = self.PeriodicSrvCli.call_async(request)
        rclpy.spin_until_future_complete(self, response)
        return response.result().success
    def Subscribe(self, COBID:int):
        """
        Subscribe "override" method, to subscribe to specific COBIDs in the CANBUS node
        :param COBID: COBID of the desired object
        :return: None
        """
        Subscribe_req = CANSubscribe.Request()
        Subscribe_req.command = "Add"
        Subscribe_req.cobid = COBID
        response = self.SubscribeSrvCli.call_async(Subscribe_req)
        rclpy.spin_until_future_complete(self, response)
        return response.result().success
    def Unsubscribe(self, COBID:int):
        """
                Subscribe "override" method, to subscribe to specific COBIDs in the CANBUS node
                :param COBID: COBID of the desired object
                :return: None
                """
        Subscribe_req = CANSubscribe.Request()
        Subscribe_req.command = "Remove"
        Subscribe_req.cobid = COBID
        success = False
        i = 0

        response = self.SubscribeSrvCli.call_async(Subscribe_req)
        for i in range(10):
            rclpy.spin_until_future_complete(self, response)
            success = response.result().success
            if success == True:
                break
            else:
                response = self.SubscribeSrvCli.call_async(Subscribe_req)
    def NMT_Write(self, data: list):
        """
        NMT write "override" method, to write NMT messages to the canbus node
        for readability
        :param node_id:
        :param data:
        :return:
        """
        NMT_msg = CANWrite()
        NMT_msg.command = "NMT"
        NMT_msg.data = data
        self.WritePub.publish(NMT_msg)
    def SDO_Write(self, node_id: int, indices: list, data: list):
        """
        SDO write "override" method, to write SDO messages to the canbus node
        for readability
        :param node_id:
        :param data:
        :return:
        """

        SDO_msg = CANWrite()
        SDO_msg.command = "SDO"
        SDO_msg.node_id = node_id
        SDO_msg.indices = indices
        SDO_msg.data = data
        self.WritePub.publish(SDO_msg)
    def PDO_Write(self, COBID: int, data: list):
        """
        PDO write "override" method, to write PDO messages to the canbus node
        for readability
        :param COBID:
        :param data:
        :return:
        """

        PDO_msg = CANWrite()
        PDO_msg.command = "PDO"
        PDO_msg.cobid = COBID
        PDO_msg.node_id
        PDO_msg.data = data
        self.WritePub.publish(PDO_msg)
    def Subscription_CB(self, message):
        return None
        # if COBID in self._COBID.ACT_CURRENT.ALL:
        #     current = int.from_bytes(data, 'little', signed=True)
        #     current_amps = current * (pow(2, 13) / 40.0) # to amps
        #     node_id = COBID - 0x380
        #     self._CURRENT_PERIODIC[node_id-1] = current_amps
        # else:
        #     self.logger.log(logging.ERROR, f"COBID {COBID} not recognised")
        #
        # if COBID in self._COBID.ACT_VELOCITY.ALL:
        #     velocity = int.from_bytes(data, 'little', signed=True)
        #     velocity_mps = velocity / ((((pow(2, 17) / (2 * 20000) * pow(2, 19)) / 1000) * 32) * (((2.0 * 3.14) / 60.0) * 0.28)) # To MPS
        #     node_id = COBID - 0x370
        #     self._VELOCITY_PERIODIC[node_id-1] = velocity_mps
        # else:
        #     self.logger.log(logging.ERROR, f"COBID {COBID} not recognized")
        #
        # if COBID in self._COBID.HEARTBEAT.ALL:
        #     status = int.from_bytes(data, 'little', signed=True)
        #     nodeid = COBID - 0x700
        #     if status == 0x85 or status == 0x05:
        #         self._STATUS_PERIODIC[nodeid-1] = 'OPERATIONAL'
        #     elif status == 0x84 or status == 0x04:
        #         self._STATUS_PERIODIC[nodeid-1] = 'STOPPED'
        #     elif status == 0xFF or status == 0x7F:
        #         self._STATUS_PERIODIC[nodeid-1] = 'PRE-OPERATIONAL'
        #     else:
        #         self._STATUS_PERIODIC[nodeid-1] = 'UNKNOWN'
def main():
    rclpy.init()
    ctrl = RobuROC_CTRL()
    ctrl.setup()

    try:
        time.sleep(1)
        rclpy.spin(ctrl)
    except Exception as e:
        print(e)
    finally:
        ctrl.destroy_node()
        rclpy.shutdown()
if __name__ == '__main__':
    main()