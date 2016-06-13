import re

newline = re.compile("\\r")
tabs = re.compile("\\t")

class DataTxtImpl:
    def __init__(self):
        pass

def parseTxt(txt):
    lines = newline.split(txt)
    if len(lines) > 0:
        names = tabs.split(lines[0])
    else:
        return None
    parsedData = []
    for i in range(1, len(lines)):
        tokens = tabs.split(lines[i])
        if len(tokens) == len(names):
            parsedLine = dict()
            for j in range(0, len(tokens)):
                parsedLine[str(names[j])] = tokens[j]
            parsedData.append(parsedLine)
        elif len(tokens) != 1:
            return None
    return parsedData

with open("../../../res/example/relationships.txt") as file:
    print(str(parseTxt(file.read())))
