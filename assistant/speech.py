import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:

        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None