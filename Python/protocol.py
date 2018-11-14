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


def SetModus(modus):
    winter = [
        # Minimal value (distance) at which the sunscreen responses
        "set_sunscreen_min_extend=10",
        "set_sunscreen_max_extend=50",
        # Values inbeetween which the sunscreen is open
        "set_min_temp=0",
        "set_max_temp=255",
        # Values inbetween which the sunscreen is open
        "set_min_light=0",
        "set_max_light=11",
    ]

    summer = [
        # Minimal value (distance) at which the sunscreen responses
        "set_sunscreen_min_extend=10",
        "set_sunscreen_max_extend=50",
        # Values inbeetween which the sunscreen is open
        "set_min_temp=100",
        "set_max_temp=255",
        # Values inbetween which the sunscreen is open
        "set_min_light=3",
        "set_max_light=5",
    ]

    if modus == "winter":
        mode = winter.copy()
    elif modus == "summer":
        mode = summer.copy()
    else:
        Report("Invalid modus")

    for command in modus:
        response = int(Transmit(connections[0].ser, command).hex(), 16)
        print(command + ": " + str(response))

# connections[0].ser.close()

# For debuging purposes:
debug = 0
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

    for command in summer:
        response = int(Transmit(connections[0].ser, command).hex(), 16)
        print(command + ": " + str(response))


# Debugging commands:
# COM4 connected
# Initializing handshake
# Handshake confirmed
# Debugging commands.
# get_sunscreen_min_extend: 5
# get_sunscreen_max_extend: 200
# get_sunscreen_status: 0
# get_sunscreen_manual: 0
# set_sunscreen_min_extend=5: 170
# set_sunscreen_max_extend=200: 170
# sunscreen_extend: 170
# sunscreen_retract: 170
# set_min_temp=15: 170
# set_max_temp=30: 170
# get_min_temp: 15
# get_max_temp: 30
# get_temp: 188
# set_min_light=1: 170
# set_max_light=6: 170
# get_min_light: 1
# get_max_light: 6
# get_light: 0
# get_sonar_distance: 205
# set_sunscreen_manual=0: 170
# [Finished in 6.594s]
