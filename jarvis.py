import pyttsx3
import speech_recognition as sr
import datetime as dt
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    
    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#voice to text
def wish():
    hour = int(dt.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis, please tell me how can I help you?")

if __name__ == "__main__":
        #speak("Hello I am Jarvis")
        #take_command()
        wish()

        #while True:
        query = take_command().lower()

            #logic for tasks
        if "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")
