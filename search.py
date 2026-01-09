import speech_recognition as sr 
from voices import speak 
import pywhatkit 
import wikipedia 
import webbrowser 


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source, 0, 4)
        text = r.recognize_sphinx(audio)
        print(text)

    try:
        print("understanding")
        quary = r.recognize_google(audio, language='en-in')
        print(f"you said: {quary}")
        return quary
    except Exception as e:
        print(" say that again ")
        return "none"
    return quary

def searchgoogle(quary):
    if "google" in quary:
        import wikipedia as googlesearch
        quary = quary.replace("maria", "")
        quary = quary.replace("search on google", "")
        quary = quary.replace("google","")
        speak(" this is what i found in the google, master")
        
        try:
            pywhatkit.search(quary)
            result = googlesearch.summary(quary,2 )
            speak(result)

        except:
            speak("no speakabe output availabe")

def searchyoutube(quary):
    if "youtube" in quary:
        speak(" this is what i found in the youtube, master")
        quary = quary.replace("maria", "")
        quary = quary.replace("search on youtube", "")
        quary = quary.replace("youtube","")
        web = "https://www.youtube.com/results?search_quary=" + quary
        webbrowser.open(web)
        pywhatkit.playonyt(quary)
        speak("done sir ")

def searchwikipedia(quary):
    if "wikipedia" in quary:
        speak(" seaching on wikipedia..., master")
        quary = quary.replace("maria", "")
        quary = quary.replace("search on wikipedia", "")
        quary = quary.replace("wikipedia","")
        result = wikipedia.summary(quary,sentences=2 )
        speak(" Accourding to the wikipedia....")
        print(result)
        speak(result)
