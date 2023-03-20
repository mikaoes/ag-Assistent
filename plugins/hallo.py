def greet(name):
    return f"Hallo {name}!"

def gruesse_von_an(von, an):
    return f"Grüße von {von} an {an}!"

commands = {
    "greet _": greet,
    "gruesse von _ an _": gruesse_von_an
    }