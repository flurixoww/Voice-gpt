import speech_recognition as sr


r = sr.Recognizer()


# with sr.Microphone() as source:
#     print("speak: ")
#     try:
        
#         audio = r.listen(source, timeout=5)
#     except sr.WaitTimeoutError:
#         print("Time is out, writing")
#         audio = None

# recognized_text = None
# if audio is not None:
#     try:
        
#         recognized_text = r.recognize_google(audio, language='en-US')
#         print("You tell: " + recognized_text)
#     except sr.UnknownValueError:
#         print("Google Speech Recognition can't recognise audio")
#     except sr.RequestError as e:
#         print("Failed to connect with Google Speech Recognition; {0}".format(e))




import g4f
import pyttsx3

#voice settings
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


while True:
    with sr.Microphone() as source:
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





    def ask_gpt(message:str) -> str:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[
                {"role": "user", "content": message}
            ])
        
        return response and engine.say(response)
        
    
    quest = recognized_text
    if quest == "end":
        
        break
    if quest == "stop":
        break

    ask_gpt(quest)
    engine.runAndWait()