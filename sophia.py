import speech_recognition as sr
import webbrowser
import sounddevice as sd
import soundfile as sf
import pyttsx3
import tempfile
import pywhatkit
import time
import pyautogui
import re

# ================= SETTINGS =================
WAKE_WORD = "alexa"
LISTEN_SECONDS = 5

# ================= VOICE (Female) =================
engine = pyttsx3.init()
for v in engine.getProperty("voices"):
    if "zira" in v.name.lower():
        engine.setProperty("voice", v.id)
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ================= LISTEN (SoundDevice) =================
r = sr.Recognizer()

def listen():
    fs = 44100
    rec = sd.rec(int(LISTEN_SECONDS * fs), samplerate=fs, channels=1)
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, rec, fs)
        path = f.name

    with sr.AudioFile(path) as src:
        audio = r.record(src)
    
    try:
        # Recognize Tamil + English
        return r.recognize_google(audio, language='ta-IN')
    except:
        return ""


# ================= CLEAN COMMAND =================
def extract_song(text):
    remove = [
        WAKE_WORD, "play", "song",
        "podu", "pannu", "paatu", "pattu"
    ]
    for w in remove:
        text = text.replace(w, "")
    return text.strip()

# ================= YOUTUBE AUTO PLAY =================
def play_youtube(song):
    speak(f"{song} play panren")
    pywhatkit.playonyt(song)
    time.sleep(5)  # browser load time


def skip_ad():
    time.sleep(0.5)          # small delay
    pyautogui.press("tab")
    time.sleep(0.3)
    pyautogui.press("tab")
    time.sleep(0.3)
    pyautogui.press("tab")
    time.sleep(0.3)
    pyautogui.press("enter")
def open_second_site_keyboard():
    time.sleep(4)          # Google results load time

def tab_press(n=1, delay=0.3):
    for _ in range(n):
        pyautogui.press("tab")
        time.sleep(delay)

# ENTER press
def enter_press():
    pyautogui.press("enter")
    time.sleep(0.2)

# Open nth link dynamically (any number of links)
def open_link_infinity(n):
    """
    n = 1 for first link, 2 for second link, ...
    """
    if n < 1: n = 1
    time.sleep(3)  # wait for page load
    tab_press(n + 1)  # +1 initial focus
    enter_press()

def extract_search(text):
    for w in [WAKE_WORD, "search", "google", "find", "thedu"]:
        text = text.replace(w, "")
        return text.strip()




# ================= KEY CONTROLS =================
def press_key(key):
    pyautogui.press(key)



def press_keys(key):
    pyautogui.hotkey(key)


# ================= MAIN =================
speak("Alexa ready")

while True:
    cmd = listen()
    print("Heard:", cmd)

    # 🔴 Minimise
    if cmd.strip() == "minimise":
        press_key("i")

    # 🔴 Backward
    elif cmd.strip() == "backward":
        press_key("j")

    # 🔴 Play / Pause
    elif "stop" in cmd or "resume" in cmd:
        press_key("k")

    # 🔴 Forward
    elif cmd.strip() == "forward":
        press_key("l")

    # 🔴 Mute
    elif cmd.strip() == "mute":
        press_key("m")

    # 🔴 Volume up
    elif "volume up" in cmd or "sound increase pannu" in cmd:
        press_key("up")

    # 🔴 Volume down
    elif "volume down" in cmd or "sound decrease pannu" in cmd:
        press_key("down")

    # 🔴 Fullscreen
    elif "full screen" in cmd or "fullscreen" in cmd:
        press_key("f")
    elif "tab" in cmd :
        press_key("tab")
    elif "enter" in cmd :
        press_key("enter")
    elif "escape" in cmd :
        press_key("esc")
    elif "next" in cmd :
        pyautogui.hotkey("shift", "n")
    elif "previous" in cmd :
        pyautogui.hotkey("alt", "left")
    elif "skip ad" in cmd or "remove ad" in cmd:
        skip_ad()
    elif "open google" in cmd or "google open" in cmd:
        webbrowser.open("https://www.google.com")
        time.sleep(2)
        pyautogui.hotkey("win", "right")

    elif "open link" in cmd:
        import re
        match = re.search(r'\b(\d+)\b', cmd)
        if match:
            number = int(match.group(1))
        else:
            number = 1 
        speak(f"{number} link open panren")
        open_link_infinity(number)
    elif "back" in cmd:
        pyautogui.hotkey("alt","left")

    elif "search" in cmd:
        query = extract_search(cmd)
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            time.sleep(2)
            
    elif "open hotstar" in cmd or "hotstar open" in cmd:
        # extract show/movie name
        show = extract_song(cmd)  # reuse song extraction function
        speak("Hotstar open panren")
        webbrowser.open("https://www.hotstar.com/in")
        time.sleep(5)  # wait for site load

        if show:
            speak(f"{show} play panren")
            # search Hotstar site for the show
            query = show.replace(" ", "+")
            webbrowser.open(f"https://www.hotstar.com/in/search?q={query}")
            time.sleep(5)
            # press first link + enter
            pyautogui.press("tab", presses=3, interval=0.3)  # adjust tabs if needed
            pyautogui.press("enter")

    # 🔴 Play song
    elif WAKE_WORD in cmd:
        song = extract_song(cmd)
        if song:
            play_youtube(song)





