import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def help() :
    Command = ' 1. open <application name>\n 2. play music\n 3. shut down\n 4. clean <directory name/path>\n 5. stop music\n 6. play movie\n 7. youtube\n 8. google\n 9. log in to insta\n'
    print(Command)
    pop = 'You can use only these commands'
    print(pop)
    speak(pop)
    