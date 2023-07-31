import os
from cryptography.fernet import Fernet
import schedule
import time
# Read the encryption key from the key file
key_file_path = '/home/sasi/Desktop/pro1/key.txt'
with open(key_file_path, 'rb') as key_file:
    endata = key_file.read()
    encryption_key=str(endata.decode())
    print(encryption_key)
cipher_suite = Fernet(encryption_key)

def decrypt_image(encrypted_image_path, decrypted_image_path):
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_data = encrypted_image_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(decrypted_image_path, 'wb') as decrypted_image_file:
        decrypted_image_file.write(decrypted_data)

