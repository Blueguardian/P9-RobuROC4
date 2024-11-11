"""
Created for Lunar surface preparation project
9. Semester, Robotics, 2024 Fall Semester
Group 962
"""

import types

class COBID:
    """
    CANBus COBID IDs for Advaneced motion controls DPCANTR-040B080 driver
    These are based on the communication documentation for the driver.

    For reference see:
    Driver datasheet:: https://www.a-m-c.com/document-login/?h=d009347&src=https%3A%2F%2Fwww.a-m-c.com%2Fproduct%2Fdpcantr-040b080%2F
    Communication documentation for the driver can be found here: https://www.a-m-c.com/document-login/?h=ff4cde0&src=https%3A%2F%2Fwww.a-m-c.com%2Fproduct%2Fdpcantr-040b080%2F
    """

    # CANBus Host ID
    HOST = 0x05
    BROADCAST = 0x00

    # CANBus Control IDs
    CONTROL = types.SimpleNamespace()
    CONTROL.ALL = [0x201, 0x202, 0x203, 0x204]

    CONTROL.Motor1 = 0x201
    CONTROL.Motor2 = 0x202
    CONTROL.Motor3 = 0x203
    CONTROL.Motor4 = 0x204

    # CANBus Mode IDs
    MODE = types.SimpleNamespace()
    MODE.ALL = [0x501, 0x502, 0x503, 0x504]

    MODE.Motor1 = 0x501
    MODE.Motor2 = 0x502
    MODE.Motor3 = 0x503
    MODE.Motor4 = 0x504

    # CANBus Actual Velocity IDs
    ACT_VELOCITY = types.SimpleNamespace()
    ACT_VELOCITY.ALL = [0x371, 0x372, 0x373, 0x374]

    ACT_VELOCITY.Motor1 = 0x371
    ACT_VELOCITY.Motor2 = 0x372
    ACT_VELOCITY.Motor3 = 0x373
    ACT_VELOCITY.Motor4 = 0x374

    # CANBus Actual Current IDs
    ACT_CURRENT = types.SimpleNamespace()
    ACT_CURRENT.ALL = [0x381, 0x382, 0x383, 0x384]

    ACT_CURRENT.Motor1 = 0x381
    ACT_CURRENT.Motor2 = 0x382
    ACT_CURRENT.Motor3 = 0x383
    ACT_CURRENT.Motor4 = 0x384

    # CANBus Target Velocity IDs
    TARGET_VELOCITY = types.SimpleNamespace()
    TARGET_VELOCITY.ALL = [0x511, 0x512, 0x513, 0x514]

    TARGET_VELOCITY.Motor1 = 0x511
    TARGET_VELOCITY.Motor2 = 0x512
    TARGET_VELOCITY.Motor3 = 0x513
    TARGET_VELOCITY.Motor4 = 0x514

    # CANBus Target Current IDs
    TARGET_CURRENT = types.SimpleNamespace()
    TARGET_CURRENT.ALL = [0x521, 0x522, 0x523, 0x524]

    TARGET_CURRENT.Motor1 = 0x521
    TARGET_CURRENT.Motor2 = 0x522
    TARGET_CURRENT.Motor3 = 0x523
    TARGET_CURRENT.Motor4 = 0x524

    # CANBus Service data object IDs
    SDO_WRITE = types.SimpleNamespace()
    SDO_WRITE.ALL = [0x601, 0x602, 0x603, 0x604]

    SDO_WRITE.Motor1 = 0x601
    SDO_WRITE.Motor2 = 0x602
    SDO_WRITE.Motor3 = 0x603
    SDO_WRITE.Motor4 = 0x604

    # CANBus Service data object receive IDs
    SDO_READ = types.SimpleNamespace()
    SDO_READ.ALL = [0x581, 0x582, 0x583, 0x584]

    SDO_READ.Motor1 = 0x581
    SDO_READ.Motor2 = 0x582
    SDO_READ.Motor3 = 0x583
    SDO_READ.Motor4 = 0x584

    # CANBus Heartbeat
    HEARTBEAT = types.SimpleNamespace()
    HEARTBEAT.ALL = [0x701, 0x702, 0x703, 0x704]

    HEARTBEAT.Motor1 = 0x701
    HEARTBEAT.Motor2 = 0x702
    HEARTBEAT.Motor3 = 0x703
    HEARTBEAT.Motor4 = 0x704

