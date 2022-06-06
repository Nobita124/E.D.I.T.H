import pyttsx3

import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        out = "\nGood Morning Sir !"
        print(out)
        speak(out)
        
    elif hour>=12 and hour<18:
        out = "\nGood Afternoon Sir !"
        print(out)
        speak(out)
    else:
        out = "\nGood Evening Sir !"
        print(out)
        speak(out)  
        
    intro = '\nHello Sir ! I am Edith. Your desktop assistant.'
    print(intro)
    speak(intro)
