#!/usr/bin/env python3
"""
Created for Lunar surface preparation project
9. Semester, Robotics, 2024 Fall Semester
Group 962
"""

import types

class CTW:
    # CANBus Enable operation ControlWord
    ENABLE_OP = 0x0F

    # CANBus Disable operation (Disable current) ControlWord
    DISABLE_OP = 0x0

    # CANBus Reset ControlWord
    RESET = 0x81

    # CANBus Shutdown ControlWord
    SHUTDOWN = 0x06

    # CANBus Turn on ControlWord
    TURNON = 0x07

    # CANBus Quickstop ControlWord
    QUICKSTOP = 0x02

    # CANBus reset communication ControlWord
    RESET_COMM = 0x82

    # CANBus Enable ControlWord
    ENABLE = 0x01
