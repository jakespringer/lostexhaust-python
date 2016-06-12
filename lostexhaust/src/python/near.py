from page import Page
from templite import Templite
from os import path

import config

class Near(Page):
    def get(self):
        conf = config.loadConfig("../../conf/config.json")
        t = Templite(filename=path.join(conf.projectRoot, "src", "html", "near.templite"))
        return t.render()
