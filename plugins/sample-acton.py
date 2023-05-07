class actOnApp:
    def __init__(self):
        self.running = False

    def __call__(self, arg):
        return f"actOnApp was called with {arg}"
    

commands = {
    "actOnApp _": actOnApp()
    }