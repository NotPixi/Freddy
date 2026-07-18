import json

COMMANDS_FILE = "config/commands.json"

def load_json(path):
    """Load and return data from a JSON file."""

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find '{path}'.")
    
def load_commands():
    return load_json(COMMANDS_FILE)