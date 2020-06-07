#!/usr/bin/python
# ---------------------------------------------------------------------
#  Copyright (C) 2020 Roche Sequencing Solutions.  All rights reserved.
#
#  Purpose: Pressure testing class that controls pump, ASV, and pressure sensor.
#
#  Author : Othman Chaney (othman.chaney@roche.com) under joel's mentor-ship
#
#  (for new SLT Pressure Tester rig)
# ---------------------------------------------------------------------
# outline
# Make a class that includes the following:
# inits the pump and pressure tester
# have a function per chip lane that calls the pressure test
# have a function that does the pressure test and the clog test per chip lane.
# incorporate the pressure and clog test into each lane on a chip
import os, sys
sys.path.append("/home/othman/PycharmProjects/GitStuff/OC-playgroung/pppgui/fluidics")
import time
import datetime
from csv import writer
from csv import DictWriter
from pumpandgpio import pumpandgpio
from lib_pressure_sensor import pressureSensor

dt = datetime.datetime.now()
pg = pumpandgpio()
ps = pressureSensor()

class PressureTest(object):

    def __init__(self):
        print('hi running pressure test')
        pg.main_inlet_ASV_close()

    def check_clamp(self):
        if pg.clamp_closed() =='0':
            print('clamp is closed')
        else:
            print('Clamp is not closed please close clamp')

    def lane_select(self, lane):
        if lane == '1':
            test = self.pressure_test_lane1()
        elif lane == '2':
            test = self.pressure_test_lane2()
        elif lane == '3':
            test = self.pressure_test_lane3()
        elif lane == '4':
            test = self.pressure_test_lane4()
        else:
            test = 'try again'
            print('pick a number between 1 and 4 please')
        return test

    def lane_loop_pressure_test(self, lane):
        #for lane in range(1, 4):
        p1 = self.pressure_test(lane)
        c1 = self.clog_test()
        date = dt.strftime("%d/%b/%y")
        field_names = ['Lane #', 'Date', 'Pressure Test', 'Clog Test']
        row_dicts = {'Lane #': lane, 'Date': date, 'Pressure Test': p1, 'Clog Test': c1}
        x = '   {}              {}              {}                                {}'
        y = x.format(lane, date, p1.split(':')[1], c1)
        lanes = 'Lane: %f' % int(lane)
        self.append_dict_as_row('/home/othman/Desktop/test1.csv', row_dicts, field_names)
        print(lanes, date, p1, c1)
        return y
        #else:
         #   print('nice try')

    def append_dict_as_row(self, file_name, dict_of_elem, field_names):
        with open(file_name, 'a+') as write_obj:
            dict_writer = DictWriter(write_obj, fieldnames=field_names)
            dict_writer.writerow(dict_of_elem)

    def clog_test(self):
        result = None
        p1 = ps.read_pressure()
        pg.all_ASV_outlet_open()
        time.sleep(2)
        p2 = ps.read_pressure()
        pg.ASV1_in_close()
        pg.ASV2_in_close()
        pg.ASV3_in_close()
        pg.ASV4_in_close()
        pg.all_ASV_outlet_close()
        if p1 > p2:
            result = '/Pass'
        elif p1 < p2:
            result = '/Fail'
        elif p1 == p2:
            result = '/Fail'
        return result

    def pressure_test_lane1(self):
        pg.ASV1_in_open()
        pg.main_inlet_ASV_close()
        p1 = ps.read_pressure()
        time.sleep(5)
        p2 = ps.read_pressure()
        if (p1 - p2) < 1:
            results = "%f:Pass" % p2
        elif (p1 - p2) > 1:
            results = "%f:Fail" % p2
        elif p1 == p2:
            results = "%f:Pass" % p2
        return results

    def pressure_test_lane2(self):
        pg.ASV2_in_open()
        pg.main_inlet_ASV_close()
        p1 = ps.read_pressure()
        time.sleep(5)
        p2 = ps.read_pressure()
        if (p1 - p2) < 1:
            results = "%f:Pass" % p2
        elif (p1 - p2) > 1:
            results = "%f:Fail" % p2
        elif p1 == p2:
            results = "%f:Pass" % p2
        return results

    def pressure_test_lane3(self):
        pg.ASV3_in_open()
        pg.main_inlet_ASV_close()
        p1 = ps.read_pressure()
        time.sleep(5)
        p2 = ps.read_pressure()
        if (p1 - p2) < 1:
            results = "%f:Pass" % p2
        elif (p1 - p2) > 1:
            results = "%f:Fail" % p2
        elif p1 == p2:
            results = "%f:Pass" % p2
        return results

    def pressure_test_lane4(self):
        pg.ASV4_in_open()
        pg.main_inlet_ASV_close()
        p1 = ps.read_pressure()
        time.sleep(5)
        p2 = ps.read_pressure()
        if (p1 - p2) < 1:
            results = "%f:Pass" % p2
        elif (p1 - p2) > 1:
            results = "%f:Fail" % p2
        elif p1 == p2:
            results = "%f:Pass" % p2
        return results

    def pressure_test(self, lane):
        pg.pump_on()
        time.sleep(1)
        pg.main_inlet_ASV_open()
        time.sleep(2)
        results = self.lane_select(lane)
        return results

    def test_gui(self, lane):
        lane_numb = lane
        x = self.lane_loop_pressure_test(lane=lane_numb)
        return x
# def prepressure_test_calibrate(self):
    # meed to add this section later

if __name__ == '__main__':
    lane_numb = raw_input('\nPlease select a number between 1 and 4 \n')
    PT = PressureTest(p1=int, p2=int)
    PT.check_clamp()
    PT.lane_loop_pressure_test(lane_numb)