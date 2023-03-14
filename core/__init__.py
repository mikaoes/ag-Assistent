import os

print("core imported")


def commands(r): # command palette for system commands
    match r:
        case "exit": exit()
        case "clear": os.system("clear"); return True, None
        case "cls": os.system("cls"); return True, None
        case "help": return True, "See help at help.md"
        case _: return False, None

os.system("clear") # first clear after import log messages

def loop():
    while True:
        r = input(">>> ")
        print(request(r))

def request(r):
    if commands(r)[0]:
        return commands(r)[1]
    else:
        return "unknown command"