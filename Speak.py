import pyttsx3
import speech_recognition as sr
import pyaudio 
import wikipedia
import webbrowser
import os
import datetime
import google

engine = pyttsx3.init('sapi5')
'''init is a factory function in python which creates an object of the required class . Here it creates an object of the Engine class in the pattysx3 module'''
'''engine is the object'''

voices = engine.getProperty('voices')
'''getProperty is just a normal function of the Engine class'''

print(voices[0].id)
engine.setProperty('voice' , voices[0].id)

def takeCommand():
    # It takes microphone input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio , language = 'en-in')
        print(f"User said : {query} \n")
    
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":

    now1 = datetime.datetime.now()
    hours = now1.strftime('%H')
    if hours > 12 and hours <= 18: 
        speak("Good Afternoon")
    elif hours > 18 and hours < 20:
        speak("Good Evening")
    elif hours > 20:
        speak("Good night")
    else:
        speak("Good Morning")
    
    speak("My name is IEDC Robot")
    speak("Wishing you a very happy puja")
    speak("I am here at your service")

    speak("You can ask me things like ...")
    speak("  ")
    speak("Search Google , Search Wikipedia , Open Youtube , Open Stackoverflow , Say the time , Say the date , Play music ")
    speak("And a lot more")
    speak("The more you ask questions , the more I get developed")
    
    if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query :
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences = 2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.come")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Desktop\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Sir , the time is {strTime}")

        elif 'the date' in query:
            now = datetime.datetime.now()
            speak(f"It is {now.strftime('%A, %B the %dth, %Y')}")

        elif 'google search' in query :
            speak("Searching Google.....")
            query = query.replace("google search" , "")
            results = google.summary(query , sentences = 2)
            speak("According to Google ")
            print(results)
            speak(results)
        
        

        
 
    







