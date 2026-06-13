from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 600
MEDIUM_SPEED = 450
SLOW_SPEED = 100

Distanza = 500 #50 mm = 5 cm


def mission1(myRobot):

    print("Go!")

    # accessory direction signs (start with negative as requested)
    accessory_left_sign = -1
    accessory_right_sign = 1

    # Initialize DriveBase (pass gyro if available)
    drive = myRobot.driveBase

    # --- 1) Fast drive straight 620 mm while moving both accessories to mechanical stop ---
    drive.reset()  # zero distance measurement
    drive.use_gyro(True)
    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)


    # Blocking straight move
    drive.straight(720, then=Stop.BRAKE, wait=True)
    drive.turn(-20, then=Stop.BRAKE, wait=True)

    # Picchia col martello e prendi le rotelline nascoste
    myRobot.accessoryRight.run_angle(FAST_SPEED, accessory_right_sign * 360*5, then=Stop.HOLD, wait=True)

    # drive.ar e risolvi altre 2 missioni
    drive.arc(-185.3, 71.67, then=Stop.HOLD, wait=True)
    drive.straight(10, then=Stop.BRAKE, wait=True)
    drive.arc(-60, 45.2, then=Stop.BRAKE, wait=True)