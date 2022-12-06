# import required module
from cryptography.fernet import Fernet

def load_key(path):
 return open(path, "rb").read()

def decrypt(path,encrypted_file,decrypt_file):
 f = Fernet(key)
 with open(encrypted_file, "rb") as file:
 # read the encrypted data
    encrypted_data = file.read()
 # decrypt data
 decrypted_data = f.decrypt(encrypted_data)
 # write the original file
 with open(decrypt_file, "wb") as file:
    file.write(decrypted_data)

key = load_key(path='C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/Python/Cryptography/CryptographyVF/filekey.key')
      
decrypt(
        path='C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/Python/Cryptography/filekey.key',
        encrypted_file = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_encrypted.txt',
        decrypt_file = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_desencrypted.txt'
        )
