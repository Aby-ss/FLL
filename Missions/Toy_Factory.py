from spike import Motor
from spike import MotorPair

movement_pair = MotorPair('F', 'B')
movement_pair.set_default_speed(25)
movement_pair.move(1.6, 'rotations')

D_motor = Motor('D')
D_motor.set_default_speed(20)
D_motor.run_for_seconds(0.6, -75)
D_motor.move(-2, 'rotations')