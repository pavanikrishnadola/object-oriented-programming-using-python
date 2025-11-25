import tkinter as tk
from gtts import gTTS
import os
from playsound import playsound
def text_to_audio():
    text = entry.get()
    if text.strip():
        tts = gTTS(text=text, lang='en')
        audio_file = "temp_audio.mp3"
        tts.save(audio_file)
        playsound(audio_file)
        entry.delete(0, 'end')
        os.remove(audio_file)
root = tk.Tk()
root.title("Text to Audio")
label = tk.Label(root, text="Enter text:")
label.pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
button = tk.Button(root, text="Convert To Audio", command=text_to_audio)
button.pack(pady=10)
root.mainloop()
