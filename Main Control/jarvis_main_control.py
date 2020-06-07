#########################################
#   JARVIS Main Control by Colby Pryor  #
#########################################
import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("JARVIS is listening:")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    if(r.recognize_sphinx(audio) == str("hey jarvis")):
       print("Hi colbs")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


