import canopen
import time
import math
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("event.log"),
                              logging.StreamHandler()])






# Object indexes for configuration
INDEX_HEARTBEAT = 0x1016
SUBINDEX_HEARTBEAT = 1


INDEX_DECELERATION_LIMIT = 0x2062
SUBINDEX_DECELERATION_LIMIT = 4


class MotorControl:
    """
    Controller for the RobuROC4 - Windows
    """
    _MAXSPEED = 2 # m/s
    _WHEEL_RAD = 0.28 # Meter
    _MODES =  {"VELOCITY": 3, "CURRENT": 4} # Operation modes
    _CANREADY = False #
    _READY = False
    _CONNECTION = None
    _PERIODIC_ENABLE = False

    _CURRENT_PERIODIC = [None, None, None, None]
    _VELOCITY_PERIODIC = [None, None, None, None]
    _TEMPORARY_PERIODIC = [None, None, None, None]
    _HEART_PERIODIC = None

    controlMode = 0

    ## CAN bus constants ##
    # CAN bus IDs for ControlWord
    _COBID_HOST = 0x05

    _COBID_CONTROL = [0x201, 0x202, 0x203, 0x204]

    _COBID_COM_VELOCITY = [0x301, 0x302, 0x303, 0x304]

    # CAN bus IDs for readying velocity and current from motor controllers
    _COBID_ACT_VELOCITY = [0x371, 0x372, 0x373, 0x374]
    _COBID_ACT_CURRENT = [0x381, 0x382, 0x383, 0x384]

    _COBID_MODE = [0x501, 0x502, 0x503, 0x504]
    _COBID_TAR_VELOCITY = [0x511, 0x512, 0x513, 0x514]
    _COBID_TAR_CURRENT = [0x521, 0x522, 0x523, 0x524]
    _COBID_SDO = [0x601, 0x602, 0x603, 0x604]
    _COBID_SDO_RETURN = [0x581, 0x582, 0x583, 0x584]
    _COBID_HEARTBEAT = [0x701, 0x702, 0x703, 0x704]
    _COBID_RESET = [0x81, 0]

    # Scaling constants
    _SCALE_CURRENT = pow(2, 13) / 40.0  # to Amps
    _SCALE_SETCURRENT = pow(2, 15) / 40.0  # to Amps
    _SCALE_VELOCITY = ((pow(2, 17) / (2 * 20000) * pow(2, 19)) / 1000) * 32  # To RPM
    _SCALE_RPM_TO_MPS = ((2.0 * 3.14) / 60.0) * _WHEEL_RAD

    setpointSpeed = [0, 0, 0, 0]


    errors = []

    # Arrays to hold actual values
    actualCur = [0, 0, 0, 0]
    actualVel = [0, 0, 0, 0]

    velocityDeadzone = 0.05

    # Arrays to hold periodic can objects

    def __init__(self, log):

        self.logger = logging.getLogger('RoboROC4')
        self.Connect()

    @property
    def ready(self):
        return self._CANREADY


    # CAN Bus related connectivity
    def Disconnect(self):
        # Make sure to kill CAN network when not using it
        if self._PERIODIC_ENABLE:
            for i in range(4):
                self._VELOCITY_PERIODIC[i].stop()
                self._CURRENT_PERIODIC[i].stop()

            self._HEART_PERIODIC.stop()
            self._PERIODIC_ENABLE = False

        if self._CANREADY:
            self._NETWORK.disconnect()
            self._CANREADY = False
    def Connect(self):

        if not self._CANREADY:
            try:
                self._NETWORK = canopen.Network()
                self._NETWORK.connect(bustype='pcan', channel='PCAN_USBBUS1', bitrate=1000000)
                self._CANREADY = True
            except Exception as error:
                self.logger.log(logging.ERROR, f"Unable to connect to CAN Bus, Error: {error}")
                self._CANREADY = False
    def Setup(self):
        internal_iterator = 0
        if self._CANREADY:
            # Stop earlier, if any, connections
            self.Disconnect()

            # Reset all drives
            self._resetDrive()
            time.sleep(0.5)

            # Setup stop deceleration limit (for smooth stop with quickStop)
            self._setDeceleration(12000000)

            # Re-enable the drives
            self._enableComm()

            # Enter Power Enabled
            self.switchOn()

            # Enter Operation Enable (ready to drive)
            self._enableOperation()

            if not self._PERIODIC_ENABLE:
                self.InitializeHeartbeat()
                self.InitializePeriodic()
                self._PERIODIC_ENABLE = True

            self._READY = True
        elif internal_iterator < 5:
            self.Connect()
            self.Setup()
        else:
            self._READY = False
            self.logger.log(logging.ERROR, f"Unable to connect to CAN Bus")
            # self.dynamicBrake()
    def Shutdown(self):
        # Shutdown the drives with a PDO message
        # Shutdown command: 0x06
        data = [0x06, 0]
        for i in range(4):
            self._SendCanPacket(self._COBID_CONTROL[i], data)
        self._disableComm()
        # Why not disableOperation?
    def StartUp(self):
        # Turn on the drives with PDO message
        # Switch on command: 0x07
        data = [0x07, 0]
        for i in range(4):
            self._SendCanPacket(self._COBID_CONTROL[i], data)
        # Test
        self._enableComm()
    def InitializePeriodic(self):
        # RTR - Actual Current
        for i in range(4):
            self._CURRENT_PERIODIC[i] = self._NETWORK.send_periodic(self._COBID_ACT_CURRENT[i], 8, .2, remote=True)
            self._NETWORK.subscribe(self._COBID_ACT_CURRENT[i], self.readPeriodic)

        # RTR - Actual Velocity
        for i in range(4):
            self._VELOCITY_PERIODIC[i] = self._NETWORK.send_periodic(self._COBID_ACT_VELOCITY[i], 8, .025, remote=True)
            self._NETWORK.subscribe(self._COBID_ACT_VELOCITY[i], self.readPeriodic)

        # SDO - Temperature
        # for i in range(4):
        # packet = self.sdoPacket( 0x2021, 0x01 )
        # self.tempPeriodic[i] = self.network.send_periodic( COBID_SDO[i], packet, .1, remote=False)
        # self.network.subscribe( COBID_SDO_RETURN[i], self.readPeriodic)
    def InitializeHeartbeat(self):

        # Consumer Heartbeat object address is 0x1016, with sub-index 01 (page 75 comm manual)

        # Consumertime Limited between 1-65535 (16-bit unsigned int)
        consumerTime = 200  # ms
        timeInBytes = (consumerTime).to_bytes(2, byteorder="little", signed=False)

        data = list(timeInBytes)
        data.append(self._COBID_HOST)  # Configure all motor driver nodes to listen for heartbeat from HOST

        for i in range(4):
            self._sdoWrite(self._COBID_SDO[i], data, INDEX_HEARTBEAT, SUBINDEX_HEARTBEAT)

        time.sleep(0.1)

        # Begin heartbeat

        self._HEART_PERIODIC = self._NETWORK.send_periodic(0x700 + self._COBID_HOST, [0], 0.1, remote=False)

    # CAN Bus interactive
    def readPeriodic(self, canid, data):

        value = int.from_bytes(data, byteorder='little', signed=True)

        if canid in self._COBID_SDO_RETURN:
            # SDO data returned
            index = int.from_bytes(data[1:3], byteorder='little', signed=False)
            subindex = data[3]

            # Temperature
            if index == 0x2021 and subindex == 0x02:
                value = int.from_bytes(data[4:8], byteorder='little', signed=True)
                print(canid, list(data), round(value / pow(2, 16), 4))

        if canid in self._COBID_ACT_CURRENT:

            if ((canid - 897 + 1) in [2, 3]):
                value = -value

            scaled = round(value / self._SCALE_CURRENT, 4)
            index = int(self._COBID_ACT_CURRENT.index(canid))
            self.actualCur[index] = scaled

        # Returned velocity
        if canid in self._COBID_ACT_VELOCITY:
            if ((canid - 881 + 1) in [2, 3]):
                value = -value

            scaled = round(value / self._SCALE_VELOCITY * self._SCALE_RPM_TO_MPS, 4)
            index = int(self._COBID_ACT_VELOCITY.index(canid))
            self.actualVel[index] = scaled if abs(scaled) > self.velocityDeadzone else 0.0;
    def setMode(self, mode):

        # Control word ( enable operation )
        prepend = [0x0F, 0]

        # Only change mode if the current mode is different
        if self.controlMode != mode:
            data = (mode).to_bytes(1, byteorder="little", signed=True)

            for i in range(4):
                self._SendCanPacket(self._COBID_MODE[i], prepend + list(data))

            self.controlMode = mode
    def setRPS(self, index=0, rad=0):
        speed = (rad * 60.0 / (2 * math.pi)) * self._SCALE_VELOCITY

        # Why int? If output is float?
        self._setSpeed(index, int(speed))
    def setMPS(self, index=0, mps=0):
        # Convert speed (m/s) to motor speed value
        speed = mps * (self._SCALE_VELOCITY / self._SCALE_RPM_TO_MPS)
        self._setSpeed(index, int(speed))
    def setRPM(self, index=0, rpm=0):
        # Convert speed (m/s) to motor speed value
        speed = rpm * self._SCALE_VELOCITY
        # print(speed)
        self._setSpeed(index, int(speed))
    def pause(self):
        self._quickStop()
    def start(self):
        self._enableOperation()
    def dynamicBrake(self):

        data = [0x80F, 0]
        for i in range(4):
            self._SendCanPacket(self._COBID_CONTROL[i], data)

    def _SendCanPacket(self, cobId, data):
        try:
            self._NETWORK.send_message(cobId, data)
        except Exception as error:
            self.errors.append(['CAN', "{:02x}".format(cobId) + ':' + str(data) + ' - ' + error.args[0]])

    def _quickStop(self):
        # Transitions the drives into quick stop state with a PDO message
        # Quick Stop command: 0x02
        data = [0x02, 0]
        for i in range(4):
            self._SendCanPacket(self._COBID_CONTROL[i], data)
    def _enableOperation(self):
        # Enable operation
        data = [0x0F, 0]
        for i in range(4):
            self._SendCanPacket(self._COBID_CONTROL[i], data)
    def _disableOperation(self):
        # Disable all drives with PDO message
        # To disable the voltage the drive must be in quick stop state
        # Disable Voltage command: 0x00
        data = [0x0, 0]
        for i in range(4):
            self._SendCanPacket(self._COBID_CONTROL[i], data)

    def _enableComm(self):
        # Enable all drives with global NMT command
        # Enable command: 0x01
        self._SendCanPacket(0, [0x1, 0])
    def _disableComm(self):
        # Transitions the drives into quick stop state with a NMT message
        # Stop command: 0x02
        self._SendCanPacket(0, [0x02, 0])
    def _resetDrive(self):
        # Reset all drives with one global NMT command
        # Reset command: 0x81
        self._SendCanPacket(0, self._COBID_RESET)
    def _setDeceleration(self, value):

        valueBytes = (value).to_bytes(4, byteorder="little", signed=True)
        data = list(valueBytes)

        for i in range(4):
            self._sdoWrite(self._COBID_SDO[i], data, INDEX_DECELERATION_LIMIT, SUBINDEX_DECELERATION_LIMIT)
    def _sdoWrite(self, COBID=0, data=None, index=0, subindex=0):

        if (len(data) <= 4):

            # Command byte for writing 4 bytes SDO
            # 0x22 describes this that is is a 4 byte SDO message from host
            commandByte = [0x22]

            # Convert object index into two bytes and append the subindex
            indexBytes = list((index).to_bytes(2, byteorder="little", signed=False))
            indexBytes.append(subindex)

            data = commandByte + indexBytes + data

            # Append zeroes if data is less than 8 bytes long
            for i in range(8 - len(data)):
                data.append(0)

            # Now send message over CAN-network
            # print('[{}]'.format(', '.join(hex(x) for x in data)))

            self._SendCanPacket(COBID, data)

        else:
            raise NotImplementedError("Data lenght is not supported")
    # Not Used?
    def _sdoRead(self, COBID=0, index=0, subindex=0):

        data = self._sdoPacket(index, subindex)

        self._SendCanPacket(COBID, data)

        # Now read packet from PCAN-VIEW <3
    def _sdoPacket(self, index=0, subindex=0):

        commandByte = [0x40]

        # Convert object index into two bytes and append the subindex
        indexBytes = list((index).to_bytes(2, byteorder="little", signed=False))
        indexBytes.append(subindex)

        data = commandByte + indexBytes

        # Append zeroes if data is less than 8 bytes long
        for i in range(8 - len(data)):
            data.append(0)

        return data
    def _setSpeed(self, index=0, speed=0):
        if self._READY:
            if isinstance(speed, int):
                # Convert speed to bytearray for sending over CAN
                # print( "Speed: " , speed )
                # if speed == 0:
                # Change mode
                # self.setMode(MODE_CURRENT)

                # Set current to zero, dont use velocity
                # current = 0

                # data = (current).to_bytes(4, byteorder="little", signed=True)
                # self.sendCanPacket( COBID_TAR_CURRENT[index], [0] )
                # else:

                # Change mode
                self.setMode(self._MODES['VELOCITY'])

                data = speed.to_bytes(4, byteorder="little", signed=True)
                self._SendCanPacket(self._COBID_TAR_VELOCITY[index], list(data))

            else:
                raise TypeError('Unvalid speed type')
    # Not used?
    def _setCurrent(self, index=0, current=0):

        if self._READY:
            value = int(current * self._SCALE_SETCURRENT)

            self.setMode(self._MODES['CURRENT'])

            data = (value).to_bytes(4, byteorder="little", signed=True)
            self._SendCanPacket(self._COBID_TAR_CURRENT[index], list(data))














# Read Ki
# mc.sdoRead( const.COBID_SDO[0], 0x2032, 0x08 )

# Read Ks
# mc.sdoRead( const.COBID_SDO[0], 0x20D8, 0x24 )

# Read Resolver resolution
# mc.sdoRead( const.COBID_SDO[0], 0x2032, 0x06 )