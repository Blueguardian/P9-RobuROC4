import gamepad
import visualizer
import controller

ctrl = gamepad.Controller()
viz = visualizer.Visualizer()
motors = controller()

max_speed = maxSpeed = 2.0 # m/s

while(not ctrl.button_active('X')):

    #direction = ctrl.get_right_stick()
    direction = ctrl.get_left_stick()

    left = round(direction[1] + direction[0] / 4, 4)
    right = round(direction[1] - direction[0] / 4, 4)

    left = left * max_speed
    right = right * max_speed

    if motors._READY:
        motors.setMPS(0, left)
        motors.setMPS(1, -right)
        motors.setMPS(2, -right)
        motors.setMPS(3, left)
