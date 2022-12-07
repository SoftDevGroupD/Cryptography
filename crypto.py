from cryptography.fernet import Fernet

question = input("Are you Encrypting or Decrypting?: Type 1 for Encrypting and 2 for Decrypting ")

if question == '1':

    def generate_key():
    # key generation
        key = Fernet.generate_key()
    # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
    generate_key()

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
                'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3.txt'
                )
    
elif question == '2':
    
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
        encrypted_file = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3.txt',
        decrypt_file = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3.txt'
        )
    

'''
    def load_key(path):
        return open(path, "rb").read()

    
    #key = open(path, "rb").read()
    #f = Fernet(key)
    
    document = input("Which is the path of the document you want to decrypt")
    path = input("Give me the the path of the key of the file you want to decrypt")
    with open(path, "rb") as file:
        key = file.read()    
        f = Fernet(key=path)
    with open(document, "rb") as file:
        #print(file.read())
        # read the encrypted data
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
 # write the original file
    with open(decrypted_data, "wb") as file:
        file.write(decrypted_data)     
'''