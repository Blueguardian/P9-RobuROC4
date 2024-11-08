"""
Created for Lunar surface preparation project
9. Semester, Robotics, 2024 Fall Semester
Group 962
"""

import canopen, logging, os, COBID, CTW

# Make directory for logs locally
if not os.path.join(os.curdir, "logs"):
    os.mkdir("logs", 0o777)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("CAN_Logs"),
                              logging.StreamHandler()])

class RobuROC_Canopen():
    """
    The RobuROC_Canopen class is constructed to communicate with the DPCANTR-040B080 drives installed in the
    RobuROC4. The methods implemented here are defined such that the low level CANBus communication is simplified to the
    extent possible. When utilized, it will establish and maintain communication with these drivers.
    """

    _DRIVE_CONFIG = os.path.join(os.path.abspath("../"), "resource", "AMC_Digiflex_1.0.14.eds")

    def __init__(self):
        self.logger = logging.getLogger("CAN")

        # Initialize a network object
        self.CAN_NETWORK = canopen.Network()
        self.CAN_NODES = []
        self._CAN_SUBSCRIPTION = []
        self._CAN_PERIODICTASK = []
        self._CONNECTED = False
    def Connect(self, bustype:str = 'pcan', channel:str = 'PCAN_USBBUS1', bitrate:int = 1000000):
        """
        Connection method for attempting to connect to the CANBUS network specified by bustype and channel at the specified
        bitrate.
        :param bustype: type of CANBus
        :param channel: Connection channel (or object), defined bu the interface to the CANBus
        :param bitrate: The bitrate for the connection
        :return: Bool: true or false for connection
        """
        if not self._CONNECTED:
            try:
                self.CAN_NETWORK.connect(bustype=bustype, channel=channel, bitrate=bitrate)
                self._CONNECTED = True
                if len (self.CAN_NODES) == 0:
                    try:
                        for i in range(1,5):
                            node = self.CAN_NETWORK.add_node(i, self._DRIVE_CONFIG)
                            self.CAN_NODES.append(node)
                    except Exception as e:
                        self.logger.log(logging.ERROR, f"Unable to initialize nodes, Error: {e}")
                        self._CONNECTED = False
            except Exception as error:
                self.logger.log(logging.ERROR, f"Unable to connect to CAN Bus, Error: {error}")
                self._CONNECTED = False
            finally:
                return self._CONNECTED
    def Disconnect(self):
        """
        Disconnection method for disconnection the CANBUS network and stopping/ending all
        related subscriptions and periodic tasks
        :return: Bool: True or False for successful disconnection
        """
        if self._CONNECTED:
            try:
                self.CAN_NETWORK.disconnect()
                # It is here assumed that the HeartBeat and Periodic status checks are enabled
                if len(self._CAN_PERIODICTASK) != 0:
                    try:
                        for task in self._CAN_PERIODICTASK:
                            task.stop()
                        for id in self._CAN_SUBSCRIPTION:
                            self.CAN_NETWORK.unsubscribe(id)
                    except Exception as error:
                        self.logger.log(logging.ERROR, f"Unable to shutdown periodic loop, Error: {error}")
            except Exception as error:
                self.logger.log(logging.ERROR, f"Unable to disconnect from CAN Bus, Error: {error}")
            finally:
                return not self._CONNECTED
        else:
            return True
    def PeriodicTask(self, COB_ID: int, data: list, period: int = 200):
        """
        Adds a CANOpen periodically sent message, e.g. for heartbeat. This task is stored should it later be
        required to be stopped.
        :param COB_ID: COBID of the intended target
        :param data: Data to be sent periodically
        :param period: The period between messages in ms
        :return: Bool: True or False for successful periodic task addition
        """
        sent_data = None
        if len(data) <= 8:
            # Zero-pad data if necessary
            data += [0] * (8 - len(data))
            data.reverse()
            sent_data = bytearray(data)
        try:
            task = self.CAN_NETWORK.send_periodic(COB_ID, sent_data, period)
            self._CAN_PERIODICTASK.append(task)
            return True
        except Exception as error:
            self.logger.log(logging.ERROR, f"Unable to send periodic task, Error: {error}")
            return False
    def Subscribe(self, COBID: int, callback: callable):
        """
        Adds a CANOpen subscription to a specified COBID, the return value is handled through the specified callback
        :param COBID: COBID of the intended target
        :param callback: Callback function, should contain: (COBID, data, percentage)
        :return: None
        TODO: Verify the parameters of the callback
        """
        try:
            self.CAN_NETWORK.subscribe(COBID, callback)
            self._CAN_SUBSCRIPTION.append(COBID)
            return True
        except Exception as error:
            self.logger.log(logging.ERROR, f"Unable to subscribe to {COBID}, Error: {error}")
            return False
    def PDOwrite(self, COB_ID: int, data=None):
        """
        Write data to a mapped RPDO object
        :param COB_ID: The mapped ID of the RPDO
        :param data: The data to be written (list of hexadecimals or ints).
        :return: Bool: True if successful, False if an error occurred.
        """

        if len(data) <= 8:
            data += [0] * (8 - len(data))
            # Ensure little endian format of data
            data.reverse()
            # Convert to bytes
            written_data = bytearray(data)
            try:
                self.CAN_NETWORK.send_message(COB_ID, written_data)
                return True
            except canopen.SdoCommunicationError as e:
                self.logger.log(logging.ERROR, f"PDO Write Error: {e}")
                return False
        else:
            self.logger.log(logging.ERROR, f"Message length over 8 bits is not supported")
            return False
    def SDOwrite(self, node_id: int, pdo_index: list, data: list):
        """
        Write data to a specified PDO for the given node.
        :param node_id: The ID of the node to write to.
        :param pdo_index: A list of the index and subindex of the pdo as in [index bit 0, index bit 1, subindex bit], e.g. [0x60, 0x60, 0x00] for index 0x6060 subindex 0x00
        :param data: The data to be sent (as a list of hexadecimals or ints).
        :return: Bool: True if the write operation was successful, False otherwise.

        TODO: Enable support for multiple lengths of data
        """
        # Setup the index sequence to send to the node
        index_data = bytearray([0x22, pdo_index[1], pdo_index[0], pdo_index[2]])

        if len(data) <= 4:
            data += [0] * (4 - len(data))
            # Ensure little endian format of data
            data.reverse()
            # Convert to bytes
            written_data = bytearray(data)
            try:
                self.CAN_NETWORK.send_message(0x600 + node_id, index_data + written_data)
                return True
            except canopen.SdoCommunicationError as e:
                self.logger.log(logging.ERROR, f"PDO Write Error: {e}")
                return False
        else:
            self.logger.log(logging.ERROR, f"Message length over 8 bits is not supported")
            return False
    def SDOread(self, node_id: int, pdo_index: list):
        """
        Retrieve the current data from the specified PDO for the given node.
        :param node_id: The ID of the node to read from.
        :param pdo_index: A list of the index and subindex of the pdo as in [index bit 0, index bit 1, subindex bit], e.g. [0x60, 0x60, 0x00] for index 0x6060 subindex 0x00
        return: Returned with callback with node id 0x580 + nodeid

        TODO: Enable support for multiple data lengths
        """
        self.CAN_NETWORK.check()
        try:
            # Setup the data package in little endian format
            # Thus  ['Read request id', 'least significant bit of index', 'most significant bit of index', 'subindex bit']
            data = [0x40, pdo_index[1], pdo_index[0], pdo_index[2]]
            # Send a read request to the specified node with the index to read from
            self.CAN_NETWORK.send_message(0x600 + node_id, bytearray(data))
        except Exception as e:
            self.logger.log(logging.ERROR, f"Error writing to node: {node_id}: {e}")
            return None
    def NMTwrite(self, node_id: int, ctrlWord: int):
        data = [ctrlWord, node_id]
        self.CAN_NETWORK.send_message(0x00, bytearray(data))
    # def PDOread(self, node_id: int, index: int, subindex: int = 0, timeout: int = 1, timeout_count = 5):
    #     """
    #     Read data from an SDO on the specified CANopen node.
    #     :param node_id: The ID of the node to read from.
    #     :param index: The index in the object dictionary to read from.
    #     :param subindex: The subindex in the object dictionary.
    #     :param timeout: Timeout in seconds for the operation.
    #     :return: Data read from the node, or raises an exception on failure.
    #     """
    #     timeout_counter = 0
    #     try:
    #         node = self._CAN_NODES[node_id-1]
    #         # Read the data from the specified index and subindex using SDO
    #         data = node.sdo[index][subindex].read(timeout=timeout)
    #         return data
    #     except canopen.SdoCommunicationError as e:
    #         self.logger.log(logging.ERROR, f"SDO Read Error: {e}")
    #         raise
    #     except TimeoutError:
    #         self.logger.log(logging.ERROR, f"SDO read timed out after {timeout} seconds")
    #         while timeout_counter < timeout_count:
    #             try:
    #                 node = self._CAN_NODES[node_id-1]
    #                 data = node.sdo[index][subindex].read(timeout=timeout)
    #                 timeout_counter += 1
    #                 return data
    #             except TimeoutError:
    #                 self.logger.log(logging.ERROR, f"SDO read timed out after {timeout} seconds")
    #         raise