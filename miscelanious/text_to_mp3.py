
from gtts import gTTS

text_in = ' '
file = open('data_in.txt', "r")
lines = file.readlines()
for x in lines:
    text_in += x.strip().replace('\n', ' ')
file.close()
language = 'en'
speaker = gTTS(text=text_in, lang=language, slow=False)
speaker.save("data_speach.mp3")
