import tkinter as tk
from tkinter import filedialog
import serial
import serial.tools.list_ports
import threading

startLock = threading.Lock()
comm_serial = 0
y_in = []


def openPort():
    global comm_serial
    comm_serial = serial.Serial(com_avail.get(), 115200)
    startLock.release()


def readFile():
    global y_in
    name = filedialog.askopenfilename(title='Open Text File',)
    txt_file = open(name, 'r')
    content = txt_file.readlines()
    y_in.clear()
    for x in content:
        y_in.append(str(x))
    txt_file.close()


def sendFile():
    global comm_serial, y_in
    for i in range(y_in.__len__()):
        comm_serial.write(y_in[i].encode())
    y_in.clear()


def onKeyPress(event):
    global comm_serial
    kaor = str(text_out.get(1.0, tk.END))[:-1]
    comm_serial.write(kaor.encode())
    text_out.delete(1.0, tk.END)


def inCom():
    startLock.acquire(blocking=True)
    while True:
        while comm_serial.inWaiting() == 0:
            pass
        while comm_serial.inWaiting() > 0:
            line_in = comm_serial.readline()
        text_in.insert(tk.END, line_in)


if __name__ == "__main__":
    comms = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        comms.append(port)

    startLock.acquire()
    task = threading.Thread(target=inCom)
    task.daemon = True
    task.start()

    view = tk.Tk()
    view.geometry('407x264')
    view.title("Serial IO")

    label1 = tk.Label(view, text='Open file')
    butt1 = tk.Button(view, text='Choose file', command=readFile)
    label1.grid(row=1)
    butt1.grid(row=2)

    label2 = tk.Label(view, text='Send file')
    butt2 = tk.Button(view, text='Send', command=sendFile)
    label2.grid(column=2, row=1)
    butt2.grid(column=2, row=2)

    com_avail = tk.StringVar()
    com_avail.set(comms[0])
    drop = tk.OptionMenu(view, com_avail, *comms)
    butt3 = tk.Button(view, text='Open Port', command=openPort)
    drop.grid(column=3, row=1)
    butt3.grid(column=3, row=2)

    text_out = tk.Text(view, height=1, width=50)
    text_out.grid(column=0, row=3, columnspan=4)
    text_out.bind('<Return>', onKeyPress)

    text_in = tk.Text(view, height=10, width=50)
    text_in.grid(column=0, row=4, columnspan=4)

    view.mainloop()
