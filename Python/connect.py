import serial, time

# TO DO:
# - PEP8
# - Grammar

class Arduino():
    # Object used for storing connections.
    # For now it only contains the port name and Serial configuration.
    # TO DO:
    # - Implement UID
    # - Extend class beyond simple storage device
    def __init__(self, port, ser):
        self.port = port
        self.ser = ser

connections = []

def Connect():
    # Ports in range of 256 is derived from the maximum value our 8-bit UID.
    ports = ['COM%s' % (i+1) for i in range(256)]
    for port in ports:
        try:
            # Definitive timeout needs to be discussed.
            ser = serial.Serial(port, 19200, timeout=3)
            ser.isOpen()
            print(ser.name + " connected")
            print("Initializing handshake")
            Handshake(ser)
            connections.append(Arduino(ser.name, ser))
            pass
        except (OSError, serial.SerialException):
            pass
    if len(connections) == 0:
        print("No devices connected")

def Handshake(ser):
    connected = 0
    for i in range(3):
        # 0xaaaaaa probably also works but it's not possible to test right now.
        # TO DO:
        # - Test saner ways to express hexadecimals
        # - Test the possible need for time.sleep()

        # "Grote letters zijn cooler" - Lars, 2018
        connect = "AAAAAA"
        ser.write(ArduinoEncode(connect))

        confirm = ser.read(6)

        if confirm == b'\xab\xcd\xef':
            ser.write(ArduinoEncode(confirm[::-1].hex()))
            print("Handshake confirmed")
            connected = 1

        if connected == 1:
            break

    if connected == 0:
        print("Handshake failed")
        print("Closing " + ser.name)
        ser.close()

# Temporary placement:
def ArduinoEncode(cmd):
    end = "\0"
    return (cmd + end).encode()

def ArduinoDecode(cmd):
    return cmd.hex()

Connect()
# For debuging purposes:
for connection in connections:
    print(connection.port)
