
from pytube import YouTube
from moviepy.editor import *

if __name__ == "__main__":
    file = open('conv_links.txt', "r")
    lines = file.readlines()
    file.close()
    for x in lines:
        link = str(x)
        try:
            ytObj = YouTube(link)
            print(ytObj.title)
            new_name = ytObj.title
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
    print("ALL done")
