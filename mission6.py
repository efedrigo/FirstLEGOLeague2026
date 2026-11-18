from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath


# Speed levels (mm/s)
FAST_SPEED = 600
MEDIUM_SPEED = 450
SLOW_SPEED = 100

Distanza = 500 #50 mm = 5 cm


def mission6(myRobot):

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

    #Prendi il pezzetto alla pianta
    drive.arc(-200,60, then=Stop.BRAKE, wait=True)
    drive.straight(650, then=Stop.BRAKE, wait=False)
    wait(400)
    myRobot.accessoryRight.run_angle(SLOW_SPEED, accessory_left_sign * (-40), then=Stop.HOLD, wait=True)
    wait(50)
    drive.turn(-15, then=Stop.BRAKE, wait=True)
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=MEDIUM_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(180, then=Stop.BRAKE, wait=True)

    #vaiindietro
    drive.settings(straight_speed=SLOW_SPEED, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(-100, then=Stop.BRAKE, wait=True)
    drive.arc(170,25, then=Stop.BRAKE, wait=True)
    myRobot.accessoryLeft.run_angle(FAST_SPEED, accessory_left_sign * (160), then=Stop.HOLD, wait=True)\

    #FASTSPPEEEEED! SBERIGATT(IIIIIII!!!!)d,feiriwv e]
    drive.settings(straight_speed=FAST_SPEED, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(-500, then=Stop.BRAKE, wait=True)
    drive.arc(200,-30, then=Stop.BRAKE, wait=True)
    print("lesgoskilmaoshifalolsicsevenahahstazionecentralemilanochesmettanoepoicomunqueilduomo@______")
    wait(200)