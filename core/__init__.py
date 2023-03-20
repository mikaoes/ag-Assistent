print("core imported")

import os
if __name__ == "__main__":
    print("core is main")
else:
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
        case 0: return False, "Command not found."
        case 1: return True, d[list(d.keys())[0]](*args(d, r_split))
        case _: return False, "Multiple commands found."
            


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
        a = request(r)
        a != None and print(a)

def request(r):
    a = command_pal(r)
    if a[0]:
        return a[1]
    else:
        ap = plugin_commands(r)
        if ap[0]:
            return ap[1]
        else:
            return "Command not found."
    
if __name__ == "__main__":
    loop()