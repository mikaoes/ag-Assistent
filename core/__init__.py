print("core imported")

import os
import types
if __name__ == "__main__":
    print("core is main")
    # import package from sibling directory
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

mode = False # mode for app runner
d_obj = None # object for app runner

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
            
    def diff_returner() -> tuple[bool, str]:
        nonlocal d
        ret_bool, ret_str_or_class = None, None
        # if d is function / is class
        if callable(d[list(d.keys())[0]]):
            ret_bool, ret_str_or_class = True, d[list(d.keys())[0]](*args(d, r_split))
        else:
            ret_bool, ret_str_or_class = False, d[list(d.keys())[0]]
        return ret_bool, ret_str_or_class

    match len(d):
        case 0: return True, "Command not found.1"
        case 1: return diff_returner()        #True, str(d[list(d.keys())[0]](*args(d, r_split)))
        case _: return True, "Multiple commands found."
            


def app_runner(do, r):
    print(f"recieved {do} and {r} with type {type(r)}")

os.system("clear") # first clear after import log messages

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
        ap = plugin_commands(r)
        if ap[0]: # if is command
            return ap[1]
        else:
            return str(ap[1])


    
if __name__ == "__main__":
    loop()