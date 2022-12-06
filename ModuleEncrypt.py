
from cryptography.fernet import Fernet
from generate_key import write_key
from load_key     import load_key
from Encrypt import encrypt

# uncomment this if it's the first time you run the code, to generate the key
write_key()

# file name
file = "sample3.txt"

# load the key
key = load_key()
# encrypt it
encrypt(file, key)
