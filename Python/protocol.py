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

# Converters:

def to_bin(dec):
    if dec == 0:
        return '0'
    return to_bin(dec // 2) + str(dec % 2)

def to_hex(dec):
    if dec == 0:
        return '0'
    return to_hex(dec // 16) + "0123456789abcdef"[dec % 16]

def from_bin(bin):
    if bin == "":
        return 0
    return 2 * from_bin(str(bin)[:-1]) + int(str(bin)[-1])

def from_dec(dec):
    if dec == "":
        return 0
    return 10 * from_dec(str(dec)[:-1]) + int(str(dec)[-1])

def from_hex(hex):
    if hex == "":
        return 0
    map = {"0": 0,
           "1": 1,
           "2": 2,
           "3": 3,
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7,
           "8": 8,
           "9": 9,
           "a": 10,
           "b": 11,
           "c": 12,
           "d": 13,
           "e": 14,
           "f": 15}
    return 16 * from_hex(hex[:-1]) + map[hex[-1]]

# print(to_bin(7))
# print(to_hex(0))
# print(from_bin(1010))
# print(from_dec(99))
# print(from_hex("399"))

# ---------------------------------------
# |    UID    | Snsr |   Data    | Cntr |
# ---------------------------------------
# |         8 |    4 |         8 |    4 |
# | 0000_0001 | 0001 | 0001_1011 | 0001 |
# |        01 |    1 |        1B |    1 |
# ---------------------------------------
#
# -----------------
# | Sensor |  ID  |
# -----------------
# |   Temp | 0001 |
# |  Light | 0002 |
# |  Sonor | 0003 |
# -----------------

# Temp = Celcius Decimaal
# Light = Lux Decimaal
# Sonor = Afstand (Cm) Decimaal

temp  = "0111b1"
light = "012ab1"
sonor = "013ef1"

def interpreter(arg):
    uid = arg[0:2]
    sensor = arg[2]
    data = arg[3:5]
    counter = arg[5]

    map = {"1":"Celcius",
           "2":"Lux",
           "3":"Centimeter"}

    # Debug onzin:

    # print(from_hex(uid))
    print(str(from_hex(data)) + " " + map[sensor])
    # print(from_hex(counter))

interpreter(temp)
interpreter(light)
interpreter(sonor)

testClass = Protocol()
