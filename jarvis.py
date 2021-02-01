import pyttsx3  as pt3            #pip install pyttsx3
import datetime as dt             #in-built 
import speech_recognition as sr   #pip install speechRecognition
import wikipedia as wiki          #pip install wikipedia
import smtplib as smt             #pre-installed
import webbrowser as wb           #in-built
import psutil                     #pip install psutil


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

def send_email(to,content):
    server=smt.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    #for this function to work, you need to set your gmail security low, which will be used as sender
    server.login("username@gmail.com","password")
    server.sendmail("username@gmail.com", to, content)
    server.close()

def cpu_status():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

if __name__=="__main__":
    wish_me()
    while True:
        query=take_command().lower()
        #All Commands will be converted to lower case for easy query recognition

        if "time" in query:
            tell_time()

        elif "date" in query:
            tell_date()

        elif "search in wikipedia" in query:
            speak("Searching...")
            query=query.replace("search in wikipedia","")
            result=wiki.summary(query,sentences=3)
            print(result)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content=take_command()
                #provide recipient email
                receiver="receiver_is_me@gmail.com"
                to=receiver
                send_email(to,content)
                speak(content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send Email!")

        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            #chromepath is the location of your chrome's installation on your computer
            search=take_command().lower()
            wb.get(chromepath).open_new_tab(search+".com")       #websites ending with .com

        elif "search in youtube" in query:
            speak("What should I search?")
            search_term=take_command().lower()
            speak("Here we go to Youtube!")
            wb.open("https://www.youtube.com/results?search_query=" + search_term)

        elif "search in google" in query:
            speak("What should I search?")
            search_term=take_command().lower()
            speak("Searching...")
            wb.open("https://www.google.com/search?q="+search_term)

        elif "cpu" in query:
            cpu_status()