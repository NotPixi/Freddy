
from assistant.loader import load_commands
from assistant.tts import speak
from assistant.speech import listen
def main():
    command = listen()

    if command is None :
        speak("Sorry, I didn't catch that.")
    else:
        speak(command)


if __name__ == "__main__":
    main()