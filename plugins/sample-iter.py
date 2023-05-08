def greet(name):
    return f"Hallo {name}!"

def gruesse_von_an(von, an):
    return f"Grüße von {von} an {an}!"

class funcApp:
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
        return "works"
    def f1(self):
        return "works as well"
        
        


commands = {
    "greet _": greet,
    "gruesse von _ an _": gruesse_von_an,
    "funcApp": funcApp()
    }