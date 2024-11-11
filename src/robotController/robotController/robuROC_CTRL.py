import canopen, logging, os, COBID, CTW

import rclpy.subscription
from rclpy.node import Node
import std_msgs
from src.robotController.robotController.robuROC_CANopen import RobuROC_Canopen

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("CAN_Logs"),
                              logging.StreamHandler()])

class ROBUROC_CTRL(Node, RobuROC_Canopen):

    # Initialize fields to contain periodic status updates
    _CURRENT_PERIODIC = [None, None, None, None]
    _VELOCITY_PERIODIC = [None, None, None, None]
    _STATUS_PERIODIC = [None, None, None, None]
    _TEMPORARY_PERIODIC = [None, None, None, None]

    # Initialize logging
    logger = logging.getLogger("CAN")

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

    def __init__(self):
        super().__init__('RobuROC_CTRL')

        self._CTW = CTW.CTW()
        self._COBID = COBID.COBID()

        while self._CONNECTED == False:
            self._CONNECTED = self.Connect()
        self.InitHeartbeat()


        self.velocity_Sub = rclpy.subscription.Subscription(std_msgs)


    def setup(self):
        """
        Setup for the RobuROC-4 (pre-configured) CANBus
        :return: None
        """
        # If the system is already initialized, stop it and reset everything
        if self._CONNECTED:
            self.CAN_NETWORK.disconnect()
            for node in self.CAN_NODES:
                # Reset all drives
                # node.nmt.send_command(0x81, 0)
                self.NMTwrite(node.id, self._CTW.RESET)
                # Set deceleration on all drives
                self.SDOwrite(node.id, [0x20, 0x64, 0x04], [0x80, 0x4F, 0x12])
                # Enable all drives
                # node.nmt.send_command(0x01, 0)
                self.NMTwrite(node.id, self._CTW.ENABLE)
                # Turn on all drives
                # node.nmt.send_command(0x07, 0)
                self.NMTwrite(node.id, self._CTW.TURNON)
                # Enable operatiom on all drives
                # node.nmt.send_command(0x0F, 0)
                self.NMTwrite(node.id, self._CTW.ENABLE_OP)

            if not self._PERIODIC:
                self.InitPeriodic()
            if not self._HEARTBEAT:
                self.InitHeartbeat()

            self.Connect()
            self._CONNECTED = True
    def InitHeartbeat(self, heartbeat_time_ms: int = 200):
        """
        Initialize heartbeat messages where the host (Node 0) is the producer
        and the nodes are consumers.

        :param heartbeat_time_ms: Time interval in milliseconds for sending heartbeat messages.
        """

        self.PeriodicTask(0x700 + self._COBID.HOST, [0], heartbeat_time_ms)
        self.logger.log(logging.DEBUG, f"Heartbeat initialized to {heartbeat_time_ms} ms")
        self._HEARTBEAT = True
    def InitPeriodic(self):
        """
        Initialize periodic read TPDO messages, such that it returns with periodic updates to the state of the drives
        and motors.
        :return: None
        """
        for node in self.CAN_NODES:
            # Subscribe to Actual Current and Velocity, Status messages and SDO read feedback
            self.Subscribe(self._COBID.ACT_CURRENT.ALL[node.id-1], self.SDO_Current_Callback)
            self.Subscribe(self._COBID.ACT_VELOCITY.ALL[node.id-1], self.SDO_Velocity_Callback)
            self.Subscribe(self._COBID.HEARTBEAT.ALL[node.id-1], self.SDO_Status_Callback)
            # self.Subscribe(self._COBID.SDO_READ.ALL[node.id-1], self.SDO_Callback)
        self._PERIODIC = True
    def setSpeed(self, speed, type:str='MPS'):
        """
        Method for setting the speed of the individual wheels
        :param speed: A list of speeds for the individual wheels
        :param type: Speed representation, current supported values: ['MPS', 'RPM']
        :return: None
        """
        for node in self.CAN_NODES:
            # Set the mode to velocity mode
            self.SDOwrite(node.id, [0x60, 0x60, 0x00], [0x03])

            # If the system is not in operation mode
            if self._STATUS_PERIODIC[node.id-1] == 'OPERATIONAL':
                self.recover()
                self.NMTwrite(node.id, self._CTW.ENABLE_OP)

            data = list(speed.to_bytes(4, byteorder='little', signed=True))
            self.SDOwrite(node.id, [0x60, 0xFF, 0x00], data)
    def brake(self, node_id):
        """
        Method for braking the RobuROC4 when velocity is set to 0.
        :param node_id: The node for which to change the state to Quickstop
        :return: None
        """
        self.NMTwrite(node_id, self._CTW.QUICKSTOP)
    def recover(self):
        """
        Recovery method for when a software related issue has arisen. Will not reset the emergency stop
        module.
        :return: None
        TODO: Enable status bit check to enable proper recovery
        """
        for node in self.CAN_NODES:
            if self._STATUS_PERIODIC[node.id-1] == 'STOPPED' or self._STATUS_PERIODIC[node.id-1] == 'UNKNOWN':
                self.NMTwrite(node.id, self._CTW.ENABLE)
                self.NMTwrite(node.id, self._CTW.ENABLE_OP)
                self.NMTwrite(node.id, self._CTW.TURNON)
    # def SDO_Callback(self, COBID:int, data:bytearray, flags:float):
    #
    #     if COBID in self._COBID.SDO_READ.ALL:
    #         # An SDO request has returned a value
    #         node_id = COBID - 0x580
    #         index = int.from_bytes(data[0:3], 'little', signed=True)
    #         subindex = int.from_bytes(data[4], 'little', signed=False)
    #         data = list(data)
    #         self._TEMPORARY_PERIODIC[node_id] = [index, subindex, data]
    #     else:
    #         self.logger.log(logging.ERROR, f"COBID {COBID} not recognized")
    def SDO_Velocity_Callback(self, COBID:int, data:bytearray, timestamp:float):
        """
        Callback function for velocity, measuring in the driver/motor. It updates the internal values _VELOCITY_PERIODIC
        with these values
        :param COBID: COBID returned as sender from the driver
        :param data: data returned from the CANBus
        :param timestamp: returned from the CANBus
        :return: None
        """
        if COBID in self._COBID.ACT_VELOCITY.ALL:
            velocity = int.from_bytes(data, 'little', signed=True)
            velocity_mps = velocity / ((((pow(2, 17) / (2 * 20000) * pow(2, 19)) / 1000) * 32) * (((2.0 * 3.14) / 60.0) * 0.28)) # To MPS
            node_id = COBID - 0x370
            self._VELOCITY_PERIODIC[node_id-1] = velocity_mps
        else:
            self.logger.log(logging.ERROR, f"COBID {COBID} not recognized")
    def SDO_Current_Callback(self, COBID:int, data:bytearray, timestamp:float):
        """
        Callback function for Current, measured in the driver/motor. It updates the internal values _CURRENT_PERIODIC
        with these values.
        :param COBID: COBID returned as sender from the driver
        :param data: data returned from the CANBus
        :param timestamp: returned from the CANBus
        :return: None
        """
        if COBID in self._COBID.ACT_CURRENT.ALL:
            current = int.from_bytes(data, 'little', signed=True)
            current_amps = current * (pow(2, 13) / 40.0) # to amps
            node_id = COBID - 0x380
            self._CURRENT_PERIODIC[node_id-1] = current_amps
        else:
            self.logger.log(logging.ERROR, f"COBID {COBID} not recognised")
    def SDO_Status_Callback(self, COBID:int, data:bytearray, timestamp:float):
        if COBID in self._COBID.HEARTBEAT.ALL:
            status = int.from_bytes(data, 'little', signed=True)
            nodeid = COBID - 0x700
            if status == 0x85 or status == 0x05:
                self._STATUS_PERIODIC[nodeid-1] = 'OPERATIONAL'
            elif status == 0x84 or status == 0x04:
                self._STATUS_PERIODIC[nodeid-1] = 'STOPPED'
            elif status == 0xFF or status == 0x7F:
                self._STATUS_PERIODIC[nodeid-1] = 'PRE-OPERATIONAL'
            else:
                self._STATUS_PERIODIC[nodeid-1] = 'UNKNOWN'
    @property
    def Velocity(self):
        return self._VELOCITY_PERIODIC
    @property
    def Current(self):
        return self._CURRENT_PERIODIC
    @property
    def Status(self):
        return self._STATUS_PERIODIC


