from os import system
import speech_recognition as sr
from gpt4all import GPT4All
import sys
import whisper
import warnings
warnings.filterwarnings("ignore")
import time
import pyautogui
import webbrowser
import os

# Initialize the local LLM
model = GPT4All("/path/to/your/local/model", allow_download=False)
assistant_name = "andy"
listening_for_trigger_word = True
should_run = True
source = sr.Microphone()
recognizer = sr.Recognizer()
base_model_path = os.path.expanduser('~/.cache/whisper/tiny.pt')
base_model = whisper.load_model(base_model_path)

# Initialize text-to-speech engine for non-macOS systems
if sys.platform != 'darwin':
    import pyttsx3
    engine = pyttsx3.init() 

tasks = []
listeningToTask = False
askingAQuestion = False

def respond(text):
    """Convert text to speech."""
    if sys.platform == 'darwin':
        ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
        clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
        system(f"say '{clean_text}'")
    else:
        engine.say(text)
        engine.runAndWait()

def listen_for_command():
    """Listen for voice commands and transcribe them."""
    with source as s:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        with open("command.wav", "wb") as f:
            f.write(audio.get_wav_data())
        command = base_model.transcribe("command.wav")
        if command and command['text']:
            print("You said:", command['text'])
            return command['text'].lower()
        return None
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def perform_command(command):
    """Perform actions based on the transcribed command."""
    global tasks
    global listeningToTask
    global askingAQuestion
    global should_run
    global listening_for_trigger_word
    if command:
        print("Command: ", command)
        if listeningToTask:
            tasks.append(command)
            listeningToTask = False
            respond(f"Adding {command} to your task list. You have {len(tasks)} tasks currently in your list.")
        elif "add a task" in command:
            listeningToTask = True
            respond("Sure, what is the task?")
        elif "list tasks" in command:
            respond("Sure. Your tasks are:")
            for task in tasks:
                respond(task)
        elif "take a screenshot" in command:
            pyautogui.screenshot("screenshot.png")
            respond("I took a screenshot for you.")
        elif "open chrome" in command:
            respond("Opening Chrome.")
            webbrowser.open("http://www.google.com/")
        elif "ask a question" in command:
            askingAQuestion = True
            respond("What's your question?")
            return
        elif askingAQuestion:
            askingAQuestion = False
            respond("Thinking...")
            print("User command: ", command)
            output = model.generate(command, max_tokens=200)
            print("Output: ", output)
            respond(output)
        elif "exit" in command:
            should_run = False
        else:
            respond("Sorry, I'm not sure how to handle that command.")
    listening_for_trigger_word = True

def main():
    """Main loop to keep the assistant running."""
    global listening_for_trigger_word
    while should_run:
        command = listen_for_command()
        if listening_for_trigger_word:
            listening_for_trigger_word = False
        else:
            perform_command(command)
        time.sleep(1)
    respond("Goodbye.")

if __name__ == "__main__":
    main()
