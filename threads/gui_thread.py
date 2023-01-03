import threading
from threading import Lock
from tkinter import *
import time

mutex_read = Lock()
endLock = Lock()

lok_in = 0


def prgStop():
    global lok_in
    if lok_in == 0:
        mutex_read.acquire()
        print("STOP")
        lok_in = 1
    else:
        mutex_read.release()
        lok_in = 0
        print("GO")


def prgKill():
    endLock.release()


def tester():
    now = 0
    while True:
        if mutex_read.acquire(blocking=False):
            print(now)
            now += 1
            mutex_read.release()
        time.sleep(1)
        print('___')
        if endLock.acquire(blocking=False):
            print("My line has ended!")
            return


if __name__ == "__main__":
    endLock.acquire()
    task = threading.Thread(target=tester)
    task.daemon = True
    task.start()

    view = Tk()
    view.geometry('400x400')
    view.title("My GUI")

    printButt = Button(view, text='Pause', command=prgStop)
    printButt.grid(row=2)
    quitButt = Button(view, text='Quit', command=prgKill)
    quitButt.grid(row=2, column=1)

    view.mainloop()
