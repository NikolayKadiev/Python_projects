import serial
import serial.tools.list_ports
import time
import threading
from tkinter import *

dataLock1 = threading.Lock()
dataLock2 = threading.Lock()
endLock1 = threading.Lock()
endLock2 = threading.Lock()

Server_serial = 0
Client_serial = 0


def server_task():
    out_data = "   "
    inp_data = "   "
    num = 0
    while True:
        if dataLock1.acquire(blocking=False):
            dataLock1.release()
            try:
                time.sleep(0.5)
                out_data = str("Server send {number}\n".format(number=num))
                Server_serial.write(out_data.encode())
                num += 1
                while Server_serial.inWaiting() == 0:
                    pass
                inp_data = str(Server_serial.readline())
                new_text.insert(1.0, "Server: " + inp_data[2:-3] + '\n')
                if num == 2500:
                    num = 0
            except:
                num = 0
                pass
        if endLock1.acquire(blocking=False):
            time.sleep(0.1)
            return


def client_task():
    out_data = "   "
    inp_data = "   "
    num = 0
    while True:
        if dataLock2.acquire(blocking=False):
            dataLock2.release()
            try:
                while Client_serial.inWaiting() == 0:
                    pass
                inp_data = str(Client_serial.readline())
                new_text.insert(1.0, "Client: " + inp_data[2:-3] + '\n')
                time.sleep(0.5)
                out_data = str("Client send {}\n".format(num))
                Client_serial.write(out_data.encode())
                num += 2
                if num == 2500:
                    num = 0
            except:
                num = 0
                pass
        if endLock2.acquire(blocking=False):
            time.sleep(0.1)
            return


def start_meas():
    global Server_serial, Client_serial
    startButt.config(background='tomato')
    stopButt.config(background='light green')
    new_text.delete(1.0, "end")
    Server_serial = serial.Serial(server_com.get(), 115200)
    Client_serial = serial.Serial(client_com.get(), 115200)
    dataLock1.release()
    dataLock2.release()
    return


def stop_meas():
    global Server_serial, Client_serial
    dataLock1.acquire()
    dataLock2.acquire()
    stopButt.config(background='tomato')
    startButt.config(background='light green')
    Server_serial.close()
    Client_serial.close()


if __name__ == "__main__":
    dataLock1.acquire()
    dataLock2.acquire()
    endLock1.acquire()
    endLock2.acquire()

    comms = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        comms.append(port)

    view = Tk()
    view.geometry('470x150')
    view.title("Data Queue")

    serverLabel = Label(view, text="Server Port")
    serverLabel.grid(row=0, column=3)
    clientLabel = Label(view, text="Client Port")
    clientLabel.grid(row=0, column=4)

    server_com = StringVar()
    client_com  = StringVar()
    drop_data = OptionMenu(view, server_com, *comms)
    server_com.set(comms[0])
    drop_command = OptionMenu(view, client_com, *comms)
    client_com.set(comms[1])
    drop_data.grid(row=1, column=3)
    drop_command.grid(row=1, column=4)

    startLabel= Label(view, text="Start")
    startLabel.grid(row=3, column=3)
    startButt = Button(view, text='Start', command=start_meas, background='light green')
    startButt.grid(row=4, column=3)
    stopLabel= Label(view, text="Stop")
    stopLabel.grid(row=3, column=4)
    stopButt = Button(view, text='Stop', command=stop_meas, background='tomato')
    stopButt.grid(row=4, column=4)

    new_text = Text(view, width=25, height=8)
    new_text.grid(row=0, column=0, columnspan=3, rowspan=6)

    task1 = threading.Thread(target=server_task)
    task1.daemon = True
    task1.start()
    task2 = threading.Thread(target=client_task)
    task2.daemon = True
    task2.start()

    view.mainloop()
    endLock1.release()
    endLock2.release()
    time.sleep(0.5)
    exit(0)
