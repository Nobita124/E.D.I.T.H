#pip install commands should be ran on cmd/command prompt
import pyautogui #pip install pyautogui
from time import sleep
import pyttsx3 #pip install pyttsx3
import os
import webbrowser #pip install webbrowser
from selenium import webdriver #pip install InstaPy
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
from getpass import getpass
from random import randint
from Greet import greet
from Help import help
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#for male voice type "voices[0].id" for female voice type "voices[1].id only if you have only two voices"
#I have three voices so I use voices[2].id for female voice i.e Zira


#This is main Code

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

greet()

def start():
    
        order = '\nPlease tell me what can I do for you ...\n'
        print(order)
        speak(order)
        com = input('--> ')
        com = com.lower()
        coma = com.split(" ")
        if coma[0].startswith('open'):
            task = coma[0] + "ing " + coma[1] + '\n'
            print(task)
            speak(task)
            sleep(randint(1,5))
            pyautogui.hotkey('win','r')
            sleep(randint(1,5))
            pyautogui.write(coma[1])
            pyautogui.press('enter')

        elif 'play music' in com : 
            music_dir = 'Song' #your music directory
            song = os.listdir(music_dir)
            print(song)
            task = '\nSir! please Copy and paste the name of the music from above you wanna play' + '\n'
            print(task)
            speak(task)
            name = input()
            na = '\nplaying music ' + name
            print(na)
            speak(na)
            sleep(randint(1,5))
            os.startfile(os.path.join(music_dir, name))
        elif coma[0].startswith('shut'):
            task = coma[0] + 'ing ' + coma[1] + '\n'
            print(task)
            speak(task)
            sleep(randint(1,5))
            pyautogui.hotkey('win','r')
            sleep(randint(1,5))
            pyautogui.write('shutdown -s')
            sleep(randint(1, 5))
            pyautogui.press('enter')
        elif coma[0].startswith('stop'):
            task = coma[0] + 'ing ' + coma[1] + '\n'
            print(task)
            speak(task)
            sleep(randint(1,5))
            pyautogui.hotkey('alt','tab')
            sleep(randint(1,5))
            pyautogui.hotkey('alt','f4')
        elif coma[0].startswith('clean'):
            task = coma[0] + 'ing ' + coma[1] + '\n'
            print(task)
            speak(task)
            sleep(randint(1,5))
            pyautogui.hotkey('win','r')
            sleep(randint(1,5))
            pyautogui.write(coma[1])
            pyautogui.press('enter')
            sleep(randint(1, 5))
            #pyautogui.press('enter')
            sleep(randint(1,5))
            pyautogui.hotkey('ctrl','a')
            sleep(randint(1,5))
            pyautogui.hotkey('shift','del')
            sleep(randint(1,5))
            pyautogui.press('enter')
        
        elif 'play movie' in com :
            movie_dir = 'D:\\Movies' #your movie directory
            film = os.listdir(movie_dir) 
            print(film)
            task = 'Copy and paste the name of the movie from above you wanna play'+ '\n'
            print(task)
            speak(task)
            nam = input()
            flm = '\nplaying movie ' + nam
            print(flm)
            speak(flm)
            sleep(randint(1,5))
            os.startfile(os.path.join(movie_dir, nam))
        elif 'youtube' in com :
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://www.youtube.com/')
            task = 'opening youtube \n'
            print(task)
            speak(task)
        elif 'google' in com :
            webbrowser.open("google.com")
        elif 'log in to insta' in com:
            nme = input("Enter your username : ")
            passwor= getpass('Enter your password : ')
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://www.instagram.com/')
            print ("Opened Instagram \n")

            sleep(randint(1,4))
            username = driver.find_element_by_name('username')
            username.send_keys(nme)
            password = driver.find_element_by_name('password')
            password.send_keys(passwor)
    
            button_login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
            button_login.click()
        #sleep(randint(3,5))

        #notnow = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
        #notnow.click()
        #sleep(randint(3,5))
        #notificationnotnow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        #notificationnotnow.click()
        elif 'help' in com :
            help()
            return start()
        else :
            non = 'Sorry Sir, Command Not found'
            print(non)
            speak(non)
            return start()

if __name__ == "__main__":
    start()
    while True:
        
         end = ('\nIs there anything else I can do for you : \n')
         print(end)
         speak(end)
         con=input('-->')
         if con.startswith('Y'):
                start()
         elif con.startswith('N'):
                con = '\nBye Sir ! I Hope that we will meet again \n'
                print(con)
                speak(con)
                exit()
