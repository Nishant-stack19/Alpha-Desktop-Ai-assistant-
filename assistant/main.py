import os
import win32com.client as win32
import speech_recognition as sr
import pyttsx3 as pyt
import openai as ai

# Initialize the speech recognizer
# speaker = win32.Dispatch("SAPI.SpVoice")
# while 1:
#     print("Listening for commands...")
#     s = input("Enter command: ")
#     speaker.Speak(s)
def speak(text):
    engine = pyt.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        # r.praise_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry, I did not understand that. Please try again."

if __name__ == "__main__":
    listen = True
    print("Starting speech recognition...")
    speak("thsi is alpha ai assistant")
    speak("Hello sir, How can i help you today?")
    while True:
        if listen:
            print("Listening for commands...")
            query = take_command()
            if "wait" in query.lower() or "stop" in query.lower():
                print("Stopping listening mode...")
                speak("OK, I will stop listen You can enable it again by saying 'listen'.")
                listen = False
            elif "open " in query.lower():
                site_name = query.lower().replace("open ", "")
                url = f"https://{site_name}.com"
                os.system(f"start {url}")
                speak(f"Opening {site_name} website.")
            elif "search" in query.lower():
                search_query = query.lower().replace("search ", "")
                url = f"https://www.google.com/search?q={search_query}"
                os.system(f"start {url}")
                speak(f"Searching for {search_query} on Google.")
            elif "exit" in query.lower():
                speak("goodbye sir! have a nice day")
                break
            elif "play music" in query.lower():
                url = "https://open.spotify.com/user/31grw6pk3dwbyc3mluuc6rfjxbzi?si=49ebe4603c744a03"
                os.system(f"start {url}")
                speak("Playing music on Spotify.")
            else:
                speak("Sorry, sir i did not understand that command.")
        else:
            print("waiting for your command...")
            query = take_command()
            if "listen" in query.lower():
                print("Enabling listening mode...")
                speak("OK, what do you want me to do?")
                listening = True
            elif "exit" in query.lower():
                speak("goodbye sir! have a nice day")
                break