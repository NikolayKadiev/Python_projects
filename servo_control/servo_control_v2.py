
from tkinter import *
import serial
import serial.tools.list_ports

servo_start_pos = 515
servo_end_pos = 2048
comm_serial = 0

def openPort():
    global comm_serial
    comm_serial = serial.Serial(com_avail.get(), 115200)


def chan_slide(var):
    srv_ctrl = []
    servo = 0
    if var == 1:
        srv_ctrl.append(0x01)
        servo = slide1.get()
        srv_ctrl.append(servo >> 8)
        srv_ctrl.append(servo & 0xFF)
        comm_serial.write(srv_ctrl)
    if var == 2:
        srv_ctrl.append(0x02)
        servo = slide2.get()
        srv_ctrl.append(servo >> 8)
        srv_ctrl.append(servo & 0xFF)
        comm_serial.write(srv_ctrl)
    if var == 3:
        srv_ctrl.append(0x03)
        servo = slide3.get()
        srv_ctrl.append(servo >> 8)
        srv_ctrl.append(servo & 0xFF)
        comm_serial.write(srv_ctrl)
    if var == 4:
        srv_ctrl.append(0x04)
        servo = slide4.get()
        srv_ctrl.append(servo >> 8)
        srv_ctrl.append(servo & 0xFF)
        comm_serial.write(srv_ctrl)


if __name__ == "__main__":
    comms = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        comms.append(port)

    view = Tk()
    view.geometry('502x280')
    view.title("Servo Control")

    slide1 = Scale(view, from_=servo_start_pos, to=servo_end_pos, orient=HORIZONTAL, length=390, showvalue=FALSE)
    slide2 = Scale(view, from_=servo_start_pos, to=servo_end_pos, orient=HORIZONTAL, length=390, showvalue=FALSE)
    slide3 = Scale(view, from_=servo_start_pos, to=servo_end_pos, orient=HORIZONTAL, length=390, showvalue=FALSE)
    slide4 = Scale(view, from_=servo_start_pos, to=servo_end_pos, orient=HORIZONTAL, length=390, showvalue=FALSE)

    butt0 = Button(view, text='Open Port', command=openPort)
    butt1 = Button(view, text='Send chan 1', command=lambda: chan_slide(1))
    butt2 = Button(view, text='Send chan 2', command=lambda: chan_slide(2))
    butt3 = Button(view, text='Send chan 3', command=lambda: chan_slide(3))
    butt4 = Button(view, text='Send chan 4', command=lambda: chan_slide(4))

    label1 = Label(view, text='Servo 1')
    label2 = Label(view, text='Servo 2')
    label3 = Label(view, text='Servo 3')
    label4 = Label(view, text='Servo 4')

    com_avail = StringVar()
    drop = OptionMenu(view, com_avail, *comms)
    drop.grid(row=1)

    butt0.grid(row=2)

    label1.grid(row=3)
    label2.grid(row=5)
    label3.grid(row=7)
    label4.grid(row=9)

    slide1.grid(row=4)
    slide2.grid(row=6)
    slide3.grid(row=8)
    slide4.grid(row=10)

    butt1.grid(column=1, row=4)
    butt2.grid(column=1, row=6)
    butt3.grid(column=1, row=8)
    butt4.grid(column=1, row=10)

    view.mainloop()
    comm_serial.close()
