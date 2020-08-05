import random
import csv
import time
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from serial import Serial
from decimal import Decimal


class pressureSensor(object):

    def __init__(self):
        try:
            # self.ser = "Serial('/dev/USBttyx', 115200, 8, 'N', 1, 0.1, 0, 0, 0, 0)"
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
        z = ((x*1000)/(4194304))*0.0145038"""  # move this back in when implamenting
        z = random.randrange(10)  # take this out
        time.sleep(1)
        print(z)
        return z

    def plotter(self):
        plt.style.use('fivethirtyeight')

        x_vals += 1
        y_vals = self.read_pressure()

        index = count()

    def animate(self):
        # data = pd.read_csv('data.csv')
        z = 0
        x = (z + 1) # data['x_value']
        y1 = self.read_pressure() # data['pressure']

        plt.cla()

        plt.plot(x, y1, label='pressure PSI')

        plt.legend(loc='upper left')
        plt.tight_layout()

        ani = FuncAnimation(plt.gcf(), animate, interval=1000)

        plt.tight_layout()
        plt.show()

    def csv(self):
        path = "/home/othman/Desktop/testdis.csv"
        # f = open("/home/othman/Desktop/testdis.csv", "w", newline="")
        # c = csv.writer(f)
        # c.writerow(["pressure"])

        for i in range(1000000):
            f = open(path, "a", newline="", encoding='utf-8-sig')
            c = csv.writer(f)
            c.writerow([self.read_pressure()])
            f.close()
        # f.close()
