import speech_recognition as sr
from engine import Engine
from random import choice
from datetime import datetime
from utils import opening_text

def take_user_input():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            engine.speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                engine.speak("Good night sir, take care!")
            else:
                engine.speak('Have a good day sir!')
            exit()
    except Exception:
        engine.speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


engine = Engine()