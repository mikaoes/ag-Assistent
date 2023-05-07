print("core imported")

import os
import types
if __name__ == "__main__":
    print("core is main")
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plugins
com_list = plugins.command_list()



def command_pal(r): # command palette for system commands
    match r:
        case "exit": exit()
        case "clear": os.system("clear"); return True, None
        case "cls": os.system("cls"); return True, None
        case "help" | "?": return True, "See help at help.md"
        case "list" : return True, com_list
        case _: return False, None

def args(dc, r_split):
    s = list(dc.keys())[0]
    s_split = s.split(" ")
    usc_pos = [i for i, v in enumerate(s_split) if v == "_"]
    arglist = [v for i, v in enumerate(r_split) if i in usc_pos]
    return(arglist)

def plugin_commands(r):
    d = com_list.copy()
    r_split = r.split(" ")
    for i, v in enumerate(r_split):
        for j in com_list:
            j_split = j.split(" ")
            try:
                if j_split[i] != v and j_split[i] != "_":
                    try:
                        del d[j]
                    except KeyError:
                        None
            except IndexError:
                None

    match len(d):
        case 0: return "Command not found."
        case 1: return d[list( d.keys())[0]](  *args(d, r_split)  )
        case _: return "Multiple commands found."
            

os.system("clear") # initial clear

def loop():
    while True:
        r = input(">>> ")
        a = request(r)
        a != None and print(a)

def request(r):
    a = command_pal(r)
    if a[0]: # if is system command
        return a[1]
    else:
        return plugin_commands(r)

    
if __name__ == "__main__":
    loop()