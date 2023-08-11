import pyttsx3
import datetime
import speech_recognition as sr 
import webbrowser as wb
import os
tuesday=pyttsx3.init()
voice=tuesday.getProperty('voices')
tuesday.setProperty('voice', voice[1].id)

def speak(audio):
    print("Tuesday:"+ audio)
    tuesday.say(audio)
    tuesday.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%I: %M: %p")
    speak(time)

def welcome():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning sir")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon sir" )
    else:
        speak("Good Night Sir")
    speak("How can I help you") 
def command():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        r.pause_threshold= 1
        audio = r.listen(source)
        
        try:
            said=r.recognize_google(audio,language="en")
            print("Mr. Hoang "+ said)

        except Exception as e:
            print("Exception:" + str(e))
    return said

if __name__== "__main__":
    welcome()
    
    while True:
        said= command().lower()
        speak(said)
        if "google" in said :
            speak("What shoud I search boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "Youtube" in said :
            speak("What shoud I search boss?")
            search=command().lower()
            url=f"https://www.youtube.com//search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "open video" in said:
            meme=r"C:\Users\hoang\Videos\Captures\meme.mp4"
            os.startfile(meme)
        elif "sing" in said:
            sofa=r"C:\Users\hoang\Videos\Captures\sofa.mp3"
            os.startfile(sofa)
        elif "time" in said:
            time()
        elif "quit" in said:
            speak("Tuesday is quitting sir.Goodbye boss")   
            quit()
    
        


        


