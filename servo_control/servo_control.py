from tkinter import *
import serial

comm_serial = 0


def openPort():
    global comm_serial
    comm_serial = serial.Serial(portEntry.get(), 115200)


def printSlide():
    serv1 = slide1.get()
    serv2 = slide2.get()
    serv3 = slide3.get()
    print('Slide 1 = ' + str(serv1))
    print('Slide 2 = ' + str(serv2))
    print('Slide 3 = ' + str(serv3))
    print(' ')
    comm_serial.write(b's')
    comm_serial.write((serv1 >> 8).to_bytes(1, 'little'))
    comm_serial.write((serv1 & 0xff).to_bytes(1, 'little'))
    comm_serial.write((serv2 >> 8).to_bytes(1, 'little'))
    comm_serial.write((serv2 & 0xff).to_bytes(1, 'little'))
    comm_serial.write((serv3 >> 8).to_bytes(1, 'little'))
    comm_serial.write((serv3 & 0xff).to_bytes(1, 'little'))


if __name__ == "__main__":
    view = Tk()
    view.geometry('400x220')
    view.title("Servo Control")

    slide1 = Scale(view, from_=1000, to=4800, orient=HORIZONTAL, length=390, showvalue=FALSE)
    slide2 = Scale(view, from_=1000, to=4758, orient=HORIZONTAL, length=390, showvalue=FALSE)
    slide3 = Scale(view, from_=1000, to=4758, orient=HORIZONTAL, length=390, showvalue=FALSE)

    butt1 = Button(view, text='Send data', command=printSlide)
    butt2 = Button(view, text='Open Port', command=openPort)

    label1 = Label(view, text='Servo 1')
    label2 = Label(view, text='Servo 2')
    label3 = Label(view, text='Servo 3')
    portEntry = Entry(view, width=20)

    portEntry.grid(row=1)
    butt2.grid(row=2)

    label1.grid(row=3)
    label2.grid(row=5)
    label3.grid(row=7)

    slide1.grid(row=4)
    slide2.grid(row=6)
    slide3.grid(row=8)

    butt1.grid(row=9)

    view.mainloop()
    comm_serial.close()
