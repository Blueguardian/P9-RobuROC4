import math, logging, CTW
from src.Gamepad.Gamepad import gamepad
from rclpy.node import Node

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("event.log"),
                              logging.StreamHandler()])






# Object indexes for configuration
INDEX_HEARTBEAT = 0x1016
SUBINDEX_HEARTBEAT = 1


INDEX_DECELERATION_LIMIT = 0x2062
SUBINDEX_DECELERATION_LIMIT = 4


class MotorControl(Node):
    """
    Controller for the RobuROC4 - Ubuntu - ROS2
    """
    MODES = {"VELOCITY": 3, "CURRENT": 4} # Operation modes

    _CURRENT_PERIODIC = [None, None, None, None]
    _VELOCITY_PERIODIC = [None, None, None, None]
    _TEMPORARY_PERIODIC = [None, None, None, None]
    _HEART_PERIODIC = None

    # Public variables
    MAX_SPEED = 2  # Meters per second
    WHEEL_RADIUS = 0.28  # Meters

    # Constants
    _SCALE_CURRENT = pow(2, 13) / 40.0  # to Amps
    _SCALE_SETCURRENT = pow(2, 15) / 40.0  # to Amps
    _SCALE_VELOCITY = ((pow(2, 17) / (2 * 20000) * pow(2, 19)) / 1000) * 32  # To RPM
    _SCALE_RPM_TO_MPS = ((2.0 * 3.14) / 60.0) * WHEEL_RADIUS

    setpointSpeed = [0, 0, 0, 0]

    # Arrays to hold actual values
    actualCur = [0, 0, 0, 0]
    actualVel = [0, 0, 0, 0]


    def __init__(self, log):
        super().__init__('controller')

        self.logger = logging.getLogger('RoboROC4')
        self.Driver = MotorComm.MotorComm()
        self.Gamepad = gamepad.Controller()
        self._CTW = CTW.CTW


    def initialize(self):
        self.Driver.Setup()

    def setMode(self, mode:str = 'VELOCITY'):
        # Only change mode if the current mode is different
        for i in range(1,5):
            if self.Driver.SDOread(i, 0x6060, 0x00, 1) != mode.capitalize():
                data = list(self.MODES[f"{mode.capitalize()}"])
                self.Driver.SDOwrite(i, 0x6060, 0x00, data)
                
    def setRPS(self, index=0, rad=0):
        speed = (rad * 60.0 / (2 * math.pi)) * self._SCALE_VELOCITY
        self.Driver.SDOwrite(index, 0x60FF, 0x00, speed)
        
    def setMPS(self, index=0, mps=0):
        # Convert speed (m/s) to motor speed value
        speed = mps * (self._SCALE_VELOCITY / self._SCALE_RPM_TO_MPS)
        self.Driver.SDOwrite(index, 0x60FF, 0x00, speed)
        
    def setRPM(self, index=0, rpm=0):
        # Convert speed (m/s) to motor speed value
        speed = rpm * self._SCALE_VELOCITY
        self.Driver.SDOwrite(index, 0x60FF, 0x00, speed)
        
    def quickStop(self):
        for i in range(1,5):
            self.Driver.NMTwrite(i, self._CTW.QUICKSTOP)

