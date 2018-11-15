import time
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from connect import *
from protocol import *

# Look, I don't want to use globals but for now I fear it is a necessary evil
thread_flag = None
previous_flag = None


def Stop():
    global thread_flag
    thread_flag = 'stop'


def Start():
    global thread_flag
    thread_flag = '1'


def UserFlag():
    global thread_flag
    global previous_flag
    previous_flag = thread_flag.copy()
    thread_flag = 'gui'


def SetPreviousFlag():
    global thread_flag
    global previous_flag
    map = {'1': '2',
           '2': '3',
           '3': '1'}
    thread_flag = map[previous_flag]


def Task1(connection):
    ser = connection.ser
    while True:
        global thread_flag
        global data

        while thread_flag != '1':
            time.sleep(0.001)

        while thread_flag == '1':
            command = "get_temp"
            # response = int(Transmit(ser, command).hex(), 16)
            response = int(Transmit(ser, command).hex(), 16)
            connection.data[0].insert(0, response)
            connection.data[0].pop()
            Report(connection.data)
            thread_flag = '2'

        if thread_flag == 'stop':
            break
        elif thread_flag == 'gui':
            time.sleep(3)
        else:
            thread_flag = '2'
        time.sleep(1)


def Task2(connection):
    ser = connection.ser
    while True:
        global thread_flag
        global data

        while thread_flag != '2':
            time.sleep(0.001)

        while thread_flag == '2':
            command = "get_light"
            # response = int(Transmit(ser, command).hex(), 16)
            response = int(Transmit(ser, command).hex(), 16)
            connection.data[1].insert(0, response)
            connection.data[1].pop()
            thread_flag = '3'

        if thread_flag == 'stop':
            break
        elif thread_flag == 'gui':
            time.sleep(3)
        else:
            thread_flag = '3'
        time.sleep(1)


def Task3(connection):
    ser = connection.ser
    while True:
        global thread_flag
        global data

        while thread_flag != '3':
            time.sleep(0.001)

        while thread_flag == '3':
            command = "get_sonar_distance"
            # response = int(Transmit(ser, command).hex(), 16)
            response = int(Transmit(ser, command).hex(), 16)
            connection.data[2].insert(0, response)
            connection.data[2].pop()
            thread_flag = '1'

        if thread_flag == 'stop':
            break
        elif thread_flag == 'gui':
            time.sleep(3)
        else:
            thread_flag = '1'
        time.sleep(1)


def Graph(connection):
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    plt.axis([0, 10, 0, 200])

    def animate(i):
        global data
        xar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        yar = connection.data[2]
        ax1.clear()
        ax1.plot(xar, yar)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.ylim([0, 3])
    plt.show()


def Main():
    Connect()
    # If no devices connected stop
    try:
        connection = connections[0]
    except IndexError:
        return

    t1 = threading.Thread(target=Task1,
                          args=[connection],
                          daemon=True,
                          )
    t2 = threading.Thread(target=Task2,
                          args=[connection],
                          daemon=True,
                          )
    t3 = threading.Thread(target=Task3,
                          args=[connection],
                          daemon=True,
                          )
    t4 = threading.Thread(target=Graph,
                          args=[connection],
                          daemon=True,
                          )

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    t3.start()
    time.sleep(1)
    # Set thread_flag to start plotting
    Start()
    # Open graph in new thread
    # t4.start()

    # For debuging purposes:
    debug = 0
    if debug == 1:
        while True:
            Report("Datasets:")
            Report(connection.data)
            time.sleep(10)


# if __name__ == '__main__':
#
#     Main()
