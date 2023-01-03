import threading
from threading import Lock
import time

mutex_read = Lock()
endLock = Lock()

def tester():
    now = 0
    while True:
        if mutex_read.acquire(blocking=False):
            print(now)
            now += 1
            mutex_read.release()
        time.sleep(1)
        if endLock.acquire(blocking=False):
            print("My line has ended!")
            return


if __name__ == "__main__":
    endLock.acquire()
    task = threading.Thread(target=tester)
    task.daemon = True
    task.start()
    time.sleep(2)
    mutex_read.acquire()
    print("stop")
    time.sleep(3)
    print("start")
    mutex_read.release()
    time.sleep(3)
    endLock.release()
    time.sleep(3)
    print("Im dead!")
