import requests
from engine import Engine
import online_ops
import os_ops
from userinputs import take_user_input

if __name__ == '__main__':
    engine = Engine()
    engine.greet_user()
    while True:
        query = take_user_input().lower()
        if 'open notepad' in query:
            os_ops.open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            os_ops.open_cmd()

        elif 'open camera' in query:
            os_ops.open_camera()

        elif 'open calculator' in query:
            os_ops.open_calculator()

        elif 'ip address' in query:
            ip_address = online_ops.find_my_ip()
            engine.speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            engine.speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = online_ops.search_on_wikipedia(search_query)
            engine.speak(f"According to Wikipedia, {results}")
            engine.speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            engine.speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            online_ops.play_on_youtube(video)

        elif 'search on google' in query:
            engine.speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            online_ops.search_on_google(query)

        elif "send whatsapp message" in query:
            engine.speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            engine.speak("What is the message sir?")
            message = take_user_input().lower()
            online_ops.send_whatsapp_message(number, message)
            engine.speak("I've sent the message sir.")

        elif "send an email" in query:
            engine.speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            engine.speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            engine.speak("What is the message sir?")
            message = take_user_input().capitalize()
            if online_ops.send_email(receiver_address, subject, message):
                engine.speak("I've sent the email sir.")
            else:
                engine.speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            engine.speak(f"Hope you like this one sir")
            joke = online_ops.get_random_joke()
            engine.speak(joke)
            engine.speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

        elif "advice" in query:
            engine.speak(f"Here's an advice for you, sir")
            advice = online_ops.get_random_advice()
            engine.speak(advice)
            engine.speak("For your convenience, I am printing it on the screen sir.")
            print(advice)


        elif 'news' in query:
            engine.speak(f"I'm reading out the latest news headlines, sir")
            engine.speak(online_ops.get_latest_news())
            engine.speak("For your convenience, I am printing it on the screen sir.")
            print(*online_ops.get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = online_ops.find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            engine.speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = online_ops.get_weather_report(city)
            engine.speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            engine.speak(f"Also, the weather report talks about {weather}")
            engine.speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        else:
            engine.speak("I am not well taught enough")
