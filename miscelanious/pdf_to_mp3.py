import PyPDF2
from gtts import gTTS

text_in = ' '
text = []
pdfreader = PyPDF2.PdfReader(open("dsp_book_Ch19.pdf", 'rb'))
for page in range(len(pdfreader.pages)):
    text.append(pdfreader.pages[page].extract_text())
    text[-1].strip().replace('&', '-')
    print(text[-1])
    text_in += text[-1].strip().replace('\n', ' ')
language = 'en'
speaker = gTTS(text=text_in, lang=language, slow=False)
speaker.save("output_data_speach.mp3")