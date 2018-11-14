import time
import threading

from connect import *
from protocol import *

# Look, I don't want to use globals but for now I fear it is a necessary evil
thread_flag = None
data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def Stop():
    global thread_flag
    thread_flag = 'stop'


def Start():
    global thread_flag
    thread_flag = '1'


def Task1(ser):

    while True:
        global thread_flag
        global data

        Report("Temperature waiting for permission to read")
        while thread_flag != '1':
            time.sleep(0.001)

        while thread_flag == '1':
            Report("Temperature is reading")
            command = "get_temp"
            response = int(Transmit(ser, command).hex(), 16)
            data[0].insert(0, response)
            data[0].pop()
            Report(data[0])
            thread_flag = '2'

        if thread_flag == 'stop':
            break
        # signals that the inner loop is done
        else:
            thread_flag = '2'
        time.sleep(1)


def Task2(ser):

    while True:
        global thread_flag
        global data

        Report("Yagami Light is waiting for permission to read")
        while thread_flag != '2':
            time.sleep(0.001)

        while thread_flag == '2':
            Report("Yagami Light is reading")
            command = "get_light"
            response = int(Transmit(ser, command).hex(), 16)
            data[1].insert(0, response)
            data[1].pop()
            Report(data[1])
            thread_flag = '3'

        if thread_flag == 'stop':
            break
        # signals that the inner loop is done
        else:
            thread_flag = '3'
        time.sleep(1)


def Task3(ser):

    while True:
        global thread_flag
        global data

        Report("Ultra Sonor is waiting for permission to read")
        while thread_flag != '3':
            time.sleep(0.001)

        while thread_flag == '3':
            Report("Ultra Sonor is reading")
            command = "get_sonar_distance"
            # response = int(Transmit(ser, command).hex(), 16)
            response = "test"
            data[2].insert(0, response)
            data[2].pop()
            Report(data[2])
            thread_flag = '1'

        if thread_flag == 'stop':
            break
        # signals that the inner loop is done
        else:
            thread_flag = '1'
        time.sleep(1)


def Main():
    Connect()
    try:
        ser = connections[0].ser
    except IndexError:
        return

    t1 = threading.Thread(target=Task1, args=[ser], daemon=True)
    t2 = threading.Thread(target=Task2, args=[ser], daemon=True)
    t3 = threading.Thread(target=Task3, args=[ser], daemon=True)

    Report("Starting Temperature")
    t1.start()
    time.sleep(1)
    Report("Starting Yagami Light")
    t2.start()
    time.sleep(1)
    Report("Starting Ultra Sonor")
    t3.start()
    time.sleep(1)

    Start()

    # For debuging purposes:
    time.sleep(120)
    Stop()
    ser.close()


if __name__ == '__main__':

    Main()
