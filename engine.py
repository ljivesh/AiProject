import pyttsx3
from datetime import datetime
from utils import credentials

class Engine:
    def __init__(self) -> None:
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty('rate', 190)
        self.engine.setProperty('volume', 1.0)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.say("Hello")
        self.engine.runAndWait()

    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self):
    
        USERNAME = credentials['USERNAME']
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            self.speak(f"Good Morning {USERNAME}")
        elif (hour >= 12) and (hour < 16):
            self.speak(f"Good afternoon {USERNAME}")
        elif (hour >= 16) and (hour < 24):
            self.speak(f"Good Evening {USERNAME}")
        
        self.speak(f"I am MENMA. How may I assist you?")
    
    def introduce(self):
        


if __name__ == '__main__':
    engine = Engine()
    engine.greet_user()