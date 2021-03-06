import pyttsx3  as pt3            #pip install pyttsx3
import datetime as dt             #in-built 
import speech_recognition as sr   #pip install speechRecognition
import wikipedia as wiki          #pip install wikipedia
import smtplib as smt             #pre-installed
import webbrowser as wb           #in-built
import psutil                     #pip install psutil
import pyjokes as pj              #pip install pyjokes
import os                         #in-built
import pyautogui as pag           #pip install pyautogui
import random                     #in-built
import json                       #in-built
import requests                   #in-built
from urllib.request import urlopen #in-built
import wolframalpha as wfa        #pip install wolframalpha
import time                       #in-built


engine=pt3.init()
wolframa_id= "wolframa_app_id here"

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

def tell_joke():
    speak(pj.get_joke())

def take_screenshot():
    img=pag.screenshot()
    strTime=dt.datetime.now().strftime("%H:%M:%S").replace(":","")
    img.save("C:/Users/ankit/Documents/Github/JARVIS-2.0/"+strTime+".png")

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

        elif "joke" in query:
            tell_joke()

        elif "offline" in query or "quit" in query:
            speak("Going offline sir!")
            quit()

        elif "word" in query:
            speak("Opening MS Word")
            ms_word=r"C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"   #path of executable file
            os.startfile(ms_word)

        elif "write a note" in query:
            speak("What should I write, Sir?")
            notes=take_command().lower()
            file=open("notes.txt","w")
            speak("Should I include date and time, sir?")
            ans=take_command().lower()
            if "yes" in ans or "sure" in ans:
                strTime=dt.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak("Done taking notes, Sir!")
            else:
                file.write(notes)

        elif "show notes" in query:
            speak("Showing Notes!")
            file=open("notes.txt","r")
            print(file.read())
            speak(file.read())

        elif "screenshot" in query:
            take_screenshot()

        elif "play song online" in query:
            song_dir="C:/Users/ankit/AppData/Roaming/Spotify/Spotify.exe"
            os.startfile(song_dir)

        elif "play song offline" in query:
            songs_dir="D:/Songs"
            music=os.listdir(songs_dir)
            speak("What should I Play sir?")
            speak("Select a number..")
            ans=take_command().lower()
            while("number" not in ans and ans!="random" and ans!="you choose" and ans!="your call"):
                speak("I could not understand your answer. Please Try again!")
                ans=take_command().lower()
            if "number" in ans:
                no=int(ans.replace("number",""))
            elif "random" in ans or "you choose" in ans or "your call" in ans:
                no=random.randint(1,100)
            
            os.startfile(os.path.join(songs_dir,music[no]))

        elif "remember that" in query:
            speak("What should I remember sir?")
            memory=take_command().lower()
            speak("You asked me to remember"+memory)
            remember=open("memory.txt","w")
            remember.write(memory)
            remember.close()

        elif "do you remember" in query:
            file=open("memory.txt","r")
            speak("You asked me to remember that "+file.read())

        elif "news" in query:
            try:
                jsonObj=urlopen("http://newsapi.org/v2/everything?q=tesla&from=2021-01-01&sortBy=publishedAt&apiKey=API_KEY")
                data=json.load(jsonObj)
                i=1

                speak("Here are some top headlines from Tesla")
                print("================TOP HEADLINES================"+"\n")
                for item in data["articles"]:
                    print(str(i)+". "+item["title"]+"\n")
                    print(item["description"]+"\n")
                    speak(item["title"])
                    i+=1
            except Exception as e:
                print(str(e))

        elif "where is" in query:
            query=query.replace("where is","")
            location=query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif "calculate" in query:
            client=wfa.Client(wolframa_id)
            index=query.lower().split().index("calculate")
            query=query.split()[index+1:]
            res=client.query("".join(query))
            answer=next(res.results).text
            print("The answer is: "+answer)
            speak("The answer is:"+answer)

        elif "what is" in query or "who is" in query:
            client=wfa.Client(wolframa_id)
            res=client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration :
                print("No results")

        elif "stop listening" in query:
            speak("For how many seconds you want me to stop listening to your commands sir?")
            ans=int(take_command().lower().replace("seconds",""))
            time.sleep(ans)
            
        elif "log out" in query:
            os.system("shutdown -l")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")