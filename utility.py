#Some utilities for this software
import speech_recognition as sr
import os

def say(text):
    clean_text = sanitize_text(text.replace('\n', ' ').strip())
    os.system(f"say {clean_text}")

def sanitize_text(text):
    # Remove special characters
    sanitized_text = ''.join(c for c in text if c.isalnum() or c.isspace())
    return sanitized_text

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            #print("Recognising...")
            query = r.recognize_google(audio, language="en-in")
            #print(f"User said: {query}")
            return query
        except Exception as e:
            return ""