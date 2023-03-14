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
        case _: return False, None

def args(dc, r_split):
    s = list(dc.keys())[0]
    s_split = s.split(" ")
    usc_pos = [i for i, v in enumerate(s_split) if v == "_"]
    arglist = [v for i, v in enumerate(r_split) if i in usc_pos]
    print(arglist)
    return(arglist)

def find_command(r):
    d = dict()
    r_split = r.split(" ")
    for i, v in enumerate(r_split):
        for j in com_list:
            j_split = j.split(" ")
            try:
                if j_split[i] == v or j_split[i] == "_":
                    d.update({j: com_list[j]})
                else:
                    d.pop(j, "not found")
            except IndexError:
                d.pop(j, "not found")
            


    match len(d):
        case 0: return "Command not found."
        case 1: return d[list(d.keys())[0]](*args(d, r_split))
        case _: return "Multiple commands found."
            
    

def plugin_commands(r): # commands from plugins
    com, arg = r.split(" ", 1)
    if com in com_list:
        return True, (com_list[com](arg))
    else:
        return False, None


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

print(find_command(input(">>> ")))
exit()