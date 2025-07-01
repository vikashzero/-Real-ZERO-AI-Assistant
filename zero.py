import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

speak("Hello, I am ZERO. How can I help you?")
while True:
    command = take_command()
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        break
    elif command != "":
        speak("You said: " + command)
