import os
import speech_recognition as sr
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

while True:
    wake_Up =takecommand()

    if 'wake up' in wake_Up:
      os.startfile("C:\\Python 3.9\\Scripts\\Jarvis-Project\\jarvis.py")
    else:
      print("Nothing......")