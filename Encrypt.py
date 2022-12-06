from cryptography.fernet import Fernet

def encrypt_file(file_to_encrypt,file_encrypted): 
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(file_to_encrypt, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_encrypted, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

encrypt_file('C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3.txt',
             'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_encrypted.txt'
             )