from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from pybricks.parameters import Axis
import umath

from robot import robotCompetition2026 as robot
#from odometer import odometer

from testConfig import program1, program0
#from testOdometer import program2
#from testPursuit i mport testPursuit
from mission1 import mission1
from mission2 import mission2a
from mission3 import mission3
from mission3a import mission3a
from mission5 import mission5
from mission6 import mission6
from missionA import missionA
#from mission9 import mission9
#from mission7 import mission7
#from mission8_b import mission8
#from mission10 import mission10
#from mission12 import mission12
#from mission956 import mission956
#from mission14 import mission14

watch = StopWatch()
myRobot = robot()
#myOdometer = odometer(myRobot,watch);

color = myRobot.colorSensor.color()
print("sensed color:",color)

MissionTable = [[Color.NONE,"A",mission1], #program0], # config test, battery level
#                [Color.BEIGE,"B",program1], # test configuration with motion
#                [Color.DARKBROWN,"C",program2],  # test odometer
#                [Color.BEIGE,"D",testPursuit], # test trajectory tracking
                [Color.YELLOW,"1",mission1],
                [Color.LIGHTGREEN,"2",mission2a],
                [Color.LIGHTBLUE,"3-",mission3],
                [Color.DARKBROWN,"5",mission5],
#                [Color.BEIGE,"6",mission6],
                [Color.ROSE,"3",mission3a],
                [Color.LIGHTBROWN,"3",missionA],
#                [Color.DARKBLUE,"4",mission8],
                [Color.WHITE,"5",mission5],
#                [Color.BLACK,"6",mission3_4],
#                [Color.RED,"7",mission14], Uncomment to enable mission14 Until mission14 is ready Uncomment the line below to enable mission14 Until mission14 is ready
                [Color.RED,"5",mission5],
                ]  

for mission in MissionTable:
    if (color == mission[0]):
        print(mission)
#        myRobot.hub.display.char(str(mission[1]))
        myRobot.hub.display.char(mission[1])
        print("Running program ",mission[1])
#        mission[2](myRobot,myOdometer)
        mission[2](myRobot)

myRobot.accessoryLeft.stop()
myRobot.accessoryRight.stop()
myRobot.driveBase.stop()

wait(500)