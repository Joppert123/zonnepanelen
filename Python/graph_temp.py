from connect import *
from protocol import *
from graph_protocol import *


def Graph(connection, sensor):
    map = {
        "temp": 0,
        "light": 1,
        "sonor": 2,
    }

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    plt.axis([0, 10, 0, 200])

    def animate(i):
        xar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        yar = connection.data[map[sensor]]
        ax1.clear()
        ax1.plot(xar, yar)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.ylim([0, 3])
    plt.show()


try:
    connection = connections[0]
except IndexError:
    Connect()
    try:
        connection = connections[0]
    except IndexError:
        print("Index Error")

Main()

Graph(connection, "temp")
