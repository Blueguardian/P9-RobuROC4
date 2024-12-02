import canopen
from time import sleep
from gamepad import Controller
import os

def callback1(canid:int, data:bytearray, flags:float):
    #value = int.from_bytes(data, byteorder='little', signed=True)
    data = list(data)
    hex_data = [hex(x) for x in data]
    print(f"Node {canid} data: {hex_data}")
# Example usage
if __name__ == "__main__":

    #log = []  # Assuming a simple log list for errors
    #mc = MotorControl(log)

    #mc.setup()  # Initialize and configure the drives
    #mc.setSpeed(index=0, speed=1000)  # Example to set speed
    #mc.run()  # Start periodic updates

    # Assuming you want to disconnect the CAN network at some point
    WHEEL_RADIUS = 0.28
    SCALE_VELOCITY = ((pow(2, 17) / (2 * 20000) * pow(2, 19)) / 1000) * 32  # To RPM
    SCALE_RPM_TO_MPS = ((2.0 * 3.14) / 60.0) * WHEEL_RADIUS
    controller = Controller()

    network = canopen.Network()
    network.connect(bustype='pcan', channel='PCAN_USBBUS1', bitrate=1000000)
    path = os.path.join(os.path.abspath(os.curdir), "AMC.eds")
    nodes = []
    network.send_periodic(0x700, [0], 0.02)
    network.subscribe(0x584, callback=callback1)
    network.subscribe(0x604, callback1)

    network.nmt.send_command(0x81)
    # network.nmt.send_command(0x82)
    # network.nmt.send_command(0x80)
    network.nmt.send_command(0x01)
    while len(network.scanner.nodes) < 4:
        network.scanner.search()
        sleep(1)
    print(network.scanner.nodes)
    for node in network.scanner.nodes:
        # nodeR = canopen.RemoteNode(i, path, False)
        node = network.add_node(node)
        nodes.append(node)
    #     print("Sending reset command")
    #     node.nmt.send_command(0x81) # reset
    #     sleep(1)
    #     print("Sending reset communication command")
    #     node.nmt.send_command(0x82) # reset communication
    #     sleep(1)
    #     print("Sending reset after error command")
    #     node.nmt.send_command(0x80)  # Reset after error
    #     sleep(1)
    #     print("Sending enable command")
    #     node.nmt.send_command(0x01) # enable
    print(nodes)
    sleep(2)
    # network.nmt.send_command(0x07)
    # network.nmt.send_command(0x0F)
    # network.nmt.send_command(0x01)
    # for node in nodes:
        # node.nmt.send_command(0x07) # turn on
        # node.nmt.send_command(0x0F) # enable operation
        # node.nmt.send_command(0x01) # enable

    for node in nodes:
        node.sdo.download(0x6040, 0x00, bytearray([0x0F, 0x00, 0x00, 0x00]))
        node.rpdo.read()
        node.tpdo.read()
    # network.send_message(0, bytearray([0x01, 0x01]))
    #network.send_message(0x601, bytearray([0x22, 0x40, 0x60, 0x00, 0x0F, 0x00, 0x00, 0x00]))
    # network.send_message(0, bytearray([0x01, 0x02]))
    #network.send_message(0x602, bytearray([0x22, 0x40, 0x60, 0x00, 0x0F, 0x00, 0x00, 0x00]))
    # network.send_message(0, bytearray([0x01, 0x03]))
    #network.send_message(0x603, bytearray([0x22, 0x40, 0x60, 0x00, 0x0F, 0x00, 0x00, 0x00]))
    #network.send_message(0, bytearray([0x01, 0x04]))
    #network.send_message(0x604, bytearray([0x22, 0x40, 0x60, 0x00, 0x0F, 0x00, 0x00, 0x00]))

    for node in nodes:
        data1 = list((12000000).to_bytes(4, byteorder='little', signed=True))
        data = [0x22, 0x62, 0x20]
        for x in data1:
            data.append(x)
        print(data)
        network.send_message(0x600 + node.id, bytearray(data))

    sleep(1)

    for node in nodes:
        print(node.nmt.state) # what state are we in?

    for node in nodes:
        print(f"{node.id}")
        print(f"Sending change mode command to node {node.id}")
        node.sdo.download(0x6060, 0x00, bytearray([0x03, 0x00, 0x00, 0x00]))

    print("Sending speed command to motor 4")
    for value in nodes[0].pdo.values().__iter__():
        print(value)
    while True:
        print(f"Quick stop brake speed: {int.from_bytes(nodes[0].sdo.upload(0x2062, 0x00), 'little')}")
        print(f"Actual speed, node {network.scanner.nodes[0]}: {int.from_bytes(nodes[0].sdo.upload(0x606C, 0x00), 'little') * (SCALE_RPM_TO_MPS / SCALE_VELOCITY)}")
        # if controller.get_buttons()[2] == 1:
        #     joystick = controller.get_left_stick()
        #
        #     left = round(joystick[1] + joystick[0] / 4, 4) * 2
        #     right = round(joystick[1] - joystick[0] / 4, 4) * 2
        #
        #     vel_MPS = int(left * (SCALE_VELOCITY / SCALE_RPM_TO_MPS))
        #     vel2_MPS = int(-right * (SCALE_VELOCITY / SCALE_RPM_TO_MPS))
        #
        #     vel_MPS = bytearray(vel_MPS.to_bytes(4, byteorder='little', signed=True))
        #     vel2_MPS = bytearray(vel2_MPS.to_bytes(4, byteorder='little', signed=True))
        #
        #     network.send_message(0x514, vel_MPS)
        #     network.send_message(0x513, vel2_MPS)
        #     network.send_message(0x512, vel2_MPS)
        #     network.send_message(0x511, vel_MPS)
        #     sleep(0.1)
        if True:
            for node in nodes:
                # network.send_message(0x514, bytearray([0x00, 0xFF, 0x00, 0x00]))
                # network.send_message(0x513, bytearray([0x00, 0xFF, 0x00, 0x00]))
                # network.send_message(0x512, bytearray([0x00, 0xFF, 0x00, 0x00]))
                # network.send_message(0x511, bytearray([0x00, 0xFF, 0x00, 0x00]))
                node.sdo.download(0x60FF, 0x00, bytearray([0x00, 0xFF, 0x00, 0x00]))

        else:
            network.send_message(0x514, bytearray([0x00, 0x00, 0x00, 0x00]))
            network.send_message(0x513, bytearray([0x00, 0x00, 0x00, 0x00]))
            network.send_message(0x512, bytearray([0x00, 0x00, 0x00, 0x00]))
            network.send_message(0x511, bytearray([0x00, 0x00, 0x00, 0x00]))
            sleep(0.1)
