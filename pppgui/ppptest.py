#!/usr/bin/python
# ---------------------------------------------------------------------
#  Copyright (C) 2020 Roche Sequencing Solutions.  All rights reserved.
#
#  Purpose: Pressure testing class that controls the robot, pump, and pressure sensor.
#
#  Author : Othman Chaney (othman.chaney@roche.com) under joel's mentor-ship
#
#  (for new PPP Pressure Tester rig)
# ---------------------------------------------------------------------
import os, sys
sys.path.append("/home/othman/PycharmProjects/GitStuff/OC-playgroung/pppgui/fluidics")
import time
import datetime
from csv import writer
from csv import DictWriter
from gantryTecan import gantryTecan
from CentrisPump import CentrisPump
from lib_pressure_sensor import pressureSensor
# outline
# Make a class that includes the following:
# inits the robot, pump. and pressure tester
# homes the robot
# library on the location of the 4 lanes per chip
# have a function per chip that calls into the location of each lane on the chip
# have a function that does the pressure test and the clog test
# incorporate the pressure and clog test into each lane on a chip
dt = datetime.datetime.now()
gc = gantryTecan()
cp = CentrisPump()
ps = pressureSensor()

class PressureTest(object):

    def __init__(self):
        print('hi running pressure test')
        cp.centrisInit()
        gc.init()

    def home(self):
        gc.home()

    def ref_inletx(self, chip):
        chip_numb = chip
        if chip_numb in ('1', '9'):
            chip_numbs = 0
        elif chip_numb in ('2', '10'):
            chip_numbs = 1
        elif chip_numb in ('3', '11'):
            chip_numbs = 2
        elif chip_numb in ('4', '12'):
            chip_numbs = 3
        elif chip_numb in ('5', '13'):
            chip_numbs = 4
        elif chip_numb in ('6', '14'):
            chip_numbs = 5
        elif chip_numb in ('7', '15'):
            chip_numbs = 6
        elif chip_numb in ('8', '16'):
            chip_numbs = 7
        else:
            chip_numbs = 100
            print('pick a number between 1 and 16 please')
        return chip_numbs

    def chip_inlet_x(self, chip):
        chip_location_x1 = [0, 1, 2, 3]
        chip_location_x2 = [4, 5, 6, 7]
        chip_numbs = self.ref_inletx(chip)
        chip_inlet_location = int
        if int(chip_numbs) in chip_location_x1:
            chip_inlet_location = 93.05 * float(chip_numbs)
        elif int(chip_numbs) in chip_location_x2:
            chip_numbss = int(chip_numbs) - 4
            chip_inlet_location = 406.4 + 93.05 * float(chip_numbss)
        else:
            chip_inlet_location = 'nothing'
        return chip_inlet_location

    def chip_inlet_y(self, chip):
        chip_numb = chip
        chip_location_y1 = ['1', '2', '3', '4', '5', '6', '7', '8']
        chip_location_y2 = ['9', '10', '11', '12', '13', '14', '15', '16']
        y_axis = float
        if chip_numb in chip_location_y1:
            y_axis = 2.85
        elif chip_numb in chip_location_y2:
            y_axis = 177.8
        else:
            y_axis = 'nothing for y'
        return y_axis

    def lane_loop_pressure_test(self, chip):
        distance_between_inlets = 3.9125
        y_axis = self.chip_inlet_y(chip)
        z_in_max = '24' # need to find this out before actually intergrating
        z_in_slow = '4' # find this out
        z_out_max = '25' # find this out
        z_out_slow = '5' # find this out
        for chip_numbs in range(0, 7):
            inlet1 = self.chip_inlet_x(chip)
            gc.moveAbs(axs='y', pos=y_axis, spd=600)
            gc.moveAbs(axs='x', pos=inlet1, spd=600)
            gc.moveAbs(axs='z2', pos=z_in_max, spd=600)
            self.prepressure_test_pull()
            gc.moveAbs(axs='z2', pos=z_in_slow, spd=0.5)
            p1 = self.pressure_test()
            c1 = self.clog_test()
            lane1 = str(p1 + c1)
            gc.moveAbs(axs='z2', pos=z_out_slow, spd=0.5)
            gc.moveAbs(axs='z2', pos=z_out_max, spd=600)
            inlet2 = inlet1 + distance_between_inlets
            print(inlet2)
            gc.moveAbs(axs='y', pos=y_axis, spd=600)
            gc.moveAbs(axs='x', pos=inlet2, spd=600)
            gc.moveAbs(axs='z2', pos=z_in_max, spd=600)
            self.prepressure_test_pull()
            gc.moveAbs(axs='z2', pos=z_in_slow, spd=0.5)
            p2 = self.pressure_test()
            c2 = self.clog_test()
            lane2 = str(p2 + c2)
            gc.moveAbs(axs='z2', pos=z_out_slow, spd=0.5)
            gc.moveAbs(axs='z2', pos=z_out_max, spd=600)
            inlet3 = inlet2 + distance_between_inlets
            print(inlet3)
            gc.moveAbs(axs='y', pos=y_axis, spd=600)
            gc.moveAbs(axs='x', pos=inlet3, spd=600)
            gc.moveAbs(axs='z2', pos=z_in_max, spd=600)
            self.prepressure_test_pull()
            gc.moveAbs(axs='z2', pos=z_in_slow, spd=0.5)
            p3 = self.pressure_test()
            c3 = self.clog_test()
            lane3 = str(p3 + c3)
            gc.moveAbs(axs='z2', pos=z_out_slow, spd=0.5)
            gc.moveAbs(axs='z2', pos=z_out_max, spd=600)
            inlet4 = inlet3 + distance_between_inlets
            print(inlet4)
            gc.moveAbs(axs='y', pos=y_axis, spd=600)
            gc.moveAbs(axs='x', pos=inlet4, spd=600)
            gc.moveAbs(axs='z2', pos=z_in_max, spd=600)
            self.prepressure_test_pull()
            gc.moveAbs(axs='z2', pos=z_in_slow, spd=0.5)
            p4 = self.pressure_test()
            c4 = self.clog_test()
            lane4 = str(p4 + c4)
            gc.moveAbs(axs='z2', pos=z_out_slow, spd=0.5)
            gc.moveAbs(axs='z2', pos=z_out_max, spd=600)
            date = dt.strftime("%d/%b/%y")
            field_names = ['Chip #', 'Date', 'Lane1 (PT/CT)', 'Lane2 (PT/CT)', "Lane3 (PT/CT)", "Lane4 (PT/CT)"]
            row_dicts = {'Chip #': chip, 'Date': date, 'Lane1 (PT/CT)': lane1, 'Lane2 (PT/CT)': lane2,
                     "Lane3 (PT/CT)": lane3, "Lane4 (PT/CT)": lane4}
            x = '   {}              {}              {}                                {}                          {}                             {}'
            y = x.format(chip, date, lane1.split(':')[1], lane2.split(':')[1], lane2.split(':')[1], lane4.split(':')[1])
            self.append_dict_as_row('/home/othman/Desktop/test.csv', row_dicts, field_names)
            print(lane1.split(':')[1], lane2, lane3, lane4)
            cp.centrisInit()
            '''chip = [chip]
            date = [dt.strftime("%d/%b/%y")]
            lane1 = [lane1.split(':')[1]]
            lane2 = [lane2.split(':')[1]]
            lane3 = [lane3.split(':')[1]]
            lane4 = [lane4]
            dicts = {'Chip #': chip, 'Date': date, 'Lane1 (PT/CT)': lane1, 'Lane2 (PT/CT)': lane2, "Lane3 (PT/CT)": lane3, "Lane4 (PT/CT)": lane4}
            df = pd.DataFrame(dicts)
            return df.to_string(col_space =25,justify = "justify", header=False, index=False)'''
            return y
        else:
            print('nice try')

    def append_dict_as_row(self, file_name, dict_of_elem, field_names):
        with open(file_name, 'a+') as write_obj:
            dict_writer = DictWriter(write_obj, fieldnames=field_names)
            dict_writer.writerow(dict_of_elem)

    def clog_test(self):
        result = None
        p1 = ps.read_pressure()
        cp.openASV()
        time.sleep(2)
        cp.closeASV()
        p2 = ps.read_pressure()
        if p1 > p2:
            result = '/Pass'
        elif p1 < p2:
            result = '/Fail'
        elif p1 == p2:
            result = '/Fail'
        return result

    def prepressure_test_pull(self):
        cp.pull(volume=900, speed=300, inlet_valve='outlet_pos')

    def pressure_test(self):
        cp.push(volume=100, speed=50, inlet_valve='outlet_pos')
        p1 = ps.read_pressure()
        # time.sleep(10)
        results=None
        p2 = ps.read_pressure()
        if (p1 - p2) < 1:
            results = "%f:Pass" % p2
        elif (p1 - p2) > 1:
            results = "%f:Fail" % p2
        elif p1 == p2:
            results = "%f:Pass" % p2
        return results

    def test_gui(self, chip):
        chip_numb = chip
        self.ref_inletx(chip=chip_numb)
        self.chip_inlet_x(chip=chip_numb)
        self.chip_inlet_y(chip=chip_numb)
        x = self.lane_loop_pressure_test(chip=chip_numb)
        return x

# if __name__ == '__main__':
    # chip_numb = raw_input('\nPlease select a number between 1 and 16 \n')
  #  PT = PressureTest()
   #  PT.ref_inletx()
    # PT.chip_inlet_x()
    # PT.chip_inlet_y()
    # PT.lane_loop_pressure_test()