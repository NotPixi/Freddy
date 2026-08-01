import os
from assistant.tts import speak


def execute(parsed, commands):

        target = parsed["target"]
        if target in commands:
            os.startfile(commands[target])
            speak("Opening "+ target)
            return
        else:
            speak("Give me the path first idiot!")