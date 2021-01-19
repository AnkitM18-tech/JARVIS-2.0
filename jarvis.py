import pyttsx3  as pt3            #pip install pyttsx3
import datetime as dt             #in-built 
import speech_recognition as sr   #pip install speechRecognition

engine=pt3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tell_time():
    time=dt.datetime.now().strftime("%H:%M:%S")   #24 hour format
    #time=dt.datetime.now().strftime("%I:%M:%S")   #12 hour format
    speak("The Current time is: ")
    speak(time)

def tell_date():
    date=dt.datetime.now().day
    month=dt.datetime.now().month
    year=dt.datetime.now().year
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
    
def wish_me():
    speak("Welcome Back Ankit!")
    tell_date()
    tell_time()

    #greetings
    hour=dt.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<24:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("JARVIS at your service sir! Please tell me how can I help you?")

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-US")
        print(query)
    except Exception as e:
        print(e)
        print("Say That Again please!...")
        return None
    return query

if __name__=="__main__":
    wish_me()
    while True:
        query=take_command().lower()
        #All Commands will be converted to lower case for easy query recognition

        if "time" in query:
            tell_time()

        if "date" in query:
            tell_date()
