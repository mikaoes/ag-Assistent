def greet(name):
    return f"Hallo {name[0]}!"

def gruesse_von_an(namen):
    return f"Grüße an {namen[1]} von {namen[0]}!"

class wechselApp:
    def __init__(self):
        self.c = 0
        self.lim = 2
    def __call__(self):
        f_name = "f" + str(self.c)
        method = getattr(self, f_name)
        self.c += 1
        self.c == self.lim and self.reset()
        return str(method())
    def reset(self):
        self.c = 0
    def f0(self):
        return "function 1"
    def f1(self):
        return "function 2"
        
        


commands = {
    "greet _": greet,
    "gruesse von _ an _": gruesse_von_an,
    "wechselApp": wechselApp()
    }