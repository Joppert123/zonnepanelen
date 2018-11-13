from connect import *

import random

class Protocol(object):
    def __init__(self):
        super(Protocol, self).__init__()



# Getters:

    def getName(arg):
        pass

    def getMode(arg):
        pass

    def getTemp(arg):
        pass

    def getLight(arg):
        pass

    def getSonor(arg):
        pass


# Setters:

    def setName(arg):
        pass

    def setMode(arg):
        pass

    def setTemp(arg):
        pass

    def setLight(arg):
        pass

    def setSonor(arg):
        pass


# WIP:

# Testing 1, 2, 3:

# class ArduinoException(Exception):
#     def __init__(self, message, errors):
#         super().__init__(message)
#
#     if response == b'':
#         print("KANKER ALLES GAAT FOUT")

def Talk(ser, command):
    ser.write(ArduinoEncodeHex(command))
    response = ser.readline()
    tries = 0
    while tries < 3:
        if response == b'':
            tries += 1
            print(tries)
            response = ser.readline()
        else:
            print(ArduinoDecodeInteger(response))
            break

def ArduinoDecodeInteger(arg):
    output = int(arg.rstrip().decode())
    return output


# For debuging purposes:
debug = 1
if debug == 1:
    Connect()
    Talk(connections[0].ser, "get_sunscreen_min_extend")
