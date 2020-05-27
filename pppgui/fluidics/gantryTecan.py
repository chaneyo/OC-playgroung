#!/home/genia/Enthought/Canopy_64bit/User/bin/python

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

"""import time
import socket

tecanIpAddr = '192.168.0.198'
tecanPort = 9897
tecanBufSize = 1024

# Tecan status strings
noErrorCmdFinished = '`'
noErrorCmdBusy = '@'
cmdStringIsUsed = 'A'
invalidCmdStringOperand = 'c'
invalidGroupCmdUsage = 'd'
events = 'e'
scanningInProgress = 'f'
invalidCmdOperation = 'g'
responseTimeOut = 'j'
deviceError = 'k'
invalidDeviceID = 'l'
terminateCmd = 't'
none = 255

# Tecan command strings
ACK = '@'
QUERY = '?'
DONE = '%'
MARKER = '#'
EVENT = '!'
NONE = ' '
STX = '\x02'
ETX = '\x03'

# tecanCommObj = None
currentPosX = 0.0
currentPosY = 0.0
currentPosZ1 = 0.0
currentPosZ2 = 0.0

CLLDSENSITIVITY = 3  # max sensitivity for cLLD axis
CLLDZ1FREQUENCY = 127
CLLDZ2FREQUENCY = CLLDZ1FREQUENCY + 2
CLLDDUTYCYCLE = 63
BENDTOLERANCE = 1.5  # max allowable deflection for tip, *please account for tip geometry*
ACCEPTWINDOW = 0.5  # acceptence window for double detection method

DETECTMODE = 1
XMAXSPEED = 600
YMAXSPEED = 600
Z1MAXSPEED = 600
Z2MAXSPEED = Z1MAXSPEED
MAXMOVESPEEDS = [XMAXSPEED, YMAXSPEED, Z1MAXSPEED, Z2MAXSPEED]
XMINSPEED = 5
YMINSPEED = XMINSPEED
Z1MINSPEED = 0.5
Z2MINSPEED = Z1MINSPEED
MINMOVESPEEDS = [XMINSPEED, YMINSPEED, Z1MINSPEED, Z2MINSPEED]
MAXSEARCHSPEED = 150
MINSEARCHSPEED = 1
CLLDSEARCHSPEED = 5
CLLDSEARCHRANGE_Z = 1.0
CLLDSEARCHSTEP = 0.1
MOVEMAXSPEED = 600
PIERCESPEED = 10

x_axis = 1
y_axis = 2
z1_axis = 3
z2_axis = 7
pierce_axis = z1_axis
dispense_axis = z2_axis


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class sendToTecan(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.YMAXSPEED = None
        self.XMAXSPEED = None
        self.Z2MAXSPEED = None
        self.Z1MAXSPEED = None
        self.y_axis = None
        self.x_axis = None
        self.z2_axis = None
        self.z1_axis = None
        self.currentPosZ2 = None
        self._commHandle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def cycle_connection(self):
        self.disconnect()
        self.connect()

    def connect(self):
        """ 'DEPRECATED in favor of `cycle_connection`' """
        self._commHandle.connect((tecanIpAddr, tecanPort))
        return True  # had to add for gantryTecan.py to connect properly

    def _recvReply(self):
        gantryReply = bytearray(tecanBufSize)
        replySize = 0
        while True:
            readByte = self._commHandle.recv(1)
            if readByte == STX:
                replySize = 0
                gantryReply[replySize] = readByte
                replySize += 1
            elif readByte == ETX:
                gantryReply[replySize] = readByte
                replySize += 1
                # read one more byte for checksum
                gantryReply[replySize] = self._commHandle.recv(1)
                replySize += 1
                break
            else:
                gantryReply[replySize] = readByte
                replySize += 1

        # calculate checksum again to compare
        checkSum = 0
        for x in range(0, replySize - 1):
            checkSum ^= gantryReply[x]

        gantryReplyStr = "".join("x%02x" % b for b in gantryReply[:replySize])

        cleanGantryReply = bytearray(replySize - 3)
        for x in range(0, replySize - 3):
            cleanGantryReply[x] = gantryReply[x + 1]

        if gantryReply[replySize - 1] != checkSum:
            return "Tecan Reply Checksum error, gantry reply: %s", str(cleanGantryReply)

        # logging the recieved packet
        return str(cleanGantryReply)

    # sendCmd also return the reply of the sent command
    def _sendNonBlockingCmd(self, cmd):
        # create byte array from command
        cmdBytes = bytearray(cmd, 'utf-8')
        # create cmdPackage, size is len of cmd + 5 for headers and checksum
        cmdPackage = bytearray(len(cmdBytes) + 5)
        # First data byte is STX
        cmdPackage[0] = STX
        # Second Byte is Host ID always fixed at 1
        cmdPackage[1] = 0x31
        # Third Byte is Sequence 1 - 7
        cmdPackage[2] = 0x31
        # Command string include command string ID and command block
        for x in range(0, len(cmdBytes)):
            cmdPackage[x + 3] = cmdBytes[x]
        # Next to last byte is ETX
        cmdPackage[len(cmdPackage) - 2] = ETX
        # Last Byte is Checksum calculating every byte from STX to ETX
        # calculate Checksum using XOr
        cmdPackage[len(cmdPackage) - 1] = 0x00
        checkSum = 0
        for x in range(0, len(cmdPackage) - 1):
            checkSum ^= cmdPackage[x]
        cmdPackage[len(cmdPackage) - 1] = checkSum
        # send out the package and hope for the best...
        self._commHandle.send(cmdPackage)
        # cmdPackageStr = "".join("x%02x" % b for b in cmdPackage)

    # sendCmd also return the final reply of the sent command after it has completed
    def sendCmd(self, cmd, pierce=False):
        global posReply
        print(cmd)
        self._sendNonBlockingCmd(cmd)
        # we look for command ack or done
        ackReply = ''
        queryReply = 0
        askAgain = True
        bypass = False
        posQuery = False
        forcePierce = False
        cLLD = False
        axis = ''
        if cmd[3:5] == '?0':  # check if position query
            bypass = True
            posQuery = True
            posReply = ''
        elif 'P' in cmd:  # check if pierce command
            bypass = True
            forcePierce = True
        elif 'B' in cmd:  # check if cLLD search command
            bypass = True
            cLLD = True
        elif '?' in cmd:  # check if general query
            bypass = True
        while askAgain:
            lastReply = ackReply
            ackReply = self._recvReply()
            # print "\r ackReply: %s" %(ackReply)
            if posQuery == True and '?' in ackReply:  # if position query is detected, save position query value
                posReply = ackReply[9:len(ackReply)]
            elif '?' in ackReply:  # if general query is detected, save response
                queryReply = ackReply
            if ackReply[1] == invalidDeviceID:
                print("\r Invalid Device ID.")
                break
            elif ackReply[1] == noErrorCmdFinished or ackReply[1] == noErrorCmdBusy or ackReply[1] == cmdStringIsUsed:
                if ackReply[-1] == ACK:
                    pass
                    # print "\r ACK reply, checking reply again"
                elif ackReply[-1] == DONE:
                    # print "\r DONE reply"
                    askAgain = False
            else:
                # Re-init upon error if not bypass
                if not bypass:
                    axis = ackReply[4]
                    time.sleep(1)
                    print("Error reply: %s", ackReply)
                    print("The axis that failed is: %s" % (axis))
                    print("Clearing the error on axis: %s" % (axis))
                    self.sendCmd('1/%sC' % (axis))
                    if axis == '9':
                        error_msg = "Error reply " + str(ackReply)
                        print(error_msg)
                    else:
                        self.sendCmd('1/{axs}N1'.format(axs=axis))
                        print('Homing the robot after the error...')
                    self.sendCmd('1(/3Z/7Z)')
                    # self.sendCmd('1/1Z')
                    # self.sendCmd('1/2Z')
                    self.disconnect()
                askAgain = False
        if posQuery == True:  # Return raw position coordinate instead of ackReply if position query
            return posReply
        elif queryReply:
            return queryReply
        elif posQuery == False:
            return ackReply

    def init(self):
        self.axis_power(axis='z2', switch='on')
        self.axis_power(axis='z1', switch='on')
        self.axis_power(axis='x', switch='on')
        self.axis_power(axis='y', switch='on')
        self.sendCmd('1(/{z1_axis}Z/{z2_axis}Z)'.format(z1_axis=self.z1_axis, z2_axis=self.z2_axis))  # z1, z2 axis
        self.sendCmd('1(/{x_axis}ZR)'.format(x_axis=self.x_axis))  # initialize x axis
        self.sendCmd('1(/{y_axis}ZR)'.format(y_axis=self.y_axis))  # initialize y axis
        self.sendCmd('1/1u9,3500')  # setting acceleration to 30000mm/s2 default: X-3500, Y-3900, Z-6000, Z_univ-1000
        self.sendCmd('1/2u9,3900')
        self.sendCmd('1/3u9,3000')
        self.sendCmd('1/7u9,3000')

    def moveAbs(self, axs, pos, spd=XMAXSPEED):
        if not isinstance(axs, int):
            axs = axs.lower()
            self.setSpeed(axs, spd)
        if axs == 'x' or axs == self.x_axis:
            axs = 1
        elif axs == 'y' or axs == self.y_axis:
            axs = 2
        elif axs == 'z1' or axs == self.z1_axis:
            axs = 3
        elif axs == 'z2' or axs == self.z2_axis:
            axs = 7
        else:
            print("moveAbs Error! Axis unknown.")
        taxis = 999
    # print axs
        cmd = '1/{axs}A{pos}R'.format(axs=axs, pos=pos)
        print(cmd)
        print("CMD: " + str(cmd) + '/r')
        self.sendCmd(cmd)

    def home(self):
        self.moveAbs(axs='z1', pos=0, spd=self.Z1MAXSPEED)
        self.moveAbs(axs='z2', pos=0, spd=self.Z2MAXSPEED)
        self.moveAbs(axs='x', pos=0, spd=self.XMAXSPEED)
        self.moveAbs(axs='y', pos=0, spd=self.YMAXSPEED)

    def setSpeed(self, axs, spd):
        axs = axs.lower()
        self.sendCmd('1/{axs}u10,{speed}'.format(axs=axs, speed=spd))  # set axis move speed

    def axis_power(self, axis='z1', switch='off'):
        global axs
        if axis.lower() == 'x':
            axs = 1
        elif axis.lower() == 'y':
            axs = 2
        elif axis.lower() == 'z1':
            axs = 3
        elif axis.lower() == 'z2':
            axs = 7

        if 'off' in switch.lower():
            self.sendCmd('1/{}N0'.format(str(axs)))
        elif 'on' in switch.lower():
            self.sendCmd('1/{}N1'.format(str(axs)))

    # disconnect cleanly by closing the file handle
    def disconnect(self):
        """ 'DEPRECATED in favor of `cycle_connection`' """
        SHUT_RDWR = 1
        # self.__commHandle.shutdown(SHUT_RDWR)
        self._commHandle.close()
        print("Tecan __commHandle has been closed")

    def __del__(self):
        self.disconnect()"""
