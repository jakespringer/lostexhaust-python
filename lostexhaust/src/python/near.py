from templite import Templite
from os import path
import config

class Near:
    def get(self):
        conf = config.loadConfig("../../conf/sample_config.json")
        t = Templite(filename=path.join(conf["projectRoot"], "src", "html", "near.templite"))
        return t.render()
