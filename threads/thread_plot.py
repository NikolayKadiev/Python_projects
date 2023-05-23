
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dataLock = threading.Lock()

fig = plt.figure(figsize=(20, 5))
fig.subplots_adjust(bottom=0.1, left=0.1)
ax = plt.subplot()

data_out = []
data = [10, 10, 25, 50, 50, 150, 50, 50, 25, 10, 10]


def data_write():
    while True:
        for i in range(data.__len__()):
            time.sleep(1)
            if dataLock.acquire():
                data_out.append(data[i])
            dataLock.release()


def plot_func(set_mod=0):
    global data_out
    inp = []
    if dataLock.acquire(blocking=False):
        inp = data_out.copy()
        dataLock.release()
    ax.clear()
    ax.plot(inp)
    ax.grid()
    inp.clear()


if __name__ == "__main__":
    dataLock.acquire()

    task = threading.Thread(target=data_write)
    task.daemon = True
    task.start()

    ani = FuncAnimation(fig, plot_func, fargs=0, interval=500, cache_frame_data=False)
    dataLock.release()
    plt.show()

    exit(0)
