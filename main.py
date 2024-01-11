import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
# import requests
import instaloader
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=2, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
         speak("Say that again please...")
         return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("good evening")
    speak("I am Jarvis. Please tell me how can i help you?")

#to send email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("kaushikdakua05@gmail.com", "Lipu5122002")
    server.sendmail("kaushikdakua05@gmail.com", to, content)

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c945bc2748714212834e7ebd5cc4eb31"

    main_page = requests.get(main_url).json()
    #print(main page)
    articles = main_page["articles"]
    #print articles
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    book = open('hello.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages the book is {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def start():
    wish()
    while True:
    # if 1:

        query = takecommand().lower()

        #logic building for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("Sir, what should  i search  on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+916371123165", "hello", 2, 25)

        elif "play songs on youtube" in query:
            speak("Sir, which song you want to hear on youtube")
            ym = takecommand().lower()
            kit.playonyt(f"{ym}")

        elif "email to kaushik" in query:
            try:
                speak("what should i say?")
                to = "kaushikdakua5@gmail.com"
                content = takecommand().lower()
                sendEmail(to, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry sir, i am unable to send the mail to the user")

        elif "no thank you" in query:
            speak("Thank you using me and it's a pleasure to work with you...")
            sys.exit()

        # to close youtube
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

#to close youtube
        elif "close youtube" in query:
            speak("okay sir, closing youtube")
            os.system("taskkill /f /im www.youtube.com")
#to set alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 19:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
    #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")


###########################################################################################################
        #switch the window
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        #news telling
        elif "tell me news" in query:
            speak("please wait, fetching the latest top ten news reports")
            news()

        #to find the location using ip address
        elif "where am i" in query or "where i am" in query or "where are we" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but  i think  we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir, due to internet issue i couldn't able to find the location")
                pass

        #---to check instagram profile
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir, please enter the username correctly.")
            name = input("Enter your username")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download your profile picture of this account")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. Now i am ready for your next command")
            else:
                pass
        #---to take screenshot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir please tell me the name of the screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder.")

        #-------read pdf
        elif "read pdf" in query:
            pdf_reader()


        #-----------hide files and folder ------------
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in the folder are hidden")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in the folder are noe visible to everyone")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")

        speak("Sir do you have any other work for me!")
if __name__ == "__main__":
    start()

