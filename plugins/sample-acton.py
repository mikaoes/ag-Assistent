class actOnApp:
    def __init__(self):
        self.running = False
        self.prev = None

    def __call__(self, arg_list):
        result = 0.0
        for i in arg_list:
            result += float(i)
        if result != "close":
            self.running = True
        else:
            self.running = False
        return result
        


object = actOnApp()
commands = {
    "actOnApp _*_": object,
    "twoOnApp _*_": object
    }