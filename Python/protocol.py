from connect import *

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
debug = 0
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
