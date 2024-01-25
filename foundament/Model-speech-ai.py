import g4f
import pyttsx3

#voice settings
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


while True:
    def ask_gpt(message:str) -> str:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[
                {"role": "user", "content": message}
            ])
        
        return engine.say(response)
        
    
    quest = str(input("Question: "))
    if quest == "end":
        
        break
    if quest == "stop":
        break
    
    ask_gpt(quest)
    engine.runAndWait()