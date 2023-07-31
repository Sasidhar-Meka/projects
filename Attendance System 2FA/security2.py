import os
from cryptography.fernet import Fernet
import schedule
import time
key = Fernet.generate_key()
cipher_suite = Fernet(key)


# Save the encryption key to a file
key_file_path = '/home/sasi/Desktop/pro1/keyfile.key'
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)


#Encrypting image files in the image folder
def encrypt_image(image_path, encrypted_folder_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        encrypted_data = cipher_suite.encrypt(image_data)

    # Create the encrypted image file with the same name as the original
    encrypted_image_path = os.path.join(encrypted_folder_path, os.path.basename(image_path))

    with open(encrypted_image_path, 'wb') as encrypted_image_file:
        encrypted_image_file.write(encrypted_data)

    return encrypted_image_path



#Keeping track of the image files in the pro1/images folder and calling the encrypt function to encrypt accordingly
def watch_folder(folder_path, encrypted_folder_path):
    # Get the initial list of files in the folder
    initial_files = set(os.listdir(folder_path))

    # Start watching the folder for changes
    while True:
        time.sleep(1)
        current_files = set(os.listdir(folder_path))
        
        # Check for new files in the folder
        new_files = current_files - initial_files

        for file in new_files:
            if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
                image_path = os.path.join(folder_path, file)
                encrypted_image_path = encrypt_image(image_path, encrypted_folder_path)

                # Delete the original image file after successful encryption
                os.remove(image_path)

        initial_files = current_files


if __name__== "__main__":

 # Specify the paths to your images folder and encrypted images folder
 image_folder_path = '/home/sasi/Desktop/pro1/images'
 encrypted_folder_path = '/home/sasi/Desktop/pro1/image encrypted'

 # Start watching the folder for changes and encrypt new images
 watch_folder(image_folder_path, encrypted_folder_path)