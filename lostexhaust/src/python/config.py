import json
import os

config = dict()

def loadConfig(filename):
    # normalize the filename
    filename = os.path.abspath(filename)
    if filename in config:
        return config[filename]
    else:
        with open(filename, "r") as configFile:
            config[filename] = json.loads(configFile.read())
            return config[filename]
