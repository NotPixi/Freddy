from assistant.loader import load_commands
from assistant.tts import speak
from assistant.speech import listen
from assistant.executor import execute
def main():
    commands = load_commands()

        
    while True:
        command = listen()
        
        if command is None:
            speak("Say it clear idiot!")
        else:
            print(command)
            execute(command , commands)

if __name__ == "__main__":
    main()