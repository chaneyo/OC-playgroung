import time
import RPi.GPIO as gpio

class sachingpio(object):

    def __init__(self):
        print('Init')

    def turn_on(self, numb):
        if numb in ranges:
            val = int(numb)
            gpio.setmode(gpio.BCM)
            gpio.setup(val, gpio.out)
            gpio.output(val, gpio.HIGH)
            print('You turned on GPIO%f' %val)
        elif numb in turn:
            tal = str(numb)
            gpio.output(1, gpio.LOW)
            gpio.output(2, gpio.LOW)
            gpio.output(3, gpio.LOW)
            gpio.output(4, gpio.LOW)
            gpio.output(5, gpio.LOW)
            gpio.output(6, gpio.LOW)
            gpio.output(7, gpio.LOW)
            gpio.output(8, gpio.LOW)
            gpio.output(9, gpio.LOW)
            gpio.output(10, gpio.LOW)
            gpio.output(11, gpio.LOW)
            gpio.output(12, gpio.LOW)
            gpio.output(13, gpio.LOW)
            gpio.output(14, gpio.LOW)
            gpio.output(15, gpio.LOW)
            gpio.output(16, gpio.LOW)
            gpio.output(17, gpio.LOW)
            gpio.output(18, gpio.LOW)
            print('turning ' + tal + ' all GPIO')
        else:
            print('nice try but pick a number between 1 and 18')



if __name__ == '__main__':
    print(time.asctime(time.localtime(time.time())))
    sg = sachingpio()
    ranges = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    turn = ['off', 'OFF', 'Off']
    while True:
        numb = raw_input('\nPlease select a number between 0 and 18 \nIf you want to turn off then type "off"\n')
        sg.turn_on(numb)