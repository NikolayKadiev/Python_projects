import tkinter as tk
from tkinter import filedialog
import serial
import serial.tools.list_ports
import threading

startLock = threading.Lock()
comm_serial = 0
y_in = []
specs = [0x1A, 0x18, 0x03, 0x16, 0X13, 0x01, 0x1B, 0x5B, 0x41, 0x1B, 0x5B, 0x42]


def openPort():
    global comm_serial
    comm_serial = serial.Serial(com_avail.get(), com_baud.get())
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
    kaor = str(text_out.get()) + '\n'
    comm_serial.write(kaor.encode())
    text_out.delete(0, tk.END)


def specPress(value):
    global comm_serial, specs
    if (value == 6) | (value == 9):
        comm_serial.write(specs[value].to_bytes(length=1, byteorder='little'))
        comm_serial.write(specs[value+1].to_bytes(length=1, byteorder='little'))
        comm_serial.write(specs[value+2].to_bytes(length=1, byteorder='little'))
    else:
        comm_serial.write(specs[value].to_bytes(length=1, byteorder='little'))


def clrBox():
    text_in.delete(1.0, tk.END)


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
    view.geometry('407x326')
    view.title("Serial IO")

    com_avail = tk.StringVar()
    com_avail.set(comms[0])
    drop = tk.OptionMenu(view, com_avail, *comms)
    butt3 = tk.Button(view, text='Open Port', command=openPort)
    drop.grid(row=1)
    butt3.grid(row=2)
    options = [4800, 9600, 115200, 921600]
    com_baud = tk.IntVar()
    com_baud.set(options[1])
    baud_drop = tk.OptionMenu(view, com_baud, *options)
    baud_drop.grid(column=1, row=1)

    butt_clr = tk.Button(view, text='Clear text', command=clrBox)
    butt_clr.grid(column=1, row=2)

    label1 = tk.Label(view, text='Open file')
    butt1 = tk.Button(view, text='Choose file', command=readFile)
    label1.grid(column=2, row=1)
    butt1.grid(column=2, row=2)

    label2 = tk.Label(view, text='Send file')
    butt2 = tk.Button(view, text='Send', command=sendFile)
    label2.grid(column=3, row=1)
    butt2.grid(column=3, row=2)

    text_out = tk.Entry(view, width=50)
    text_out.grid(column=0, row=5, columnspan=4)
    text_out.bind('<Return>', onKeyPress)

    text_in = tk.Text(view, height=10, width=50)
    text_in.grid(column=0, row=6, columnspan=4)

    sbutt1 = tk.Button(view, text='Ctrl+Z', command=lambda: specPress(0))
    sbutt1.grid(column=0, row=3)
    sbutt2 = tk.Button(view, text='Ctrl+X', command=lambda: specPress(1))
    sbutt2.grid(column=1, row=3)
    sbutt3 = tk.Button(view, text='Ctrl+C', command=lambda: specPress(2))
    sbutt3.grid(column=2, row=3)
    sbutt4 = tk.Button(view, text='Ctrl+V', command=lambda: specPress(3))
    sbutt4.grid(column=3, row=3)
    sbutt5 = tk.Button(view, text='Ctrl+S', command=lambda: specPress(4))
    sbutt5.grid(column=0, row=4)
    sbutt6 = tk.Button(view, text='Ctrl+A', command=lambda: specPress(5))
    sbutt6.grid(column=1, row=4)
    sbutt7 = tk.Button(view, text='UP', command=lambda: specPress(6))
    sbutt7.grid(column=2, row=4)
    sbutt8 = tk.Button(view, text='DOWN', command=lambda: specPress(9))
    sbutt8.grid(column=3, row=4)

    view.mainloop()
