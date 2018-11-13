from connect import *

import random

class Protocol(object):
    def __init__(self):
        super(Protocol, self).__init__()



# Getters:

    # Sunscreen:



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

def Transmit(ser, command):
    ser.write(ArduinoEncodeHex(command))
    response = ser.readline()
    for i in range(2):
        if response == b'':
            return "No response"
        else:
            return response
            break

def ArduinoDecodeInteger(arg):
    output = arg.rstrip().decode()
    return output


# For debuging purposes:
debug = 1
if debug == 1:
    Connect()
    print("Debugging commands.")
    commands = ["get_sunscreen_status",
                "get_sunscreen_min_extend",
                "get_sunscreen_max_extend",
                "set_sunscreen_min_extend",
                "set_sunscreen_max_extend",
                "get_temp",
                "get_min_temp",
                "get_max_temp",
                "set_min_temp",
                "set_max_temp",
                "get_light",
                "get_sonar_distance",
                "sunscreen_extend",
                "sunscreen_retract"]

    for command in commands:
        print(command + ": " + str(Transmit(connections[0].ser, command)))
