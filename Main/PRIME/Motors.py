# Making the motor move back and forth
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor on port A.
example_motor = Motor(Port.A)

# Make the motor run clockwise at 500 degrees per second.
example_motor.run(500)

# Wait for three seconds.
wait(3000)

# Make the motor run counterclockwise at 500 degrees per second.
example_motor.run(-500)

# Wait for three seconds.
wait(3000)

# Initialising Multiple Motors
# Initialize motors on port A and B.
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# Make both motors run at 500 degrees per second.
track_motor.run(500)
gripper_motor.run(500)

# Wait for three seconds.
wait(3000)