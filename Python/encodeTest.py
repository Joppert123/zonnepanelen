test = "AAAAAA"

def ArduinoEncode(cmd):
    end = "\0"
    print((cmd + end).encode())
    return (cmd + end).encode()

ArduinoEncode(test)
#
#
#
#
# test = b'AAAAAA\0'
# print(test)
# print(test.decode())
# string = "AAAAAA"
# end = "\0"
# cmd = string + end
# print(cmd.encode())
