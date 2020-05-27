#!/home/genia/Enthought/Canopy_64bit/User/bin/python
import os
import socket
"""if __name__ == '__main__':
    import sys
    sys.path.append(os.environ['SEQALL_PATH'])
    sys.path.append('/home/genia/projects/labcodes_branch')
    sys.path.append('/home/genia/projects/labcodes_branch/fluidics')
from gantryTecan import gantryTecan as gantryTecan

class CentrisPump(gantryTecan):
    tecanCommObj = sendTotecan()
    Syringesize = 1000
    maxPullvol = 1000
    maxPullspeed = 300
    maxTubePull = 2000

    def __init__(self, valve_num=1):
        gantryTecan.__init__(self)

    def closePinchValve(self):
        self.centrisClosePinchValve()

    def openPinchValve(self):
        self.centrisOpenPinchValve()

    def valve(self, spot):
        self.centrisValvePos(spot)

    def centrisInit(self):
        print('initing')
        self.tecanCommObj.sendCmd('1/9Z7,1,1R')
        self.tecanCommObj.sendCmd('1/9U11R')

    def centrisSetSpeed(self, speed=maxPullspeed):
        self.tecanCommObj.sendCmd('1/9V{},1'.format(str(speed)))

    def centrisValvePos(self, spot):
        if spot == 'a' or spot == 'inlet_pos':
            spot = 1
        elif spot == 'b' or spot == 'outlet_pos':
            spot = 2
        elif spot == 'c' or spot == 'waste_pos':
            spot = 3
        elif spot == 'd' or spot == 'outlet_pos_dis':
            spot = 4
        elif spot == 'e':
            spot = 5
        elif spot == 'f':
            spot = 6
        print('Switching to valve: %s' % spot)
        self.tecanCommObj.sendCmd('1/9I{}R'.format(str(spot)))

    def centrisPull(self, volume, speed=maxPullspeed, delay=0.5):
        if volume > 1000:
            volume = 1000
        vol_start = self.get_syringePos()
        print('\nStarting Syringe position: %.1f ul' % vol_start)
        print('Pulling {}ul at {}ul/sec'.format(str(volume), str(speed)))
        self.centrisSetSpeed(speed)
        self.tecanCommObj.sendCmd('1/9P{},1R'.format(str(volume)))
        vol_end = self.get_syringePos()
        print('Final Syringe position: %.1f ul' % vol_end)
        vol_delta = vol_end - vol_start
        valve = self.get_valvePos()
        print('Aspirated %.1f ul from valve %s.' % (vol_delta, valve.upper()))
       
    def centrisPush(self, volume, speed=maxPullspeed, delay=0.5):
        vol_start = self.get_syringePos()
        print('\nStarting Syringe position: %.1f ul' % vol_start)
        print('Pushing {}ul at {}ul/sec'.format(str(volume), str(speed)))
        self.centrisSetSpeed(speed)
        self.tecanCommObj.sendCmd('1/9D{},1R'.format(str(volume)))
        vol_end = self.get_syringePos()
        print('Final Syringe position: %.1f ul' % vol_end)
        vol_delta = vol_end - vol_start
        valve = self.get_valvePos()
        print('Dispensed %.1f ul into valve %s.' % (-vol_delta, valve.upper()))

    def centrisOpenPinchValve(self):
        print('Opening Anti-Siphon valve')
        self.tecanCommObj.sendCmd('1/0L1,1R')

    def centrisClosePinchValve(self):
        print('Closing Anti-Siphon valve')
        self.tecanCommObj.sendCmd('1/0L1,0R')"""

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