from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 600
MEDIUM_SPEED = 450
SLOW_SPEED = 100

Distanza = 500 #50 mm = 5 cm


def mission5(myRobot):

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

    drive.straight(760, then=Stop.BRAKE, wait=True)
    drive.turn(58, then=Stop.BRAKE, wait=True)
    drive.straight(180/2, then=Stop.BRAKE, wait=True)
    myRobot.accessoryLeft.run_angle(SLOW_SPEED/2, accessory_left_sign * (20), then=Stop.HOLD, wait=True)
    myRobot.accessoryLeft.run_angle(SLOW_SPEED, accessory_right_sign * (-20), then=Stop.HOLD, wait=False)
    drive.straight(-160, then=Stop.BRAKE, wait=True)
    drive.turn(36, then=Stop.BRAKE, wait=True)
    drive.straight(-40, then=Stop.BRAKE, wait=True)
    myRobot.accessoryRight.run_angle(SLOW_SPEED, accessory_left_sign * (-130), then=Stop.HOLD, wait=True)
    wait(200)
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(110, then=Stop.BRAKE, wait=True)
    myRobot.accessoryRight.run_angle(SLOW_SPEED, accessory_left_sign * (60), then=Stop.HOLD, wait=False)
    wait(400)
    drive.settings(straight_speed=MEDIUM_SPEED, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(-80, then=Stop.BRAKE, wait=True)
    drive.turn(70, then=Stop.BRAKE, wait=True)
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(600, then=Stop.BRAKE, wait=True)
    wait(4000)
    drive.straight(400, then=Stop.BRAKE, wait=True)



