from gtts import gTTS

import  os

f=open("tts.txt")
x=f.read()

language='eng'

audio=gTTS(text=x,lang=language,slow=True)

audio.save("tts.wav")
os.system("tts.wav")
