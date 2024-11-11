"""
Adapted for Lunar surface preparation project
9. Semester, Robotics, 2024 Fall Semester
Group 962

Copyright (c) 2017 Jon Cooper

This file is part of pygame-xbox360controller.
Documentation, related files, and licensing can be found at
  <https://github.com/joncoop/pygame-xbox360controller>.
"""

import pygame, gamepad_buttons

class Controller:
    id_num = 0

    def __init__(self, dead_zone=0.05):
        """
        Initializes a controller. IDs for controllers begin at 0 and increment by 1
        each time a controller is initialized.

        Args:
            dead_zone: The size of dead zone for the analog sticks (default 0.15)
        """
        self.BUTTONS = gamepad_buttons.GamepadButtons
        self.joystick = pygame.joystick.Joystick(Controller.id_num)
        self.joystick.init()
        self.dead_zone = dead_zone

        # Linux and Mac triggers behave funny. See get_triggers().
        self.left_trigger_used = False
        self.right_trigger_used = False

        Controller.id_num += 1

    def get_id(self):
        """
        Returns:
            The ID of the controller.
        """

        return self.joystick.get_id()

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
        return (self.joystick.get_button(self.BUTTONS.A),
                self.joystick.get_button(self.BUTTONS.B),
                self.joystick.get_button(self.BUTTONS.X),
                self.joystick.get_button(self.BUTTONS.Y),
                self.joystick.get_button(self.BUTTONS.LEFT_BUMP),
                self.joystick.get_button(self.BUTTONS.RIGHT_BUMP),
                self.joystick.get_button(self.BUTTONS.BACK),
                self.joystick.get_button(self.BUTTONS.START),
                0,  # Unused, since Guide only works on Linux
                self.joystick.get_button(self.BUTTONS.LEFT_STICK_BTN),
                self.joystick.get_button(self.BUTTONS.RIGHT_STICK_BTN))

    def get_left_stick(self):
        """
        Gets the state of the left analog stick.

        Returns:
            The x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

            Negative values are left and up.
            Positive values are right and down.
        """

        left_stick_x = self.dead_zone_adjustment(self.joystick.get_axis(self.BUTTONS.LEFT_STICK_X))
        left_stick_y = self.dead_zone_adjustment(self.joystick.get_axis(self.BUTTONS.LEFT_STICK_Y))

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

        right_stick_x = self.dead_zone_adjustment(self.joystick.get_axis(self.BUTTONS.RIGHT_STICK_X))
        right_stick_y = self.dead_zone_adjustment(self.joystick.get_axis(self.BUTTONS.RIGHT_STICK_Y))

        return right_stick_x, right_stick_y

    def get_triggers(self):
        """
        Gets the state of the triggers.

        On Windows with pygame version 1.9, both triggers work additively to act as
        a single axis. In all other cases, each trigger functions as an independent
        axes. In this interface, triggers will behave additively for all platforms
        so that pygame controllers will work consistently on each platform and
        pygame version.

        On Linux and Mac, trigger axes return 0 if they haven't been used yet. Once
        used, an unpulled trigger returns 1 and pulled returns -1. The trigger_used
        booleans keep the math correct for triggers prior to use.

        Returns:
            A float in the range -1.0 <= value <= 1.0 where -1.0 represents full
            left and 1.0 represents full right. If the triggers are pulled
            simultaneously, then the sum of the trigger pulls is returned.
        """

        trigger_axis = 0.0

        if self.BUTTONS.platform_id == self.BUTTONS.LINUX or self.BUTTONS.platform_id == self.BUTTONS.MAC:
            left = self.joystick.get_axis(self.BUTTONS.LEFT_TRIGGER)
            right = self.joystick.get_axis(self.BUTTONS.RIGHT_TRIGGER)

            if left != 0:
                self.left_trigger_used = True
            if right != 0:
                self.right_trigger_used = True

            if not self.left_trigger_used:
                left = -1
            if not self.right_trigger_used:
                right = -1

            trigger_axis = (-1 * left + right) / 2

        elif self.BUTTONS.platform_id == self.BUTTONS.WINDOWS:
            if self.BUTTONS.version == 2:
                left = self.joystick.get_axis(self.BUTTONS.LEFT_TRIGGER)
                right = self.joystick.get_axis(self.BUTTONS.RIGHT_TRIGGER)
                trigger_axis = (-1 * left + right) / 2
            else:
                trigger_axis = -1 * self.joystick.get_axis(self.BUTTONS.TRIGGERS)

        return trigger_axis

    def get_pad(self):
        """
        Gets the state of the directional pad.

        Returns:
            A tuple in the form (up, right, down, left) where each value will be
            1 if pressed, 0 otherwise. Pads are 8-directional, so it is possible
            to have up to two 1s in the returned tuple.
        """

        if self.BUTTONS.platform_id == self.BUTTONS.LINUX or self.BUTTONS.platform_id == self.BUTTONS.WINDOWS:
            hat_x, hat_y = self.joystick.get_hat(0)

            up = int(hat_y == 1)
            right = int(hat_x == 1)
            down = int(hat_y == -1)
            left = int(hat_x == -1)
            return up, right, down, left

        elif self.BUTTONS.platform_id == self.BUTTONS.MAC:
            up = self.joystick.get_button(self.BUTTONS.PAD_UP)
            right = self.joystick.get_button(self.BUTTONS.PAD_RIGHT)
            down = self.joystick.get_button(self.BUTTONS.PAD_DOWN)
            left = self.joystick.get_button(self.BUTTONS.PAD_LEFT)
            return up, right, down, left

    def SwitchOff(self):
        self.joystick.quit()

    def PadBattery(self):
        return self.joystick.get_power_level()
