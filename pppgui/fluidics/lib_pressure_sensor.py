import random
import csv
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
        z = random.random()  # take this out
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
        x_value = 0
        pressure = self.read_pressure()

        fieldnames = ["x_value", "pressure"]

        with open('data.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

        while True:
            with open('data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                info = {
                    "x_value": x_value,
                    "pressure": pressure
                }

                csv_writer.writerow(info)
                print(x_value, pressure)

                x_value += 1
                pressure = pressure

            time.sleep(1)
