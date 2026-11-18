from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 600
MEDIUM_SPEED = 450
SLOW_SPEED = 100

Distanza = 500 #50 mm = 5 cm


def missionA(myRobot):

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
   
    drive.straight(733, then=Stop.BRAKE, wait=True)
    drive.turn(-40, then=Stop.BRAKE, wait=True)
    drive.straight(110, then=Stop.BRAKE, wait=True)
    myRobot.accessoryLeft.run_angle(FAST_SPEED, accessory_left_sign * -70, then=Stop.HOLD, wait=True)
    

