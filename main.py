import pyttsx3
import speech_recognition as sr
import datetime
import os


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


if __name__ == "__main__":
    wish()

    # while True:
    if 1:

        query = takecommand().lower()

        #logic building for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        # elif "open camera" in query:



