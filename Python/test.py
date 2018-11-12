import serial, time

ser = serial.Serial("COM3", 19200, timeout=None)

print("Start")
i = 0
while ser.isOpen():
    if ser.read(6) == (b'ping\r\n'):
        print(ser.name + " verbonden")
        i = i + 1
        if i == 3:
            ser.close()
print("Fin")
print(ser.readline())
