# GrowthPurple Company Task Assignment
Speech to Speech Voice assistant using Python Using Local LLM(Large Language Models)

Working demos:
https://drive.google.com/drive/folders/1EX4Enz-yZgP-DpcWRbgNGRmHfTSaCOPe?usp=sharing

Overview:

This project involves creating a voice assistant named "Andy" using Python. The assistant listens for voice commands, processes them using a local large language model (LLM), and responds with appropriate actions. Key functionalities include adding tasks, listing tasks, taking screenshots, opening web pages, and answering questions using the LLM.

Prerequisites:

Ensure the following installed on the system:

Python 3.7 or higher
A local LLM (e.g., GPT-4 model) **** we used this model
Microphone for voice input
Speakers for voice output (or a text-to-speech engine)

Required Modules:

os: For interacting with the operating system.
speech_recognition: For recognizing speech input from the microphone.
gpt4all: For using a local LLM.
sys: For system-specific parameters and functions.
whisper: For transcribing audio files.
warnings: To manage warning messages.
time: For time-related functions.
pyautogui: For GUI automation (e.g., taking screenshots).
webbrowser: For opening web pages.
pyttsx3: For text-to-speech conversion (Windows and Linux).

Installing Required Modules:

Use the following pip commands to install the required modules:
pip install SpeechRecognition
pip install gpt4all
pip install openai-whisper
pip install pyautogui
pip install pyttsx3

Steps to Run the Assistant:

Set up the Local LLM: Download and place your local model file in the appropriate directory.
Modify the Path: Update the model = GPT4All("/path/to/your/local/model", allow_download=False) line with the correct path to your model file.
Run the Script: Execute the script using Python.

Usage:

The assistant listens for commands and performs actions such as adding tasks, listing tasks, taking screenshots, opening a web browser, and answering questions.
Speak clearly into the microphone and wait for the assistant to respond.
To exit, say "exit".

Conclusion:

This document provides a comprehensive guide to setting up and running a Speech-to-Speech Voice Assistant using Python and a local LLM. Ensure all dependencies are installed and correctly configured to enable seamless functionality. Enjoy interacting with your personalized voice assistant!

