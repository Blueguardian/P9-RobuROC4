#  Copyright (c) 2017 Jon Cooper
#
#  This file is part of pygame-xbox360controller.
#  Documentation, related files, and licensing can be found at
#
#      <https://github.com/joncoop/pygame-xbox360controller>.
#
# Slightly modified pygame-xbox360controller for Robotics 9. Semester Project
#

import pygame
import sys


class Controller:
    _ID_NUM = 0
    _SYSTEM_ID = None
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

    def __init__(self, dead_zone=0.05):
        """
        Initializes a controller. IDs for controllers begin at 0 and increment by 1
        each time a controller is initialized.
        Args:
            dead_zone: The size of dead zone for the analog sticks (default 0.15)
        """
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(Controller._ID_NUM)
        self.joystick.init()
        self.dead_zone = dead_zone


        Controller._ID_NUM += 1
        self.version = int(pygame.version.ver[0])

    @property
    def ID_NUM(self):
        return self._ID_NUM
    @ID_NUM.setter
    def ID_NUM(self, value:int=0):
        self._ID_NUM = value
    @property
    def BUTTONS(self, index:str):
        return self._BUTTONS[index]
    @property
    def AXES(self, index:str):
        return self._AXES[index]
    @property
    def button_active(self, button:str):
        self.joystick.get_button(self._BUTTONS[button])



    def dead_zone_adjustment(self, value):
        """
        Analog sticks likely wont ever return to exact center when released. Without
        a dead zone, it is likely that a small axis value will cause game objects
        to drift. This adjusment allows for a full range of input while still
        allowing a little bit of 'play' in the dead zone.

        Returns:
            Axis value outside of the dead zone remapped proportionally onto the
            -1.0 <= value <= 1.0 range.
        """

        if value > self.dead_zone:
            return (value - self.dead_zone) / (1 - self.dead_zone)
        elif value < -self.dead_zone:
            return (value + self.dead_zone) / (1 - self.dead_zone)
        else:
            return 0
    def get_buttons(self):
        """
        Gets the state of each button on the controller.

        Returns:
            A tuple with the state of each button. 1 is pressed, 0 is unpressed.
        """
        return (self.joystick.get_button(self.A),
                self.joystick.get_button(self.B),
                self.joystick.get_button(self.X),
                self.joystick.get_button(self.Y),
                self.joystick.get_button(self.LEFT_BUMP),
                self.joystick.get_button(self.RIGHT_BUMP),
                self.joystick.get_button(self.BACK),
                self.joystick.get_button(self.START),
                0,  # Unused, since Guide only works on Linux
                self.joystick.get_button(self.LEFT_STICK_BTN),
                self.joystick.get_button(self.RIGHT_STICK_BTN))
    def get_left_stick(self):
        """
        Gets the state of the left analog stick.

        Returns:
            The x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

            Negative values are left and up.
            Positive values are right and down.
        """

        left_stick_x = self.dead_zone_adjustment(self.joystick.get_axis(self.AXES('LEFT_STICK_X')))
        left_stick_y = self.dead_zone_adjustment(self.joystick.get_axis(self.AXES('LEFT_STICK_Y')))

        return (left_stick_x, left_stick_y)
    def get_right_stick(self):
        """
        Gets the state of the right analog stick.

        Returns:
            The x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

            Negative values are left and up.
            Positive values are right and down.
        """

        right_stick_x = self.dead_zone_adjustment(self.joystick.get_axis(self.AXES('RIGHT_STICK_X')))
        right_stick_y = self.dead_zone_adjustment(self.joystick.get_axis(self.AXES('RIGHT_STICK_Y')))

        return (right_stick_x, right_stick_y)
    def get_triggers(self):
        """
        Gets the state of the triggers.

        On Windows with pygame version 1.9, both triggers work additively to act as
        a single axis. In all other cases, each trigger functions as an independent
        axes. In this interface, triggers will behave additively for all platforms
        so that pygame controllers will work consistently on each platform and
        pygame version.

        Returns:
            A float in the range -1.0 <= value <= 1.0 where -1.0 represents full
            left and 1.0 represents full right. If the triggers are pulled
            simultaneously, then the sum of the trigger pulls is returned.
        """


        left = self.joystick.get_axis(self.AXES('LEFT_TRIGGER'))
        right = self.joystick.get_axis(self.AXES('RIGHT_TRIGGER'))
        trigger_axis = (-1 * left + right) / 2

        return trigger_axis
    def get_pad(self):
        """
        Gets the state of the directional pad.

        Returns:
            A tuple in the form (up, right, down, left) where each value will be
            1 if pressed, 0 otherwise. Pads are 8-directional, so it is possible
            to have up to two 1s in the returned tuple.
        """

        hat_x, hat_y = self.joystick.get_hat(0)

        up = int(hat_y == 1)
        right = int(hat_x == 1)
        down = int(hat_y == -1)
        left = int(hat_x == -1)


        return up, right, down, left