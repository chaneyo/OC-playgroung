import random
import csv
import time
import subprocess
import signal
import os
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

    def csv(self):
        path = "/home/othman/Desktop/testdis.csv"
        try:
            while True:
                for i in range(1000000):
                    f = open(path, "a", newline="", encoding='utf-8-sig')
                    c = csv.writer(f)
                    c.writerow([self.read_pressure()])
                    f.close()
        except KeyboardInterrupt:
            print("Pressed Ctrl-C to terminate the pressure collection")
            pass

    def csv_clear(self):
        data_in = ['15']
        with open('/home/othman/Desktop/testdis.csv', 'w') as outfile:
            outfile.writelines(data_in)
        x = 'cleared'
        print(x)
        return x

    def csv_move(self):
        myfile = "/home/othman/Desktop/testdis.csv"
        try:
            os.remove(myfile)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))


if __name__ == '__main__':
    p = pressureSensor()
    pro = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'python3 /home/othman/PycharmProjects/GitStuff/OC-playgroung/pppgui/fluidics/plotter.py'], preexec_fn=os.setpgrp)
    p.csv()
    os.killpg(pro.pid, signal.SIGINT)
    p.csv_clear()
