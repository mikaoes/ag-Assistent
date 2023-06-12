# import every plugin in the plugins folder
import os
import importlib

def command_list():
    d = dict()
    for i in os.listdir("plugins"):
        if i.endswith(".py") and i != "__init__.py" and not i.startswith("piig00"):
            # import "commands" dictionary from plugin
            from_path = "plugins." + i[:-3]
            c = importlib.import_module(from_path)
            d.update(c.commands)
    return d