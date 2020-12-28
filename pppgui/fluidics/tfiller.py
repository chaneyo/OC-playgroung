import time

class troughF(object):

    def __init__(self):
        print('Init')
        print(time.asctime(time.localtime(time.time())))

    def turn_on(self, numb):
        if int(numb) < 100:
            val = int(numb)
            print('You pumped %f amount' %val)
        else:
            tal = str(numb)
            print('nice try but ' + tal + ' is a number too large')



#if __name__ == '__main__':
#    print(time.asctime(time.localtime(time.time())))
#    sg = sachingpio()
#    turn = ['off', 'OFF', 'Off']
#    while True:
#        numb = raw_input('\nPlease select a number between 0 and 18 \nIf you want to turn off then type "off"\n')
#        sg.turn_on(numb)