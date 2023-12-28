import pyttsx3
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

if __name__ == "__main__":
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
                content = takecommand().lower()
                to = "kaushikdakua5@gmail.com"
                sendEmail(to, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry sir, i am unable to send the mail to the user")

        elif "no thank you" in query:
            speak("Thank you using me and have good day sir...")
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
        #speak("Sir do you have any other work for me!")


