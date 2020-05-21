import random
from decimal import Decimal

class pressureSensor(object):

    def __init__(self):
        print('p sensor')

    def connect_to_ps(self):
        pass

    def read_pressure(self):
        x = random.random()
        print(x)
        return x

