import pyttsx3  as pt3         #pip install pyttsx3
import datetime as dt          #in-built 
engine=pt3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tell_time():
    time=dt.datetime.now().strftime("%H:%M:%S")
    speak("The Current time is: "+ time)

def tell_date():
    date=dt.datetime.now().day
    month=dt.datetime.now().month
    year=dt.datetime.now().year
    speak("The current date is :{} {} {}".format(date,month,year))

