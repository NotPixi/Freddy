from assistant.loader import load_commands
from assistant.tts import speak
from assistant.speech import listen
from assistant.executor import execute
from assistant.parser import parse
def main():
    commands = load_commands()

        
    while True:
        command = listen()
        
        if command is None:
            speak("Say it clear idiot!")
        else:
            print(command)
            parsed = parse(command)
            execute(parsed , commands)

if __name__ == "__main__":
    main()