#########################################
#   JARVIS Main Control by Colby Pryor  #
#########################################
import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import os
#lists to recognize commands
light_list = ['lights','light','the light','on','ah']
# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold = 1000
with sr.Microphone() as source:
    print("JARVIS is listening:")
    audio = r.listen(source)
    r.recognize_sphinx(audio)
# recognize speech using Sphinx
try:
    while(r.recognize_sphinx(audio) != "quit"): 
        while(r.recognize_sphinx(audio) == "jarvis"):  
            with sr.Microphone() as source:
                print("JARVIS is listening:")
                audio = r.listen(source)
                print(r.recognize_sphinx(audio))
                r.energy_threshold = 1000
                speakwords = "Hello Colby! What can I do for you?"
                texttoaud = gTTS(text=speakwords, lang='en-us')
                texttoaud.save("speakwords1.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("speakwords1.mp3")
                pygame.mixer.music.play()
                time.sleep(float(2.3))
                pygame.mixer.music.load("beep_tone.mp3")
                pygame.mixer.music.play()
                with sr.Microphone() as source:
                    time.sleep(2)
                    print("JARVIS is listening:")
                    audio = r.listen(source)
            if(r.recognize_sphinx(audio) in light_list):
                r.energy_threshold = 1000
                speakwords = "Would you like them on or off?"
                texttoaud = gTTS(text=speakwords, lang='en-us')
                texttoaud.save("speakwords3.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("speakwords3.mp3")
                pygame.mixer.music.play()
                time.sleep(float(2.3))
                pygame.mixer.music.load("beep_tone.mp3")
                pygame.mixer.music.play()
                with sr.Microphone() as source:
                    time.sleep(2)
                    print("JARVIS is listening:")
                    audio = r.listen(source)
                if(r.recognize_sphinx(audio) in light_list):
                    r.energy_threshold = 1000
                    speakwords = "Turning on the light"
                    texttoaud = gTTS(text=speakwords, lang='en-us')
                    texttoaud.save("speakwords3.mp3")
                    pygame.mixer.init()
                    pygame.mixer.music.load("speakwords3.mp3")
                    pygame.mixer.music.play()
                elif(r.recognize_sphinx(audio) == "off"):
                    r.energy_threshold = 1000
                    speakwords = "Turning on the light"
                    texttoaud = gTTS(text=speakwords, lang='en-us')
                    texttoaud.save("speakwords4.mp3")
                    pygame.mixer.init()
                    pygame.mixer.music.load("speakwords4.mp3")
                    pygame.mixer.music.play()
        else:
            with sr.Microphone() as source:
                print("JARVIS is listening:")
                audio = r.listen(source)
                print(r.recognize_sphinx(audio))
                r.energy_threshold = 1000

    else:
        print("c")

except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


