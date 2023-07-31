#For the security of facial data
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_image(image_path, encrypted_image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        encrypted_data = cipher_suite.encrypt(image_data)

    with open(encrypted_image_path, 'wb') as encrypted_image_file:
        encrypted_image_file.write(encrypted_data)

def decrypt_image(encrypted_image_path, decrypted_image_path):
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_data = encrypted_image_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(decrypted_image_path, 'wb') as decrypted_image_file:
        decrypted_image_file.write(decrypted_data)

