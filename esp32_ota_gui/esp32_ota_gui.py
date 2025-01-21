
import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import filedialog
import time

Pserial = 0
file_types = [('All Files', '*.*'),
              ('Text Document', '*.txt')]


def openPort():
    global Pserial
    Pserial = serial.Serial(com_avail.get(), 115200, timeout=3)
    Pserial.flushInput()
    Pserial.flush()
    conn_label.config(text= 'Connected to ' + str(com_avail.get()), fg='green')


def read_file_app():
    name = filedialog.askopenfilename(filetypes=file_types)
    file = open(name, 'rb')
    data_in = file.read()
    file.close()
    data_in_len = data_in.__len__()
    data_out_len = 0
    data_step_len = 1000
    otu_ge = [0x4E, 0x41, 0x56, 0x00, 0x00, 0x00, 0x00]
    otu_ge[3] = (data_in_len >> 24) & 0xFF
    otu_ge[4] = (data_in_len >> 16) & 0xFF
    otu_ge[5] = (data_in_len >> 8) & 0xFF
    otu_ge[6] = data_in_len & 0xFF
    print('App len: ' + str(data_in_len))
    Pserial.write(otu_ge)
    print(str(Pserial.readline()))
    time.sleep(2)
    while True:
        if data_in_len - data_out_len > data_step_len:
            Pserial.write(data_in[data_out_len:(data_out_len+data_step_len)])
            print(str(Pserial.readline()) + '\t' + str(data_out_len+data_step_len))
        else:
            Pserial.write(data_in[data_out_len:])
            print(str(Pserial.readline()))
            break
        data_out_len += data_step_len


if __name__ == "__main__":
    comm_port = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        comm_port.append(port)

    if comm_port.__len__() == 0:
        comm_port.append('XXX')

    view = tk.Tk()
    view.geometry('250x100')

    label0 = tk.Label(view, text='--- Port ---')
    label0.grid(row=0, column=0, columnspan=3)
    butt0 = tk.Button(view, text='Open Port', command=openPort)
    butt0.grid(row=1, column=0)
    com_avail = tk.StringVar()
    com_avail.set(comm_port[0])
    drop = tk.OptionMenu(view, com_avail, *comm_port)
    drop.grid(row=1, column=2)
    conn_label = tk.Label(view, text='No connection!', fg='red')
    conn_label.grid(row=2, column=0, columnspan=3)

    butt1 = tk.Button(view, text='Select file', command=read_file_app)
    butt1.grid(row=1, column=3)

    view.mainloop()