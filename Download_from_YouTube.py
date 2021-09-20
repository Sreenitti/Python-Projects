from gtts import gTTS
import os
from tkinter import *

def textToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")

root = Tk()
root.title("Text To Speech Convertor")

canvas = Canvas(root, width=400, height=300)
canvas.pack()

label = Label(root, text="Enter text ")
canvas.create_window(200, 150, window=label)

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Convert", command=textToSpeech)
canvas.create_window(200, 230, window=button)

root.mainloop()