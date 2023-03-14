def greet(name, name2="zwo"):
    return f"Hello, {name} and {name2}!"

def gruesse_von_an(von, an):
    return f"Grüße von {von} an {an}!"

commands = {
    "greet _": greet,
    "gruesse von _ an _": gruesse_von_an}