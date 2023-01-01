from tkinter import *
import serial


def printSlide():
    serv1 = slide1.get()
    serv2 = slide2.get()
    serv3 = slide3.get()
    print('Slide 1 = ' + str(serv1))
    print('Slide 2 = ' + str(serv2))
    print('Slide 3 = ' + str(serv3))
    print(' ')
    comm_serial.write(serv1.to_bytes(1, 'big'))


view = Tk()
view.geometry('400x200')
view.title("Servo Control")

slide1 = Scale(view, from_=0, to=180, orient=HORIZONTAL, length=390, showvalue=FALSE)
slide2 = Scale(view, from_=0, to=180, orient=HORIZONTAL, length=390, showvalue=FALSE)
slide3 = Scale(view, from_=0, to=180, orient=HORIZONTAL, length=390, showvalue=FALSE)

butt1 = Button(view, text='Send data', command=printSlide)

label1 = Label(view, text='Servo 1')
label2 = Label(view, text='Servo 2')
label3 = Label(view, text='Servo 3')

label1.grid(row=1)
label2.grid(row=3)
label3.grid(row=5)

slide1.grid(row=2)
slide2.grid(row=4)
slide3.grid(row=6)

butt1.grid(row=7)

comm_serial = serial.Serial('COM4', 115200)

view.mainloop()