#########################################
#   JARVIS Main Control by Colby Pryor  #
#########################################
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold = 1000
with sr.Microphone() as source:
    print("JARVIS is listening:")
    audio = r.listen(source)
    r.recognize_sphinx(audio)
# recognize speech using Sphinx
try:
    while(r.recognize_sphinx(audio) != "jarvis"):  
        with sr.Microphone() as source:
            print("JARVIS is listening:")
            audio = r.listen(source)
            print(r.recognize_sphinx(audio))
    else:
        def intro():
            import time
            introduction = "Hello Colby! What can I do for you?"
            texttoaud = gTTS(text=introduction, lang='en-us')
            texttoaud.save("intro.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("intro.mp3")
            pygame.mixer.music.play()
            with sr.Microphone() as source:
                print("JARVIS is listening:")
                time.sleep(2)
                audio = r.listen(source)
                print("JARVIS is listening:")
            if(r.recognize_sphinx(audio) == "weather"):
                print(r.recognize_sphinx(audio))
                print("hello")
            else:
                print(r.recognize_sphinx(audio))
                print("hi")
        intro()
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


