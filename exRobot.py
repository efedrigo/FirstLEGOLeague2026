t=0s
class robot:
    t=0;

    def __init__(self):
        t=0;

    def getTime():
        t=t+0.01;
        return t;

    def getEncoderL():
        return ((t*1000)%100)/(1000)*7.3
    
    def getEncoderL():
        return ((t*1000)%100)/(-1000)*7.3
    