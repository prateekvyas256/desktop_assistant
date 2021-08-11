import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getproperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')

    elif hour>=12 and hour<18:
        speak('good aftenoon')

    else:
        speak('good evening')

    speak('i am jarvis sir .what can i help you')

def takecommand():
    # it take microphone input from the user and return string output 

    r = sr.recoginzer()
    with sr.microphone() as sources:
        print("listening..")
        r.pause_threshold = 1
        audio = r.listen(source)


try:
    print('recognizing...')
    query = r.recognize_google(audio,language = 'en-in')
    print(f'user said: {query}\n')

except Exception as e :
    print(e)

    print('say that again please...')
    return'none'
return query


if__name__=="__main__":     
    wishme()
    while True:
    query = take command().lower()

    # logic for executing tasks based on story
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentence=2)
        print(results)
        speak(results)
    elif'open youtube'in query:
        webrowser.open('youtube.com')
    
    elif'open google'in query:
        webrowser.open('google.com')

    elif'open stackoverflow'in query:
        webrowser.open('stackoverflow.com')

    elif' the time ' in query:
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'sir,the time is {strTime}')   

    elif' opencode ' in query:
        codepath = 'C:\\Users\\prate\\shotcut\\shotcut.exe'
        os.startfile(codepath)

    if 'quit ' in query:
        exit()