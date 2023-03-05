import os

# create a list of every subfolder in the plugin directory

path = os.path.join(os.path.dirname(os.path.realpath(__file__)).replace("/core/cli", ""), 'plugins') # needs to be changed

print(path)

plugins = os.listdir(path)