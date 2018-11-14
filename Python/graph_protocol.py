import time
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from connect import *
from protocol import *
from vraska import *

# Look, I don't want to use globals but for now I fear it is a necessary evil
thread_flag = None
previous_flag = None

# Temperature is data[0]
# Light       is data[1]
# Ultra Sonor is data[2]
data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


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


def Task1(ser):

    while True:
        global thread_flag
        global data

        while thread_flag != '1':
            time.sleep(0.001)

        while thread_flag == '1':
            command = "get_temp"
            # response = int(Transmit(ser, command).hex(), 16)
            response = int(Transmit(ser, command).hex(), 16)
            data[0].insert(0, response)
            data[0].pop()
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

        while thread_flag != '2':
            time.sleep(0.001)

        while thread_flag == '2':
            command = "get_light"
            # response = int(Transmit(ser, command).hex(), 16)
            response = int(Transmit(ser, command).hex(), 16)
            data[1].insert(0, response)
            data[1].pop()
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

        while thread_flag != '3':
            time.sleep(0.001)

        while thread_flag == '3':
            command = "get_sonar_distance"
            # response = int(Transmit(ser, command).hex(), 16)
            response = int(Transmit(ser, command).hex(), 16)
            data[2].insert(0, response)
            data[2].pop()
            thread_flag = '1'

        if thread_flag == 'stop':
            break
        # signals that the inner loop is done
        else:
            thread_flag = '1'
        time.sleep(1)


def Graph():
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    plt.axis([0, 10, 0, 200])

    def animate(i):
        global data
        xar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        yar = data[2]
        ax1.clear()
        ax1.plot(xar, yar)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.ylim([0, 3])
    plt.show()


def Main():
    Connect()
    try:
        ser = connections[0].ser
    except IndexError:
        return

    t1 = threading.Thread(target=Task1,
                          args=[ser],
                          daemon=True,
                          )
    t2 = threading.Thread(target=Task2,
                          args=[ser],
                          daemon=True,
                          )
    t3 = threading.Thread(target=Task3,
                          args=[ser],
                          daemon=True,
                          )

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    t3.start()
    time.sleep(1)

    Start()

    t4 = threading.Thread(target=Graph,
                          args=[],
                          daemon=True,
                          )
    t4.start()

    # Graph()

    # For debuging purposes:
    # time.sleep(1200)
    # Stop()
    # ser.close()
    while True:
        Report("Datasets:")
        Report(data[0])
        Report(data[1])
        Report(data[2])
        Report("\n")
        time.sleep(10)


if __name__ == '__main__':

    Main()
