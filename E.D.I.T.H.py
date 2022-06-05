import pyautogui
from time import sleep
import pyttsx3
import speech_recognition as sr
import pyaudio
import os
import webbrowser
from selenium import webdriver #pip install InstaPy
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
from getpass import getpass
from random import randint
from Greet import greet
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#for male voice type "voices[0].id" for female voice type "voices[1].id"


##This is main Code

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    greet()
    speak('Please tell me what can I do for you ...')
    com = input()
    com = com.lower()
    coma = com.split(" ")
    if coma[0].startswith('open'):
        speak(coma[0] + "ing " + coma[1])
        sleep(0.50)
        pyautogui.hotkey('win','r')
        sleep(2)
        pyautogui.write(coma[1])
        pyautogui.press('enter')

    elif 'play music' in com : 
        music_dir = 'Song'
        song = os.listdir(music_dir)
        print(song)
        speak('Sir! please Copy and paste the name of the music from above you wanna play')
        name = input()
        speak('playing music' + name)
        sleep(0.50)
        os.startfile(os.path.join(music_dir, name))
    elif coma[0].startswith('shut'):
        speak(coma[0] + 'ing ' + coma[1])
        sleep(0.50)
        pyautogui.hotkey('win','r')
        sleep(0.75)
        pyautogui.write('shutdown -s')
        sleep(1)
        pyautogui.press('enter')
    elif coma[0].startswith('off'):
        speak(coma[0] + 'ing ' + coma[1])
        sleep(0.50)
        pyautogui.hotkey('alt','tab')
        sleep(2)
        pyautogui.hotkey('alt','f4')
    elif coma[0].startswith('clean'):
        speak(coma[0] + 'ing ' + coma[1])
        sleep(0.50)
        pyautogui.hotkey('win','r')
        sleep(1)
        pyautogui.write(coma[1])
        pyautogui.press('enter')
        sleep(1.5)
        #pyautogui.press('enter')
        sleep(0.25)
        pyautogui.hotkey('ctrl','a')
        sleep(0.50)
        pyautogui.hotkey('shift','del')
        sleep(1)
        pyautogui.press('enter')
    elif coma[0].startswith('defragment'):
        speak(coma[0] + 'ing ')
        sleep(0.50)
        pyautogui.press('win')
        pyautogui.write('Defragmentation')
        sleep(2.5)
        pyautogui.moveTo(243,119,duration=0.25)
        pyautogui.click()
    elif 'play movie' in com :
        movie_dir = 'D:\\Movies'
        film = os.listdir(movie_dir)
        print(film)
        speak('Copy and paste the name of the movie from above you wanna play')
        nam = input()
        speak('playing movie' + nam)
        sleep(0.50)
        os.startfile(os.path.join(movie_dir, nam))
    elif 'youtube' in com :
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.youtube.com/')
    elif 'google' in com :
        webbrowser.open("google.com")
    elif 'log in on insta' in com:
        nme = input("Enter your username : ")
        passwor= getpass('Enter your password : ')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.instagram.com/')
        print ("Opened Instagram")

        sleep(randint(1,4))
        username = driver.find_element_by_name('username')
        username.send_keys(nme)
        password = driver.find_element_by_name('password')
        password.send_keys(passwor)
    
        button_login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
        button_login.click()
        sleep(randint(3,5))

        notnow = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
        notnow.click()
        sleep(randint(3,5))
        notificationnotnow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notificationnotnow.click()

if __name__ == "__main__":
    start()
    while True:
         speak('Is there anything else I can do for you : ')
         con=input()
         if con.startswith('Y'):
                start()
         elif con.startswith('N'):
                speak('Bye Sir ! I Hope that we will meet again ')
                exit()
               
