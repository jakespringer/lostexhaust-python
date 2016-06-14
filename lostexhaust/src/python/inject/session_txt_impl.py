import sys
import os
sys.path.append(os.path.abspath("../"))
import config
import time
import re
from cryptography.fernet import Fernet

class SessionTxtImpl:
    def __init__(self):
        self.conf = config.loadConfig("../../conf/example_config.json")
        self.fernet = Fernet(str(self.conf["fernetSessionKey"]))
        self.tokenCheck = re.compile(r"^[0-9]+\|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\|[0-9]+$")
        self.pipe = re.compile(r"\|")

    def checkAndParseToken(self, token, maxTime, ip):
        sessionId = self.fernet.decrypt(token)
        if self.tokenCheck.match(sessionId):
            elements = self.pipe.split(sessionId)
            (oldId, oldIp, oldTime) = (int(elements[0]), elements[1], int(elements[2]))
            if (int(time.time()) - oldTime < maxTime) and (oldIp == ip):
                return (oldId, oldIp, oldTime)
        return None

    def generateToken(self, id, ip):
        time_str = str(int(time.time()))
        id_str = str(id)
        ip_str = str(ip)
        return self.fernet.encrypt(id_str + "|" + ip_str + "|" + time_str)
