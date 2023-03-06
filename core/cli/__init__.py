import os

print("main_loop imported")
import core.cli.plugin_import
plugin_import.hallo.greet()

def commands(r): # command palette for system commands
    r == "exit" and exit()
    if r == "clear" : os.system("clear"); return True
    if r == "cls" : os.system("cls"); return True
    if r == "help" : print("See help at: help.md"); return True

#os.system("clear") # first clear after import log messages

def start():
    while True:
        request = input(">>> ")
        print("You said: " + request)
        if commands(request): continue
        print("Command not found")