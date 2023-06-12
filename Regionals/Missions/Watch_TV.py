from spike import Motor
from spike import MotorPair

movement_pair = MotorPair('F', 'B')

movement_pair.move(2, 'rotations')
movement_pair.move(-2, 'rotations')