import threading, time

from protocol import *
from connect import *

plot = []

def GetTempForPlot(command, refresh, y):
    for i in range(y):
        plot.append(0)

    try:
        ser = connections[0].ser
    except IndexError:
        print("Kan niet")

    while 1:
        temp = int(Transmit(ser, command).hex(), 16)
        plot.insert(0, temp)
        plot.pop(len(plot)-1)
        time.sleep(refresh)


def PrintPlot(refresh):
    pastPlot = []
    while 1:
        if plot == pastPlot:
            pass
        else:
            pastPlot = plot.copy()
            print(plot)
        time.sleep(refresh)


Connect()

y = 10
refresh = 1
command = "get_temp"

t1 = threading.Thread(target = GetTempForPlot, args=[command, refresh, y])
t2 = threading.Thread(target = PrintPlot, args=[refresh])
t1.start()
t2.start()
