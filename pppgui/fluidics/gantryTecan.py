import time

class gantryTecan(object):

    def __init__(self):
        print('init')

    def home(self):
        pass

    def init(self):
        pass

    def moveAbs(self, axs, pos, spd):
        axes = str(axs)
        position = str(pos)
        speed = str(spd)
        print(axes, speed, position)
