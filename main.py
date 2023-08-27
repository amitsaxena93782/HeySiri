import datetime
import os
import webbrowser

from ai_chat import chat
from utility import say, takeCommand

if __name__ == '__main__':
    print("Hello I am Siri, what can I do for you today")
    say("Hello I am Siri, what can I do for you today")
    while True:
        print("Listening...")
        query = ""
        while True:
            query = takeCommand()
            if (query != ""):
                break
        if (query == ""):
            print("Could'nt identify your voice! Please try again!")
            say("Could'nt identify your voice! Please try again!")
        print("Recognising...\n")

        print(f"Amit: {query}")
        stops = ["stop", "exit", "end", "bye", "see you"]
        end = False
        for stop in stops:
            if stop in query.lower():
                print("Siri: Ok sir, see you soon again")
                say("Ok sir, see you soon again")
                end = True
                break
        if end: break
        sites = [["youtube", "https://youtube.com"],
                 ["wikipedia", "https://wikipedia.com"],
                 ["udemy", "https://udemy.com"],
                 ["facebook", "https://facebook.com"],
                 ["instagram", "https://instagram.com"],
                 ["google", "https://google.com"]]
        for site in sites:
            if site[0] in query.lower():
                print(f"Siri: Opening {site[0]} sir!...\n")
                say(f"Opening {site[0]} sir!...")
                webbrowser.open_new(site[1])
                continue
        if "music" in query.lower() or "play" in query.lower():
            musicPath = "/Users/amit/Downloads/Brown-Munde.mp3"
            print("Siri: Playing music!")
            say("Playing music!")
            os.system(f"open {musicPath}")
            continue

        # todo: Add more applications
        apps = [["game", "Asphalt8"],
                ["facetime", "FaceTime"],
                ["clock", "Clock"]]
        for app in apps:
            if app[0] in query.lower():
                print(f"Siri: Opening {app[1]} sir!")
                say(f"Opening {app[1]} sir!")
                os.system(f"open /Applications/{app[1]}.app")
                end = True
                continue
        if end:
            break
        apps = [["facetime", "FaceTime"],
                ["clock", "Clock"]]
        for app in apps:
            if app[0] in query.lower():
                print(f"Siri: Opening {app[1]} sir!")
                say(f"Opening {app[1]} sir!")
                os.system(f"open /System/Applications/{app[1]}.app")
                continue

        if "time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Siri: Sir the time is {strfTime}")
            os.system(f"say Sir the time is {strfTime}")
            continue

        result = chat(query)
        if (result == ""):
            print("Siri: Some error occurred!")
            say("Some error occurred!")
        else:
            print(f"Siri: {result}")
            say(result)





