print("core imported")

import os
import types
if __name__ == "__main__":
    print("core is main")
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plugins
com_list = plugins.command_list()
running = [False, None] # bool, object


def command_pal(r): # command palette for system commands
    match r:
        case "exit": exit()
        case "close": running[0] = False; return True, None
        case "clear": os.system("clear"); return True, None
        case "cls": os.system("cls"); return True, None
        case "help" | "?": return True, "See help at help.md"
        case "list" : return True, com_list
        case _: return False, None

def args(dc, r_split):
    s = list(dc.keys())[0]
    s_split = s.split(" ")
    
    usc_pos = [i for i, v in enumerate(s_split) if v == "_" or v == "_*_"]
    arglist = [v for i, v in enumerate(r_split) if i in usc_pos]
    return(arglist)

def plugin_commands(r):
    d = com_list.copy()
    r_split = r.split(" ")
    for i, v in enumerate(r_split): # split input string and enumerate (index, value)
        for j in com_list: # iterate through command list
            j_split = j.split(" ") # split command string
            try:
                if j_split[i] != v and j_split[i] != "_" and j_split[i] != "_*_":
                    try:
                        del d[j]
                    except KeyError:
                        None
            except IndexError:
                None

    def class_runner(c):
        nonlocal d, r_split
        try:
            r = c( args(d, r_split) )
        except:
            r = c()
        if isinstance(c, object):
            try:
                global running
                running[0] = c.running
                running[1] = c
            except:
                None
        return r

    match len(d):
        case 0: return "Command not found."
        case 1: return class_runner(d[list(d.keys())[0]])
        case _: return "Multiple commands found."



os.system("clear") # initial clear

def loop():
    while True:
        global running
        input_string = ">>> "
        if running[0]:
            try:
                input_string = f"({running[1].name}) >>> "
            except:
                None
        else:
            input_string = ">>> "
        r = input(input_string)
        a = request(r)
        a != None and print(a)

def request(r):
    global running
    a = command_pal(r)
    if a[0]: # if is system command
        return a[1]
    elif running[0] == False:
        return plugin_commands(r)
    elif running[0] == True:
        c = running[1]
        ret = c(r.split(" "))
        if isinstance(c, object):
            try:
                running[0] = c.running
                running[1] = c
            except:
                None
        return ret

    
if __name__ == "__main__":
    loop()