import time

class CentrisPump(object):

    def __init__(self):
        print('cnetrisPump')

    def centrisInit(self):
        pass

    def openASV(self):
        pass

    def closeASV(self):
        pass

    def pull(self, volume, speed, inlet_valve):
        vol = str(volume)
        spd = str(speed)
        val = str(inlet_valve)
        print(vol, spd, val)
        return vol

    def push(self,volume, speed, inlet_valve):
        vol = str(volume)
        spd = str(speed)
        val = str(inlet_valve)
        print(vol, spd, val)
        return spd