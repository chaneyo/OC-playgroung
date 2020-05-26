import random
from serial import Serial
from decimal import Decimal


class pressureSensor(object):

    def __init__(self):
        try:
            self.ser = "Serial('/dev/USBttyx', 115200, 8, 'N', 1, 0.1, 0, 0, 0, 0)"
            print('p sensor connected')
        except:
            print('No Pressure Sensor Detected')

    def read_pressure(self):
        '''
        Reads Pressure from the IDEX sensor
        :return: Pressure in psi
        '''

        self.ser #.flushInput()
        self.ser #.write('RB412\r\n')
        # x = int(r[2:9], 16) move this back in when implamenting
        x = random.random()  # take this out
        pressure = ((((x * 1000) / (2 ** 22)) * 100) * 0.000145)
        print(x)
        return pressure
