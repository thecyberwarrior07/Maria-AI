from voices import speak 
import time


greet = time.strftime("%H:%M:%S")
#getting our first welcome note
if greet == "00:00:00" :
    speak("hello sir, good morning, i'm maria ai, what can i do for you ???")
    print("hello sir, good morning, i'm maria ai, what can i do for you ???")
elif "00:00:00" < greet < "11:59:59":
    speak("hello sir, good morning, i'm maria ai, what can i do for you ???")
    print("hello sir, good morning, i'm maria ai, what can i do for you ???")
elif "12:00:00" < greet < "17:59:59":
    speak("hello sir, good afternoon, i'm maria ai, what can i do for you ???")
    print("hello sir, good afternoon, i'm maria ai, what can i do for you ???")
elif "18:00:00" < greet < "23:59:59":
    speak("hello sir, good Evening, i'm maria ai, what can i do for you ???")
    print("hello sir, good Evening, i'm maria ai, what can i do for you ???")
    