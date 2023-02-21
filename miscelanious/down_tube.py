from tkinter import *
from pytube import YouTube
from moviepy.editor import *
import os

def do_it():
    link = name.get()
    ytObj = YouTube(link)
    print(ytObj.title)
    new_name = ytObj.title
    try:
        print("Download started!")
        ytObj.streams.get_audio_only().download(filename=new_name+'.mp4')
        print("Downloaded!\nConversion start...")
        new_file = AudioFileClip(new_name+'.mp4')
        new_file.write_audiofile(new_name+'.mp3')
        new_file.close()
        os.remove(new_name+'.mp4')
        print("Done!")
    except:
        print('Video not found!')

view = Tk()
view.geometry('350x50')
view.title("YouTube MP3")

butt1 = Button(view, text='Download', command=do_it)
name = Entry(view, width=30)
name.grid(row=0,)
butt1.grid(row=0,column=1)

view.mainloop()
