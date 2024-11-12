"""
Created for Lunar surface preparation project
9. Semester, Robotics, 2024 Fall Semester
Group 962

Copyright 2024 Thomas Schou Sørensen, Julian Witold Wagner and César Zacharie G Hostens

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import canopen, logging, os, asyncio

from rclpy.node import Node

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

    #_DRIVE_CONFIG = os.path.join(os.path.abspath("../../"), "resource", "AMC_Digiflex_1.0.14.eds")
    _SDO_ABORT_CODES  = {
        0x00000503: "Toggle bit not alternated",
        0x00000504: "SDO protocol timed out",
        0x00010504: "Command specifier not valid",
        0x00020504: "Invalid block size (block mode only, see DS301)",
        0x00030504: "Invalid sequence number (block mode only, see DS301)",
        0x00040504: "CRC error (block mode only, see DS301)",
        0x00050504: "Out of memory",
        0x00000601: "Unsupported access to an object",
        0x00010601: "Attempt to read a write only object",
        0x00020601: "Attempt to write a read only object",
        0x00000602: "Object does not exist in the object dictionary",
        0x00410604: "Object cannot be mapped to the PDO",
        0x00420604: "The number and length of the objects to be mapped would exceed PDO length",
        0x00430604: "General parameter incompatibility reason",
        0x00470604: "General internal incompatibility in the device",
        0x00000606: "Access failed due to a hardware error",
        0x00100607: "Data type does not match, length of service parameter does not match",
        0x00120607: "Data type does not match, length of service parameter too high",
        0x00130607: "Data type does not match, length of service parameter too low",
        0x00110609: "Sub-index does not exist",
        0x00300609: "Value range of parameter exceeded (only for write access)",
        0x00310609: "Value of parameter written too high",
        0x00320609: "Value of parameter written too low",
        0x00360609: "Maximum value is less than minimum value",
        0x00000800: "General error",
        0x00200800: "Data cannot be transferred or stored to the application",
        0x00210800: "Data cannot be transferred or stored to the application because of local control",
        0x00220800: "Data cannot be transferred or stored to the application because of present device state",
        0x00230800: "Object dictionary dynamic generation fails or no object dictionary is present (object dictionary loads from file and file error occurred)"
    }
    CAN_NETWORK = canopen.Network()

    def __init__(self):
        self.logger = logging.getLogger("CANBUS")

        # Initialize a network object
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
                            node = self.CAN_NETWORK.add_node(i)
                            self.CAN_NODES.append(node)
                    except Exception as e:
                        self.logger.error(f"Unable to initialize nodes, Error: {e}")
                        self._CONNECTED = False
            except Exception as error:
                self.logger.error(f"Unable to connect to CAN Bus, Error: {error}")
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
                            self._CAN_PERIODICTASK.remove(task)
                        for id in self._CAN_SUBSCRIPTION:
                            self.Unsubscribe(id)
                    except Exception as error:
                        self.logger.error(f"Unable to shutdown periodic loop, Error: {error}")
            except Exception as error:
                self.logger.error(f"Unable to disconnect from CAN Bus, Error: {error}")
            finally:
                return not self._CONNECTED
        else:
            return True
    def PeriodicTask(self, COB_ID: int, data: list, period: float = 0.2):
        """
        Adds a CANOpen periodically sent message, e.g. for heartbeat. This task is stored should it later be
        required to be stopped.
        :param COB_ID: COBID of the intended target
        :param data: Data to be sent periodically
        :param period: The period between messages in seconds
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
            self.logger.error(f"Unable to send periodic task, Error: {error}")
            return False
    def Subscribe(self, COBID: int, callback: callable):
        """
        Adds a CANOpen subscription to a specified COBID, the return value is handled through the specified callback
        :param COBID: COBID of the intended target
        :param callback: Callback function, should contain: (COBID, data, percentage), where percentage corresponds to the amount of the poackage received
        :return: None
        """
        try:
            self.CAN_NETWORK.subscribe(COBID, callback)
            self._CAN_SUBSCRIPTION.append(COBID)
            return True
        except Exception as error:
            self.logger.error(f"Unable to subscribe to {COBID}, Error: {error}")
            return False
    def Unsubscribe(self, COBID: int, callback: callable = None):
        """
        Removes a CANOpen subscription to a specific COBID
        :param COBID: COBID of the intended target
        :param callback: Callback function or None
        :return:
        """
        try:
            if callback == None:
                self.CAN_NETWORK.unsubscribe(COBID)
                self._CAN_SUBSCRIPTION.remove(COBID)
            else:
                self.CAN_NETWORK.unsubscribe(COBID, callback)
                self._CAN_SUBSCRIPTION.remove(COBID)
        except Exception as e:
            self.logger.error(f"Error unsubscribing from {COBID}, error: {e}")
    async def SDOwrite(self, node_id: int, pdo_index: list, data: list):
        """
        Write data to a specified SDO for the given node.
        :param node_id: The ID of the node to write to.
        :param pdo_index: A list of the index and subindex of the SDO as in [index bit 0, index bit 1, subindex bit].
        :param data: The data to be sent (as a list of hexadecimals or ints).
        :return: Bool: True if the write operation was successful, False otherwise.
        """

        if len(data) > 4:
            index_data = bytearray([pdo_index[0], pdo_index[2], pdo_index[1]])
            data.reverse()
            data_chunks = [data[i:i + 4] for i in range(0, len(data), 4)]

            feedback = None
            received_data = None
            feedback_event = asyncio.Event()

            def temp_callback(_cobid, rec_data, rec_perc):
                nonlocal feedback, received_data
                feedback = int.from_bytes(rec_data[0:1], 'little')
                received_data = int.from_bytes(rec_data[5:], 'little')
                feedback_event.set()

            # Subscribe to node responses
            self.Subscribe(0x580 + node_id, temp_callback)

            try:
                # Initial SDO write request with control byte 0x20
                self.CAN_NETWORK.send_message(
                    0x600 + node_id,
                    bytearray([0x20]) + index_data + bytearray([0x00] * 4)
                )
                await feedback_event.wait()
                feedback_event.clear()

                if feedback == 0x80:
                    self.logger.error(
                        f"Error writing to {pdo_index}: {self._SDO_ABORT_CODES.get(received_data)}"
                    )
                    return False

                # Segment transfer loop
                for i, chunk in enumerate(data_chunks):
                    control_byte = 0x10 if feedback == 0x20 else 0x00
                    payload = bytearray([control_byte]) + bytearray(chunk) + bytearray([0] * (4 - len(chunk)))
                    self.CAN_NETWORK.send_message(0x600 + node_id, payload)

                    await feedback_event.wait()
                    feedback_event.clear()

                    # Final segment handling for the last chunk
                    if i == len(data_chunks) - 1:
                        final_control_byte = 0x11 if feedback == 0x20 else 0x01
                        final_payload = bytearray([final_control_byte]) + bytearray(chunk) + bytearray(
                            [0] * (4 - len(chunk)))
                        self.CAN_NETWORK.send_message(0x600 + node_id, final_payload)
                        await feedback_event.wait()

                return True

            except Exception as e:
                self.logger.error(f"Error writing to SDO {0x600 + node_id}, error: {e}")
                return False

            finally:
                # Ensure we unsubscribe from responses after all operations are done
                self.Unsubscribe(0x580 + node_id)

        elif len(data) <= 4:
            data += [0] * (4 - len(data))
            data.reverse()  # Ensure little endian format
            written_data = bytearray(data)

            try:
                index_data = bytearray([pdo_index[1], pdo_index[0], pdo_index[2]])
                self.CAN_NETWORK.send_message(0x600 + node_id, index_data + written_data)
                return True
            except canopen.SdoCommunicationError as e:
                self.logger.error(f"PDO Write Error: {e}")
                return False

        else:
            self.logger.error(
                f"Error in writing to {pdo_index}: Unsupported data length."
            )
            return False
    async def SDOread(self, node_id: int, pdo_index: list):
        """
        Retrieve the current data from the specified SDO for the given node.
        :param node_id: The ID of the node to read from.
        :param pdo_index: A list of the index and subindex of the sdo as in [index bit 0, index bit 1, subindex bit], e.g. [0x60, 0x60, 0x00] for index 0x6060 subindex 0x00
        return: Returns data with callback with node id 0x580 + nodeid or None if an error occurs.

        TODO: Enable support for multiple data lengths
        """
        feedback = None
        received_data = bytearray()
        feedback_event = asyncio.Event()
        control_bit = 0x60  # Start with control bit 0x60 for multi-part transfer

        def temp_callback(_cobid, rec_data, rec_perc):
            nonlocal feedback, received_data
            feedback = int.from_bytes(rec_data[0:1], 'little')
            received_data.extend(rec_data[5:])  # Collect data from response payload
            feedback_event.set()

        try:
            # Setup the initial read request in little-endian format
            data = [0x40, pdo_index[1], pdo_index[0], pdo_index[2]]
            # Subscribe to response and send the initial read request
            self.Subscribe(0x580 + node_id, temp_callback)
            self.CAN_NETWORK.send_message(0x600 + node_id, bytearray(data))

            # Continuously wait and read until the last message is received
            while True:
                await feedback_event.wait()
                feedback_event.clear()

                # Check for SDO error
                if feedback == 0x80:
                    self.logger.error(f"SDO error: node {node_id}, error: {self._SDO_ABORT_CODES.get(received_data[-8:])}")
                    return None

                # If feedback indicates last packet received, break loop
                if control_bit == 0x60 and feedback == 0x41:
                    break
                elif control_bit == 0x70 and feedback == 0x43:
                    break

                # Toggle control bit and send acknowledgment to request next part
                control_bit = 0x70 if control_bit == 0x60 else 0x60
                self.CAN_NETWORK.send_message(0x600 + node_id, bytearray([control_bit]))

            # Return the assembled data as an integer
            rcv_data = int.from_bytes(received_data, 'little')
            return rcv_data

        except Exception as e:
            self.logger.error(f"Error reading from node {node_id}: {e}")
            return None
    def PDOwrite(self, COB_ID: int, data=None):
        """
        Write data to a mapped RPDO object (Controlword)
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
                self.logger.error(f"PDO Write Error: {e}")
                return False
        else:
            self.logger.error(f"Message length over 8 bits is not supported")
            return False
    def PDOread(self, node_id: int, index: int, subindex: int = 0, timeout: int = 1, timeout_count: int = 5):
        """
        Read data from an SDO on the specified CANopen node.
        :param node_id: The ID of the node to read from.
        :param index: The index in the object dictionary to read from.
        :param subindex: The subindex in the object dictionary.
        :param timeout: Timeout in seconds for the operation.
        :return: Data read from the node, or raises an exception on failure.

        TODO: NOT SUPPORTED (Can be accessed through either SDOread or Subscribe)
        """
        timeout_counter = 0
        try:
            node = self.CAN_NODES[node_id - 1]
            # Read the data from the specified index and subindex using SDO
            data = node.sdo[index][subindex].read(timeout=timeout)
            return data
        except canopen.SdoCommunicationError as e:
            self.logger.error(f"SDO Read Error: {e}")
            raise
        except TimeoutError:
            self.logger.error(f"SDO read timed out after {timeout} seconds")
            while timeout_counter < timeout_count:
                try:
                    node = self.CAN_NODES[node_id - 1]
                    data = node.sdo[index][subindex].read(timeout=timeout)
                    timeout_counter += 1
                    return data
                except TimeoutError:
                    self.logger.error(f"SDO read timed out after {timeout} seconds")
            raise
    def NMTwrite(self, node_id: int, ctrlWord: int):
        data = [ctrlWord, node_id]
        self.CAN_NETWORK.send_message(0x00, bytearray(data))
