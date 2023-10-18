from tkinter.constants import COMMAND
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit 
import wikipedia
import os
import pyautogui 
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
import datetime
from playsound import playsound
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow

Assistant=pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',150)
def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f":{audio}")
    print("    ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening............")
        command.pause_threshold = 1
        audio = command.listen(source,timeout=5,phrase_time_limit=5)

        try: 
            print("Recognizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except:
            return "none"
        return query.lower()

def taskexecution():
    
 Speak("Hello Sir I am ZEN")
 Speak("How may I help you? ")
 
  
 def Whatsapp():
       Speak("Tell me the name of the Person!")
       name=takecommand()
       
       if 'deepanshu' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+919870808662",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
       elif 'aryan' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+919140289864",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
       elif 'rishika' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+918219714336",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
       elif 'kushagra' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+918887122744",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
       elif 'pra' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+918858532751",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
       elif 'sajal' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+919305493779",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
       elif 'riya' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+919548458448",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")

       elif 'suraj' in name:
           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg("+919870808662",msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
       else:
           Speak("Tell me the Phone Number")
           phone= int(takecommand())
           ph='+91' + phone

           Speak("Tell me the Message!")
           msg=takecommand()
           Speak("Tell Me the Time Sir!")
           Speak("Time in Hour!")
           hour=int(takecommand())
           Speak("Time in Minutes!")
           min=int(takecommand())
           pywhatkit.sendwhatmsg(ph,msg,hour,min,2)
           Speak("Ok sir,Sending Whatsapp Message !")
           
 
 def OpenApps():
     Speak("Ok sir, Wait a Second!")

     if 'Photoshop' in query:
       os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe")
     elif 'maps' in query:
       webbrowser.open("https://www.google.com/maps/@20.9880135,82.7525294,5z")   
     elif 'instagram' in query:
       webbrowser.open("https://www.instagram.com/")
     elif 'chrome' in query:
       os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
     elif 'moodle' in query:
       webbrowser.open("http://lms.kiet.edu/moodle/")        

     Speak("Your Command Has Been Sucessfully Completed!")     
 
 def YoutubeAuto():
     Speak("Whats Your Command?")
     comm=takecommand()

     if 'pause' in comm:
         keyboard.press('spacebar')
     elif 'restart' in comm:
         keyboard.press('0')
     elif 'mute' in comm: 
         keyboard.press('m')
     elif 'skip' in comm:
         keyboard.press('l')
     elif 'back' in comm:
         keyboard.press('j')
     elif 'full screen' in comm:
         keyboard.press('f')
     elif 'film mode' in comm:
         keyboard.press('t')
     Speak("Done Sir!")                   

 def Dict():
     Speak("Activating Dictionary!")
     Speak("Tell Me the Problem!")
     probl=takecommand()
     if 'meaning' in probl:
         probl=probl.replace("What is the","")
         probl=probl.replace("zen","")
         probl=probl.replace("of","")
         probl=probl.replace("meaning","")
         result= Diction.meaning(probl)
         Speak(f"The Meaning for{probl} is {result}")
         Speak("Exited Dictionary")

 def screenshot():
     Speak("Ok Sir, What Should I Name That File?")
     path= takecommand()
     path1name=path+".png"
     path1='C:\Python 3.9\Scripts\Jarvis-Project\Screenshot\\'+ path1name
     ss=pyautogui.screenshot()
     ss.save(path1)
     os.startfile("C:\Python 3.9\Scripts\Jarvis-Project\Screenshot")
     Speak("Here is Your ScreenShot!")  

 def TakeHindi():
    command = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening............")
        command.pause_threshold = 1
        audio = command.listen(source,timeout=5,phrase_time_limit=5)

        try: 
            print("Recognizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except:
            return "none"
        return query.lower()

 def Tran():
     Speak("Tell me The Line!")
     line=TakeHindi()       
     translate=Translator()
     result=translate.translate(line)
     Text=result.text
     Speak(Text)

 def Temp():
     search="temperature in ghaziabad"
     url=f"https://www.google.com/search?q={search}"
     r=requests.get(url)
     data = BeautifulSoup(r.text,"html.parser")
     temperature = data.find("div",class_= "BNeawe").text
     Speak(f"The Temprature Outside is {temperature}")

 def SpeedTest():
     import speedtest
     Speak("Checking speed...........")
     speed=speedtest.Speedtest()
     downloading=speed.download()
     correctDown= int(downloading/800000)
     uploading=speed.upload()
     correctUpload = int(uploading/800000)

     if 'uploading' in query:
         Speak(f"TheUploading Speed is {correctUpload} mbps ")

     elif 'downloading' in query:
         Speak(f"The Downloading Speed is {correctDown} mbps")
     else:
         Speak(f"The Downloading is {correctDown} and The Uploading Speed is {correctUpload} mbps")       

 while True:
      
   query=takecommand()

   if 'zen' in query:
           Speak("Hello Sir, I am zen.")
           Speak("Your personal AI Assistant")
           Speak("How May I Help You")
   elif 'how are you' in query:    
           Speak("I Am Fine Sir!")
   elif 'you may leave' in query:
           Speak(" OK Sir, You can call me Anytime! ")
           break    
   elif 'bye' in query:
           Speak('Have a good Day,Sir')
           break
   elif 'youtube search' in query:
           Speak("OK Sir ,This is What I found for your Search!")
           query=query.replace("zen","")
           query=query.replace("youtube search","")
           web='https://www.youtube.com/results?search_query='+ query
           webbrowser.open(web)
           Speak("Done Sir")
   elif 'google search' in query:
           import wikipedia as googleScrap
           query=query.replace("zen","")
           query=query.replace("google search","")
           query=query.replace("google","")
           Speak("This is what I found on Web!")
           pywhatkit.search(query)
           try:
               result=googleScrap.summary(query,3)
               Speak(result)
               Speak("Done Sir")
           except:
               Speak("No Data Available!")    
   elif 'website' in query:
           Speak("Ok sir,Launching....")
           query=query.replace("zen","")
           query=query.replace("website","")
           query=query.replace(" ","")
           web1=query.replace("open","")
           web2='http://www.'+ web1 + '.com'
           webbrowser.open(web2)
           Speak("Launched Sir!")
   elif 'launch' in query:
           Speak("Tell me the Name of the Website!")
           name=takecommand()
           web='http://www.'+ name + '.com'
           webbrowser.open(web)
           Speak("Done Sir!")
   elif 'open spotify' in query:
           Speak("Ok Sir!")
           webbrowser.open("https://open.spotify.com/")  
           Speak("Done Sir!")
   elif 'wikipedia' in query:
           Speak("Searching Wikipedia.............")
           query=query.replace("zen","")
           query=query.replace("wikipedia","")
           wiki=wikipedia.summary(query,4)
           Speak(f"According to Wikipedia :{wiki}")      
   elif 'whatsapp message' in query:
           Whatsapp()
   elif 'screenshot' in query:
          screenshot() 
   elif 'open Photoshop' in query:
           OpenApps()
   elif 'Spotify' in query:
           OpenApps()    
   elif 'maps' in query:
           OpenApps()
   elif 'chrome' in query:
           OpenApps()
   elif 'instagram' in query:
           OpenApps()    
   elif 'moodle' in query:
           OpenApps()
   elif 'stop' in query:
         keyboard.press('spacebar')
   elif 'restart' in query:
         keyboard.press('0')
   elif 'mute' in query: 
         keyboard.press('m')
   elif 'skip' in query:
         keyboard.press('l')
   elif 'back' in query:
         keyboard.press('j')
   elif 'full screen' in query:
         keyboard.press('f')
   elif 'film mode' in query:
         keyboard.press('t')        
   elif 'youtube tool' in query:
           YoutubeAuto()     
   elif 'joke' in query:
       get=pyjokes.get_joke()
       Speak(get)
   elif 'repeat my word' in query:
       Speak("Speak Sir")
       jj=takecommand()
       Speak(f"You Said:{jj}")
   elif 'my location' in query:
       Speak("Ok Sir, Wait a Second")
       webbrowser.open('https://www.google.com/maps/@27.224768,77.9994067,18z')
   elif 'dictionary' in query:
       Dict()
   elif 'play music' in query:
       Speak("Tell me THe name of the song!")
       musicName=takecommand()
       pywhatkit.playonyt(musicName)
       Speak("Your Song has been started!,Enjoy Sir!")
   elif 'set alarm' in query:
       Speak("Enter the Time!")
       time=input(": Enter the Time :")

       while True:
           Time_Ac= datetime.datetime.now()
           now=Time_Ac.strftime("%H:%M:%S")

           if now==time:
               Speak("Its Time to Work Sir!")
               playsound('LSD.mp3')
               Speak("Alarm Closed!")
           elif now>time:
               break    
   elif 'video downloader' in query:
       root= Tk()
       root.geometry('500x300')
       root.resizable(0,0)
       root.title("Youtube Video Downloader")
       Speak("Enter the Link!")
       Label(root,text="Youtube Video Downloader",font='arial 15 bold').pack()
       link= StringVar()
       Label(root,text='Paste Yt video URl here',font='arial 15 bold').place(x=160,y=60)
       Entry(root,width=70,textvariable=link).place(x=32,y=90)

       def VideoDownloader():
           url= YouTube(str(link.get()))
           video=url.streams.first()
           video.download()
           Label(root,text="Downloaded",font='arial 15').place(x=180,y=210)

       Button(root,text="Download",font = 'arial 15 bold',bg='pale violet red',padx= 2, command= VideoDownloader).place(x=180,y=150)
       root.mainloop()
       Speak("Video Downloaded")    
   elif 'translator' in query:
       Tran()
   elif 'remember that' in query:
       rememberMsg= query.replace("remember that","")
       rememberMsg=query.replace("zen","")
       Speak("You tell Me to remind you that:"+ rememberMsg)
       remember=open('data.txt','w')
       remember.write(rememberMsg)
       remember.close()
   elif 'what do you remember' in query:
       remember=open('data.txt','r')
       Speak("You tell me to "+remember.read())
   elif 'temperature' in query:
       Temp()
   elif 'downloading speed'in query:
       SpeedTest()
   elif 'uploading speed'in query:
        SpeedTest()
   elif 'internet speed' in query:
         SpeedTest()
   elif 'how to' in query:
       Speak("Getting Data from the Internet!")
       op=query.replace("zen","")
       max_result=1
       how_to_func=search_wikihow(op,max_result)
       assert len(how_to_func)==1
       how_to_func[0].print()
       Speak(how_to_func[0].print())
       Speak(how_to_func[0].summary)
      

taskexecution()    