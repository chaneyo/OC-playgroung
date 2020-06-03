import time
import RPi.GPIO as gpio

class pumpandgpio(object):

    def __init__(self):
        print('Pump Init')
        print('ASV Init')

    def pump_on(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('Pump is Running')

    def pump_off(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.LOW)
        print('Pump is Off')

    def ASV1_in_open(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('Lane 1 inlet open')

    def ASV2_in_open(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('Lane 2 inlet open')

    def ASV3_in_open(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('Lane 3 inlet open')

    def ASV4_in_open(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('Lane 4 inlet open')

    def ASV1_in_close(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.LOW)
        print('Lane 1 inlet close')

    def ASV2_in_close(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.LOW)
        print('Lane 2 inlet close')

    def ASV3_in_close(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.LOW)
        print('Lane 3 inlet close')

    def ASV4_in_close(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.LOW)
        print('Lane 4 inlet close')

    def all_ASV_outlet_open(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('All ASV outlet open')

    def all_ASV_outlet_close(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('All ASV outlet closed')

    def main_inlet_ASV_open(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.HIGH)
        print('Main ASV Open')

    def main_inlet_ASV_close(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.out)
        gpio.output(18, gpio.LOW)
        print('Main ASV Cloased')

    def clamp_closed(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(22, gpio.input)
        gpio.input(22, gpio.LOW)
        print('Clamp is not closed please close the clamp')