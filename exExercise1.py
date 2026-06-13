import umath

from exRobot import robot

myRobot = robot();

D=100;
wheelD = 44.3;
wheelC = wheelD * umath.pi;

x      = 0;
y      = 0;
x_prev = 0;
y_prev = 0;
loopX  = 0;
loopY  = 0;

while (myRobot.getTime()<24):
    t = myRobot.getTime();
    x = myRobot.getEncoderL() * wheelC / 360;
    y = myRobot.getEncoderR() * wheelC / 360;

    if (x_prev<0):
        loopX = loopX + 1;
    x_prev = x;

    if (y_prev<0):
        loopY = loopY + 1;
    y_prev = y;

print(x+wheelC*loopX,y+wheelC*loopY);


