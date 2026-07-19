import os
from assistant.tts import speak


def execute(command, commands):

    for app in commands:

        if app in command:
            os.startfile(commands[app])
            speak("Opening "+ app)
            return

    speak("Give me the path first idiot!")