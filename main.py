from gtts import gTTS
import os

myText = input("enter text you want to listen:")   

language = "en"

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")