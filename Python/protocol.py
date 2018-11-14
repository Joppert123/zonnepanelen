from connect import *


def Transmit(ser, command):
    ser.write(ArduinoEncodeHex(command))
    response = ser.read(1)
    for i in range(10):
        if response == b'':
            Report("STERF!")
            time.sleep(3)
            ser.write(ArduinoEncodeHex(command))
            response = ser.read(1)
        else:
            return response


def ArduinoDecodeHex(arg):

    output = arg.rstrip().decode()
    return output


# For debuging purposes:
debug = 1
if debug == 1:
    Connect()
    print("Debugging commands.")
    commands = [
        "get_sunscreen_min_extend",
        "get_sunscreen_max_extend",
        "get_sunscreen_status",
        "get_sunscreen_manual",
        "set_sunscreen_min_extend=5",
        "set_sunscreen_max_extend=200",
        "sunscreen_extend",
        "sunscreen_retract",
        "set_min_temp=15",
        "set_max_temp=30",
        "get_min_temp",
        "get_max_temp",
        "get_temp",
        "set_min_light=1",
        "set_max_light=6",
        "get_min_light",
        "get_max_light",
        "get_light",
        "get_sonar_distance",
        "set_sunscreen_manual=0",
    ]

    for command in commands:
        response = int(Transmit(connections[0].ser, command).hex(), 16)
        print(command + ": " + str(response))

# Debugging commands:
# get_sunscreen_status: b'0\r\n'
# get_sunscreen_min_extend: b'\x05'
# get_sunscreen_max_extend: No response
# set_sunscreen_min_extend: b'\xaa'
# set_sunscreen_max_extend: b'\xaa'
# get_temp: b'\x0e'
# get_min_temp: b'\x02'
# get_max_temp: b'\xff'
# set_min_temp: b'\xaa'
# set_max_temp: b'\xaa'
# get_light: b'\x02'
# get_sonar_distance: b'='
# sunscreen_extend: b'\xaa'
# sunscreen_retract: b'\xaa'
# [Finished in 45.691s]
