import os

# create a list of every subfolder in the plugin directory

path = os.path.join(os.path.dirname(os.path.realpath(__file__)).replace("/core/cli", ""), 'plugins') # needs to be changed

print(path)

plugins = os.listdir(path)
print(plugins)

# create a list of commands for every plugin

commands = []

for plugin in plugins:
    if plugin == "__pycache__" or plugin == "__init__.py": continue
    plugin = plugin.replace(".py", "")
    commands.append([plugin, ])