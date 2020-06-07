#########################################
#   JARVIS Main Control by Colby Pryor  #
#########################################
import speech_recognition as sr
from gtts import gTTS
import os
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("JARVIS is listening:")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    while(r.recognize_sphinx(audio) != "jarvis"):  
        with sr.Microphone() as source:
            print("JARVIS is listening:")
            audio = r.listen(source)
    else:
        introduction = "Hello Colby! What can I do for you?"
        texttoaud = gTTS(text=introduction, lang='en',  slow=False)
        texttoaud.save("intro.mp3")
        os.system("start /B intro.mp3")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


