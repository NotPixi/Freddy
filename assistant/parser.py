

def parse(command):
    words = command.split()
    action = words[0]
    target = " ".join(words[1:])

    return{
        "action" : action,
        "target" : target
    }