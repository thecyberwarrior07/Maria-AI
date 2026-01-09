#from logging import exception
import sys
import pygame
import os
import requests
from bs4 import BeautifulSoup
import datetime
#import edge_tts
#import pyttsx3 as p
#from temp import speak
#import search
import speech_recognition as sr

# creating an engine
#engine = p.init()
#rate = engine.getProperty("rate")
#engine.setProperty("rate",110)
# getting system voice
#voices=engine.getProperty('voices')
# setting-up our engine voice to windows
#engine.setProperty("voice",voices[1].id)

#def speak(audio):
 #   engine.say(audio)
  #  engine.runAndWait()


def speak(text) :
     voice = 'en-US-EmmaMultilingualNeural'
     text = text.replace("&", "&amp;")
     data = f"python -m edge_tts --rate=+0% --voice \"{voice}\" --text \"{text}\" --write-media \"data.mp3\""
     os.system(data)

     pygame.init()
     pygame.mixer.init()
     pygame.mixer.music.load("data.mp3")

     try:
          pygame.mixer.music.play()

          while pygame.mixer.music.get_busy():
               pygame.time.Clock().tick(10)

     except Exception as e:
          print(e)

     finally:
          pygame.mixer.music.stop()
          pygame.mixer.quit()

# getting speech recognition 

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 30
        r.adjust_for_ambient_noise(source, 1.5)
        print("listening...")
        audio = r.listen(source, 0, 7)
        text = r.recognize_sphinx(audio)
        text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        print(text)
    try:
        print("understanding")
        quary = r.recognize_google(audio, language='en-in')
        print(f"you said: {quary}\n")
    except Exception as e:
        print(" say that again ")
        return "none"
    return quary

if __name__ == "__main__":
    while True :
        quary = TakeCommand().lower()
        if "wake up" in quary:
            from greetomaster import greet
            g = greet
            speak(g)
            while True:
                quary = TakeCommand().lower()
                if "go sleep" in quary:
                    speak(" ohk sir, you can call me anytime")
                    break
                elif "hello mariya" in quary:
                    speak("hello sir, how are you?")
                elif "open" in quary:
                    from opnapps import openappweb
                    openappweb(quary)
                elif "close" in quary:
                    from opnapps import closewebapp
                    closewebapp(quary)
                elif "google" in quary:
                    from search import searchgoogle
                    searchgoogle(quary)
                elif "youtube" in quary:
                    from search import searchyoutube
                    searchyoutube(quary)
                elif "wikipedia" in quary:
                    from search import searchwikipedia
                    searchwikipedia(quary)
                elif "temperature" in quary:
                    search = " temperature in khargone "
                    url = "https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {temp} in {search}")
                elif "weather" in quary:
                    search = " weather in khargone "
                    url = "https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {temp} in {search}")
                elif "time" in quary:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f" Your current time {strTime}")
                elif "finally sleep" in quary:
                    speak("going to sleep, master")
                    exit()
                