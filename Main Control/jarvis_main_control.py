#########################################
#   JARVIS Main Control by Colby Pryor  #
#########################################
import speech_recognition as sr
from meross_iot.manager import MerossManager
from meross_iot.cloud.devices.power_plugs import GenericPlug
from meross_iot.meross_event import MerossEventType
from meross_iot.api import MerossHttpClient
from gtts import gTTS
import pygame
import time
import sys
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
    while(r.recognize_sphinx(audio) != "quit"): 
        while(r.recognize_sphinx(audio) == "jarvis"):  
            with sr.Microphone() as source:
                print("JARVIS is listening:")
                audio = r.listen(source)
                print(r.recognize_sphinx(audio))
                r.energy_threshold = 1000
                speakwords = "Hello Colby! What can I do for you?"
                texttoaud = gTTS(text=speakwords, lang='en-us')
                texttoaud.save(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords1.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords1.mp3")
                pygame.mixer.music.play()
                time.sleep(float(2.3))
                pygame.mixer.music.load(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\beep_tone.mp3")
                pygame.mixer.music.play()
                with sr.Microphone() as source:
                        print("JARVIS is listening:")
                        audio = r.listen(source)
                light_list = ['lights','light','the light','on','ah']
                if(r.recognize_sphinx(audio) in light_list):
                        r.energy_threshold = 1000
                        speakwords = "Would you like them on or off?"
                        texttoaud = gTTS(text=speakwords, lang='en-us')
                        texttoaud.save(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords2.mp3")
                        pygame.mixer.init()
                        pygame.mixer.music.load(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords2.mp3")
                        pygame.mixer.music.play()
                        time.sleep(float(2.3))
                        pygame.mixer.music.load(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\beep_tone.mp3")
                        pygame.mixer.music.play()
                        with sr.Microphone() as source:
                            print("JARVIS is listening:")
                            audio = r.listen(source)
                        if(r.recognize_sphinx(audio) == 'on'):
                            r.energy_threshold = 1000
                            speakwords = "Turning on the light"
                            texttoaud = gTTS(text=speakwords, lang='en-us')
                            texttoaud.save(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords3.mp3")
                            pygame.mixer.init()
                            pygame.mixer.music.load(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords3.mp3")
                            pygame.mixer.music.play()
                        elif(r.recognize_sphinx(audio) == 'off'):
                            r.energy_threshold = 1000
                            speakwords = "Turning off the light"
                            texttoaud = gTTS(text=speakwords, lang='en-us')
                            texttoaud.save(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords4.mp3")
                            pygame.mixer.init()
                            pygame.mixer.music.load(r"C:\Users\colby\OneDrive\Desktop\J.A.R.V.I.S\Main Control\audio\speakwords4.mp3")
                            pygame.mixer.music.play()
            if(r.recognize_sphinx(audio) == "hello"):
                print("hi")
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


