import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from AppOpener import open,close
import time 
# import os 
import smtplib

print
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speek(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0)and(hour < 12) :
        speek("good morning")
    elif (hour>=12)and(hour<18):
        speek("good afternoon ")
    else:
        speek("good evening")

    speek ("i am zira ") 
    time.sleep(0)
    speek (" plz tell what can i help you") 

def send_Email(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.login("nominathnk@gmail.com",'@kuwar2004')
    server.sendmail('nominathnk@gmail.com',to,content)



def take_command():
    '''taking input from user and convert speech to str'''
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listerning....")
        r.energy_threshold= 800
        audio = r.listen(source)
        

    try:
        print('recognizing...')
        quiry = r.recognize_google(audio,language='en-in')
        print(f"user said: {quiry}\n")

    except Exception as e :
        print("say that again plz...")
        return "none"
    return quiry   

if __name__ == "__main__":
    wishme()
    while True:
        query = take_command().lower()
        if 'hay switty' in query:
            speek("hellow nominath what can i help")
        
        if 'wikipedia' in query:
                speek("surching on wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences = 2)
                speek("according to wikipedia.....")
                speek (results)
                
        
        elif 'open youtube' in query:
                speek("opening youtube!")
                open('YouTube')

        elif 'open vs code' in query:
                speek ('opening visual studio code')
                open('Visual Studio Code')
                
        elif 'open google' in query:
                speek ("opening google.com")
                webbrowser.open("https://www.google.com/")

        elif 'open whats app' in query:
                speek ("opening whats app")
                open("WhatsApp Web")
            
        elif 'the time' in query:
                strtime = datetime.datetime.now().strftime('%H:%M:%S')
                speek(f"the time is{strtime}")

        elif 'send email to nominath' in query:
            try:
                speek("what should i say?")
                content  = take_command()
                to = "nominathyouremail@gmal.com"
                send_Email(to,content)
                speek("email has been sent!")
            except Exception as e :
                print(e)
                speek ('sorry we can not send email!')


        elif 'stop' in query:
                speek(f"thank for using me")
                time.sleep(0)
                speek(f"have a nice day")
                break  
