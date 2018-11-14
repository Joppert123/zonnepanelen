import os
import sys
import time
import serial
import random

from converters import *


class Arduino():
    # Object used for storing connections.
    # For now it only contains the port name and Serial configuration.
    # TO DO:
    # - Extend class beyond simple storage device
    def __init__(self, port, ser, uid):
        self.port = port
        self.ser = ser
        self.uid = uid


connections = []
UIDS = []


def Report(s):
    # To ensure messages are reported runtime during testing.
    print(s)
    sys.stdout.flush()
    time.sleep(0.01)


def Connect():

    # Ports in range of 255 is derived from the maximum value our 8-bit UID.
    ports = ['COM%s' % (i + 1) for i in range(255)]
    for port in ports:
        try:
            # Definitive timeout needs to be discussed.
            ser = serial.Serial(port, 19200, timeout=3)
            ser.isOpen()
            Report(ser.name + " connected")
            Report("Initializing handshake")
            Handshake(ser)
            connections.append(Arduino(ser.name, ser, GenerateUID()))
            pass
        except (OSError, serial.SerialException):
            pass
    if len(connections) == 0:
        Report("No devices connected")


def Handshake(ser):
    connected = 0
    for i in range(3):
        # "Grote letters zijn cooler" - Lars, 2018
        connect = "AAAAAA"
        ser.write(ArduinoEncodeHex(connect))

        confirm = ser.read(6)
        Report(confirm)

        if confirm == b'\xab\xcd\xef':
            ser.write(ArduinoEncodeHex(confirm[::-1].hex()))
            connected = 1

        if connected == 1:
            Report("Handshake confirmed")
            break

    if connected == 0:
        Report("Handshake failed")
        Report("Closing " + ser.name)
        ser.close()

# Temporary placement:


def ArduinoEncodeHex(cmd):
    end = "\0"
    return (cmd + end).encode()


def ArduinoDecodeHex(cmd):
    return cmd.hex()


def GenerateUID():
    while 1:
        uid = random.randint(0, 255)
        if uid in UIDS:
            pass
        else:
            UIDS.append(uid)
            # to_hex() Adds a preceding zero (0)
            return to_hex(uid)[1::]
            break


# For debuging purposes:
debug = 0
if debug == 1:
    Connect()
    for connection in connections:
        Report(connection.port + " " + str(connection.uid))
