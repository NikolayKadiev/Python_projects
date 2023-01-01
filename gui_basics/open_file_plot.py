from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
fig.subplots_adjust(bottom=0.1, left=0.1)

y1 = []


def readFile():
    global y1
    y1.clear()
    name = filedialog.askopenfilename(title='Open Text File', filetypes=(("Text Files", "*.txt"),))
    txt_file = open(name, 'r')
    content = txt_file.readlines()
    for x in content:
        y1.append(float(x.split('\t\t')[1]))
    txt_file.close()



def plotFile():
    plt.cla()
    ax.plot(y1)
    ax.set_xlabel('time [ms]')
    ax.set_ylabel('ECG')
    plt.grid()
    plt.show()


view = Tk()
view.geometry('200x100')
view.title("File open and plot")


butt1 = Button(view, text='read', command=readFile)
butt2 = Button(view, text='plot', command=plotFile)

label1 = Label(view, text='Read a file')
label2 = Label(view, text='Plot the file')

label1.grid(row=1)
label2.grid(row=1, column=2)

butt1.grid(row=2)
butt2.grid(row=2, column=2)

view.mainloop()