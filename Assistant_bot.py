import random
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import psutil 
import ctypes  # For controlling brightness on Windows

recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()


responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I assist you today?"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "what's your name": ["You can call me AssistantBot.", "I'm AssistantBot, nice to meet you!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                       "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!"],
    "quit": ["Bye! Take care.", "Goodbye! Have a great day!"],
    "exit": ["Bye! Take care.", "Goodbye! Have a great day!"]
}

def generate_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            response = random.choice(responses[key])
            speak(response)
            return response

    app_commands = {
        "chrome": "chrome",
        "notepad": "notepad",
        "spotify": "spotify",
        "file explorer": "explorer.exe",
    }
    for app_name, command in app_commands.items():
        if app_name in user_input:
            try:
                subprocess.Popen([command], shell=True) 
                speak(f"Opening {app_name}.")
                return f"Opening {app_name}."
            except FileNotFoundError:
                search_in_powershell(app_name)
                return f"Application {app_name} not found locally. Searching in PowerShell."

    if "volume" in user_input:
        change_volume(user_input)
        return "Volume changed."

    search_url = "https://www.google.com/search?q=" + user_input
    webbrowser.open_new_tab(search_url)
    speak("I've searched the web for you.")
    return "I've searched the web for you."

def search_in_powershell(app_name):
    powershell_command = f"Get-AppxPackage *{app_name}* | Select-Object -Property PackageFullName"
    result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
    if result.stdout:
        speak(f"{app_name} found in PowerShell.")
        print(result.stdout)
    else:
        speak(f"Sorry, I couldn't find {app_name} in PowerShell.")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            return user_input.lower()
        except sr.WaitTimeoutError:
            print("No speech detected. Waiting for command...")
            return None
        except sr.UnknownValueError:
            print("Unable to recognize speech. Waiting for command...")
            return None

def speak(text, language='en'):
    synthesizer.setProperty('voice', language)
    synthesizer.say(text)
    synthesizer.runAndWait()

def close_application(app_name):
    for proc in psutil.process_iter():
        if proc.name() == app_name + ".exe":
            proc.terminate()

def change_volume(user_input):
    # Split user input by spaces and iterate over each word
    words = user_input.split()
    for i, word in enumerate(words):
        # Check if the word is numeric
        if word.isdigit():
            # Extract volume value from the numeric word and set volume using system command
            volume_value = int(word)
            volume_value = max(0, min(100, volume_value))  # Ensure volume value is within 0-100
            subprocess.run(["nircmd", "setsysvolume", str(volume_value * 655.35)])  # Change volume using nircmd
            return
    # If no numeric value found after "volume", notify the user
    speak("Please specify a valid volume level after 'volume'.")

def minimize_all_windows():
    # Use the Windows API to minimize all windows
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)  # Minimize console window
    ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)  # Press the Windows key
    ctypes.windll.user32.keybd_event(0x4D, 0, 0, 0)  # Press the 'M' key
    ctypes.windll.user32.keybd_event(0x4D, 0, 2, 0)  # Release the 'M' key
    ctypes.windll.user32.keybd_event(0x5B, 0, 2, 0)  # Release the Windows key


def interact():
    speak("Welcome! I'm AssistantBot, your friendly assistant. How can I assist you today?")
    while True:
        user_input = listen()
        if user_input is not None:
            if user_input.lower() == "minimize all windows" or user_input.lower() == "minimise all windows":
                minimize_all_windows()
                speak("Minimized all windows.")
            elif user_input.lower().startswith("change language to"):
                language = user_input.lower().split("change language to ")[1].strip()
                if language in ['en', 'es', 'fr']:  # Add more languages as needed
                    speak(f"Language changed to {language}.", language)
                else:
                    speak("Sorry, I don't support that language.")
            else:
                response = generate_response(user_input)
                print("AssistantBot:", response)
                if user_input.lower() == "quit" or user_input.lower() == "exit":
                    break
engine = pyttsx3.init()
engine.say(interact)
engine.runAndWait()

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

interact()
