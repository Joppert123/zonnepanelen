from connect import *
from protocol import *

temp = None
light = None
distance = None
min_temp = None
max_temp = None
min_light = None
max_light = None
sunscreen_min = None
sunscreen_max = None
sunscreen_status = None
sunscreen_manual = None


def TransmitBetter(command, arg=""):
    global temp
    global light
    global distance
    global min_temp
    global max_temp
    global min_light
    global max_light
    global sunscreen_min
    global sunscreen_max
    global sunscreen_status
    global sunscreen_manual

    commands = [
        "get_sunscreen_min_extend",
        "get_sunscreen_max_extend",
        "get_sunscreen_status",
        "get_sunscreen_manual",
        "set_sunscreen_min_extend",
        "set_sunscreen_max_extend",
        "sunscreen_extend",
        "sunscreen_retract",
        "set_min_temp",
        "set_max_temp",
        "get_min_temp",
        "get_max_temp",
        "get_temp",
        "set_min_light",
        "set_max_light",
        "get_min_light",
        "get_max_light",
        "get_light",
        "get_sonar_distance",
        "set_sunscreen_manual",
    ]

    map = {
        "get_temp": temp,
        "get_light": light,
    }

    if command not in commands:
        Report("command not in commands")
        return

    if command[:3] == "set":
        if arg != "" and isinstance(arg, str) is True:
            command = command + "=" + arg
            # Debug:
            print(command)
        else:
            Report("no arg provided")
            return

    # response = int(Transmit(connections[0].ser, command).hex(), 16)
    response = "response"

    if command[:3] == "get":
        if command == "get_sunscreen_min_extend":
            sunscreen_min = response
        if command == "get_sunscreen_max_extend":
            sunscreen_max = response
        if command == "get_sunscreen_status":
            sunscreen_status = response
        if command == "get_sunscreen_manual":
            sunscreen_manual = response
        if command == "get_min_temp":
            min_temp = response
        if command == "get_max_temp":
            max_temp = response
        if command == "get_temp":
            temp = response
        if command == "get_min_light":
            min_light = response
        if command == "get_max_light":
            max_light = response
        if command == "get_light":
            light = response
        if command == "get_sonar_distance":
            distance = response

print(temp)
TransmitBetter("get_temp")
print(temp)
TransmitBetter("set_max_temp", "50")
