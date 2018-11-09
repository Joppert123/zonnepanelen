import serial

ser = serial.Serial("COM3", 19200, timeout=2)
write = ser.write(b'ping/0')
write
read = ser.readline()
read

# test = ser.read(100)
# test
