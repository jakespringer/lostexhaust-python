import hashlib
import string
import random
import sys

salt = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
string = sys.argv[1]
hash_object = hashlib.sha512(string + salt)
hex_dig = hash_object.hexdigest()
print("Salt: " + salt)
print("Hash: " + hex_dig)
