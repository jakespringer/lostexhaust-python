import hashlib
import txt_util

passwords = None

def checkPassword(username, password):
    global passwords
    if passwords == None:
        with open("../../../res/example/users.txt") as f:
            passwords = txt_util.parseTxt(f.read())
    for i in range(0, len(passwords)):
        if passwords[i]["username"] == username:
            salt = passwords[i]["salt"]
            hash_object = hashlib.sha512(password + salt)
            hex_dig = hash_object.hexdigest()
            if str(hex_dig) == passwords[i]["password_hash"]:
                return True
    return False

import sys

username = sys.argv[1]
password = sys.argv[2]
print(username+":"+password + " resulted in "+str(checkPassword(username, password)))
