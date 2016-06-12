
class Config:
    def __init__(self, projectRoot):
        self.projectRoot = projectRoot

def loadConfig(filename):
    return Config("/Users/jake/Development/lostexhaust-python/lostexhaust")
