def to_bin(dec):
    if dec == 0:
        return '0'
    return to_bin(dec // 2) + str(dec % 2)

def to_hex(dec):
    if dec == 0:
        return '0'
    return to_hex(dec // 16) + "0123456789ABCDEF"[dec % 16]

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
           "A": 10,
           "B": 11,
           "C": 12,
           "D": 13,
           "E": 14,
           "F": 15}
    return 16 * from_hex(hex[:-1]) + map[hex[-1]]
