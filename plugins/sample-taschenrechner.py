class rechner:
    def __init__(self):
        self.running = True
        self.name = "Taschenrechner"

    def __call__(self, arg_list):
        match len(arg_list):
            case 3:
                return self.rechenaufgabe(arg_list)
    def rechenaufgabe(self, arg_list):
        vorzeichen = arg_list[1]
        result = 0.0
        match vorzeichen:
            case "+":
                result = float(arg_list[0]) + float(arg_list[2])
            case "-":
                result = float(arg_list[0]) - float(arg_list[2])
            case "*":
                result = float(arg_list[0]) * float(arg_list[2])
            case "/":
                result = float(arg_list[0]) / float(arg_list[2])
        return result
        


object = rechner()
commands = {
    "rechner _*_": object,
    "taschenrechner _*_": object
    }