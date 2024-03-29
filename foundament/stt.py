import speech_recognition as sr


r = sr.Recognizer()


with sr.Microphone() as source:
    print("speak: ")
    try:
        
        audio = r.listen(source, timeout=5)
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
