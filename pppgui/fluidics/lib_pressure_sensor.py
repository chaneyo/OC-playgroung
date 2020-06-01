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

        """self.ser.flushInput()
        self.ser.write('RB404\r\n')
        r = ser.readline()
        x = int(r[2:9],16)
        print('int value: ',x)
        z = ((x*1000)/(4194304))*0.0145038""" # move this back in when implamenting
        z = random.random()  # take this out
        print(z)
        return z
