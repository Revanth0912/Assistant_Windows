# Assistant_Windows

---

````markdown
# 🗣️ Windows Voice Assistant (AssistantBot)

An intelligent, voice-controlled assistant built in Python for Windows. AssistantBot performs desktop-level tasks through
voice commands — including launching applications, adjusting volume, fetching date/time, taking screenshots,searching the web,
and more — using natural speech input.

---

## 🚀 Features

- 🎙️ **Speech Recognition** — Trigger actions by speaking commands prefixed with “Assistant”
- 🧠 **Contextual Replies** — Friendly responses to greetings and small talk
- 📂 **App Launcher** — Opens apps like Chrome, Notepad, File Explorer, Spotify
- 🔊 **Volume Control** — Adjust system volume using numeric voice input
- 📸 **Screenshot Capture** — Captures and saves the current screen with a single command
- 🌐 **Web Search** — Automatically searches Google if no match found
- 🕒 **Tells Time & Date** — Fetches the current system time and date
- 🪟 **Minimize All Windows** — Minimizes all windows instantly via voice
- 🖥️ **Works Offline (mostly)** — Doesn’t require continuous internet, except for speech recognition

---

## 🧪 Example Commands

| Voice Command                     | Action                                     |
|----------------------------------|--------------------------------------------|
| `Assistant open Chrome`          | Launches Google Chrome                     |
| `Assistant take a screenshot`    | Saves screenshot to Pictures/Screenshots   |
| `Assistant what's the time?`     | Speaks the current time                    |
| `Assistant set volume to 50`     | Adjusts volume to 50%                      |
| `Assistant minimize all windows` | Minimizes all open windows                 |
| `Assistant open notepad`         | Launches Notepad                           |
| `Assistant search palm fruit AI` | Searches Google with the given query       |

---

## 🛠️ Tech Stack

- 🐍 **Python 3**
- 🎤 `speech_recognition` – Voice input
- 🔈 `pyttsx3` – Offline text-to-speech (TTS)
- 🧠 `pyautogui` – Screenshots and automation
- 🪟 `subprocess`, `psutil`, `ctypes` – App control and Windows integration
- 🌍 `webbrowser` – Google search fallback

---

## 📂 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Revanth0912/Assistant_Windows/blob/main/Assistant_bot.py
   cd WindowsVoiceAssistant
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Download **nircmd** and add it to PATH if you want volume control to work:

   * [Download nircmd](https://www.nirsoft.net/utils/nircmd.html)

4. Run the assistant:

   ```bash
   python assistant.py
   ```

---

## ⚙️ Configuration Notes

* Uses `Google Speech Recognition` (requires temporary internet access)
* Volume control requires `nircmd.exe` to be installed and added to system PATH
* Make sure your microphone is working and permissions are enabled

---

## 🧠 Future Enhancements

* Add more apps to launch dynamically
* Add personalized assistant name setting
* Include offline NLP for command understanding
* Multi-language voice support and command training

---

## 📸 Demo

> *Coming Soon: Screen recording or GIF of the assistant in action.*

---

## 📧 Contact

* 👨‍💻 M Revanth Reddy
* 📫 [revanthmatoori09@gmail.com](mailto:revanthmatoori09@gmail.com)
* 🔗 [LinkedIn](https://www.linkedin.com/in/m-revanthreddy/)
* 🌐 [GitHub](https://github.com/Revanth0912)

---

⭐ *“Designed to bridge voice and system automation — hands-free, context-aware desktop control made simple.”*



