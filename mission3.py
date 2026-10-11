from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.tools import wait
import umath as umath
import math


# Speed levels (mm/s)
FAST_SPEED = 600
MEDIUM_SPEED = 450
SLOW_SPEED = 300

Distanza = 500 #50 mm = 5 cm


def mission3(myRobot):

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
    #drive.straight(720, then=Stop.BRAKE, wait=True)
    #drive.turn(-20, then=Stop.BRAKE, wait=True)

    #muovi porta robot avanti e abbassa il braccio
    myRobot.accessoryRight.run_angle(SLOW_SPEED, accessory_right_sign * 163, then=Stop.HOLD, wait=False)
    drive.straight(462, then=Stop.BRAKE, wait=True)
    
    drive.turn(16, then=Stop.BRAKE, wait=True)
    myRobot.accessoryRight.run_angle(SLOW_SPEED, accessory_right_sign * (-26), then=Stop.HOLD, wait=True)
    drive.settings(straight_speed=100, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(-160, then=Stop.BRAKE, wait=True)
    
    myRobot.accessoryRight.run_angle(SLOW_SPEED, accessory_right_sign * (20), then=Stop.HOLD, wait=True)
    drive.turn(-26, then=Stop.BRAKE, wait=True)
    drive.settings(straight_speed=400, straight_acceleration=FAST_SPEED,turn_rate=100, turn_acceleration=100)
    drive.straight(-400, then=Stop.BRAKE, wait=True)
    
    myRobot.accessoryLeft.run_angle(SLOW_SPEED, accessory_right_sign * (-150), then=Stop.HOLD, wait=True)
    
    myRobot.accessoryRight.run_angle(SLOW_SPEED, accessory_right_sign * (-80), then=Stop.HOLD, wait=True)
    wait(260)
    drive.straight(780, then=Stop.BRAKE, wait=True)
    drive.turn(-20, then=Stop.BRAKE, wait=True)
    drive.straight(-100, then=Stop.BRAKE, wait=True)
    drive.turn(30, then=Stop.BRAKE, wait=True)

    drive.straight(-80, then=Stop.BRAKE, wait=True)
    myRobot.accessoryLeft.run_angle(SLOW_SPEED, accessory_right_sign * (80), then=Stop.HOLD, wait=True)
    drive.straight(-40, then=Stop.BRAKE, wait=True)
    drive.turn(90, then=Stop.BRAKE, wait=True)
    myRobot.accessoryLeft.run_angle(SLOW_SPEED, accessory_right_sign * (80), then=Stop.HOLD, wait=True)
    drive.straight(85.795320, then=Stop.BRAKE, wait=True)

    #be the cool robot who makes the cool mission
    myRobot.accessoryLeft.run_angle(SLOW_SPEED, accessory_right_sign * (-80), then=Stop.HOLD, wait=True)
    print("Kinderarbeit Auf Die Eins!")



    #the robot is now in front of the ramp, ready to climb it. The next steps would involve adjusting the accessories and driving up the ramp, but those details are not included in this snippet.

    #GET OUT drive.straight(-900, then=Stop.BRAKE, wait=True)
    #drive.straight(100, then=Stop.BRAKE, wait=True)
    #drive.turn(20, then=Stop.BRAKE, wait=True)
    #drive.straight(-100 , then=Stop.BRAKE, wait=True)
    #drive.turn(-10, then=Stop.BRAKE, wait=True)
    #drive.straight(-900, then=Stop.BRAKE, wait=True)

