import json
from voice import listen
import os
import webbrowser

# Load commands
with open("commands.json", "r") as f:
    commands = json.load(f)

while True:
    command = listen()

    if command == "exit":
        break

    if command in commands:
        for action in commands[command]:

            if action["type"] == "app":
                os.startfile(action["path"])
            elif action["type"] == "website":
                webbrowser.open(action["url"])

    else:
        print("Command not found.")