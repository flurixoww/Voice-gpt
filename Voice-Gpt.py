import speech_recognition as sr
import g4f
import pyttsx3
import os
import webbrowser


r = sr.Recognizer()

#voice settings
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


while True:
    with sr.Microphone() as source:
        engine.say("Speak")
        engine.runAndWait()
        print("speak: ")
        try:
        
            audio = r.listen(source, timeout=2)
        except sr.WaitTimeoutError:
            print("Time is out, writing")
            audio = None

    recognized_text = None
    if audio is not None:
        try:
        
            recognized_text = r.recognize_google(audio, language='en-US')
            print("You tell: " + recognized_text)
        except sr.UnknownValueError:
            print("Google Speech Recognition can't recognise audio")
        except sr.RequestError as e:
            print("Failed to connect with Google Speech Recognition; {0}".format(e))


    quest = recognized_text
   

    if quest == "end":
        engine.say("Stopping the program")
        engine.runAndWait()
        break

    if quest == "stop":
        engine.say("Stopping the program")
        engine.runAndWait()
        break
##########################################################################
    # User commands
    if quest == "open browser":
        engine.say("Oppening browser")
        engine.runAndWait()
        webbrowser.open('https://', new=2)
        continue
        

    if quest == "open telegram":
        engine.say("Opening telegram")
        engine.runAndWait()
        os.startfile(r'J:\Telegram Desktop\Telegram.exe')
        continue

    if quest == "open YouTube":
        engine.say("Opening YouTube")
        engine.runAndWait()
        webbrowser.open('https://youtube.com', new=2)
        continue

    if quest == "open Steam" or "open steam":
        engine.say("Opening Steam")
        engine.runAndWait()
        os.startfile(r"D:\steam\steam.exe")
        continue

    
##############################################################################


    def ask_gpt(message:str) -> str:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[
                {"role": "user", "content": message}
            ])
        
        return response and engine.say(response)
        
    
 

    ask_gpt(quest)
    engine.runAndWait()