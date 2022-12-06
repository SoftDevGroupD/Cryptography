# import required module
from cryptography.fernet import Fernet
key = Fernet.generate_key()

def decrypt(path,encrypted_file,decrypt_file):
 f = Fernet(key='y4gxrtEdiyGS5leNU7E6ATdlA2NBWQ-AWi6gdN-o8cQ=')
 with open(encrypted_file, "rb") as file:
 # read the encrypted data
    encrypted_data = file.read()
 # decrypt data
 decrypted_data = f.decrypt(encrypted_data)
 # write the original file
 with open(decrypt_file, "wb") as file:
    file.write(decrypted_data)
    
decrypt(
        path='C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/Python/Cryptography/filekey.key',
        encrypted_file = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_encrypted.txt',
        decrypt_file = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_desencrypted.txt'
        )
