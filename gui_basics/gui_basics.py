from tkinter import *
import tkinter.messagebox

def printAll():
    print(new_text.get(1.0, END))
    statusBar.config(text='Print text box')


def printButt(var):
    statusBar.config(text=var + ' was pressed')
    new_text.insert(END, var + ' was pressed' + '\n')


def printSlide():
    val = slide1.get()
    new_text.insert(END, str(val) + '\n')
    statusBar.config(text='Slider was printed')


def chng(vr):
    radioLabel.config(text=vr)
    statusBar.config(text='Radio button was pressed')


def inpPrint():
    stri = ent.get()
    new_text.insert(END, str(droping.get()) + '\t' + stri + '\n')
    if var.get() == TRUE:
        ent.delete(0, END)
    statusBar.config(text='Input field was printed')


view = Tk()
view.geometry('400x400')
view.title("My GUI")

# make a message box
tkinter.messagebox.showinfo('Hello', "Hello there")
answer = tkinter.messagebox.askquestion("Q1", "Do you know da way?")
if answer == 'yes':
    print(';-)')

# make a menu bar
menu1 = Menu(view)
view.config(menu=menu1)
subMenu = Menu(menu1)
menu1.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Print', command=printAll)
subMenu.add_separator()
subMenu.add_command(label='quit', command=view.quit)

# make a toolbar -> frame and button
toolbar = Frame(view, bg="blue")
insertButton = Button(toolbar, text='Insert button', command=lambda: printButt('Insert button'))
insertButton.pack(side=LEFT, padx=2, pady=2)
pulButton = Button(toolbar, text='Play button', command=lambda: printButt('Play button'))
pulButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# make a statusbar -> label
statusBar = Label(view, text='Ready...', bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

# make slider
slide1 = Scale(view, from_=0, to=400, orient=HORIZONTAL, length=390)
slide1.pack()
sliderButt = Button(view, text='Print me', command=printSlide)
sliderButt.pack()

#  make text box
new_text = Text(view, width=40, height=5)
new_text.pack()

# make radio buttons
var1 = IntVar()
Radiobutton(view, text='option 1', variable=var1, value=1, command=lambda: chng(var1.get())).pack()
Radiobutton(view, text='option 2', variable=var1, value=2, command=lambda: chng(var1.get())).pack()
radioLabel = Label(view, text=var1.get())
radioLabel.pack()

#  make entry and check button
ent = Entry(view, width=50)
butt = Button(view, text='Enter me: ', command=inpPrint)
var = IntVar()
chk = Checkbutton(view, text="Delete entry?", variable=var)
droping = IntVar()
# drop = OptionMenu(view, droping, 0, 1, 2, 3, 4, 5, 6, 7)
options = [0, 1, 2, 3, 4, 5, 6, 7]
drop = OptionMenu(view, droping, *options)
ent.pack()
butt.pack()
chk.pack()
drop.pack()

view.mainloop()