#!/usr/bin/env python3
import sys, pygame

class GamepadButtons:

    # Set fields for different types for easier readability
    LINUX = 0
    MAC = 1
    WINDOWS = 2

    # Determine the operating system
    platform_id = None
    # Determine the python version
    version = int(pygame.version.ver[0])

    # Check OS type
    if sys.platform.startswith("lin"):
        platform_id = LINUX
    elif sys.platform.startswith("darwin"):
        platform_id = MAC
    elif sys.platform.startswith("win"):
        platform_id = WINDOWS

    if platform_id == LINUX:
        # buttons
        A = 0
        B = 1
        X = 2
        Y = 3
        LEFT_BUMP = 4
        RIGHT_BUMP = 5
        BACK = 6
        START = 7
        # GUIDE = 8
        LEFT_STICK_BTN = 9
        RIGHT_STICK_BTN = 10

        # axes
        LEFT_STICK_X = 0
        LEFT_STICK_Y = 1
        RIGHT_STICK_X = 3
        RIGHT_STICK_Y = 4
        LEFT_TRIGGER = 2
        RIGHT_TRIGGER = 5

    elif platform_id == WINDOWS:
        # buttons
        A = 0
        B = 1
        X = 2
        Y = 3
        LEFT_BUMP = 4
        RIGHT_BUMP = 5
        BACK = 6
        START = 7
        LEFT_STICK_BTN = 8
        RIGHT_STICK_BTN = 9

        # axes
        LEFT_STICK_X = 0
        LEFT_STICK_Y = 1
        if version == 2:
            RIGHT_STICK_X = 2
            RIGHT_STICK_Y = 3
            LEFT_TRIGGER = 4
            RIGHT_TRIGGER = 5
        else:
            RIGHT_STICK_X = 4
            RIGHT_STICK_Y = 3
            TRIGGERS = 2

    elif platform_id == MAC:
        # buttons
        A = 11
        B = 12
        X = 13
        Y = 14
        LEFT_BUMP = 8
        RIGHT_BUMP = 9
        BACK = 5
        START = 4
        LEFT_STICK_BTN = 6
        RIGHT_STICK_BTN = 7

        # d-pad
        PAD_UP = 0
        PAD_DOWN = 1
        PAD_LEFT = 2
        PAD_RIGHT = 3

        # axes
        LEFT_STICK_X = 0
        LEFT_STICK_Y = 1
        RIGHT_STICK_X = 2
        RIGHT_STICK_Y = 3
        LEFT_TRIGGER = 4
        RIGHT_TRIGGER = 5