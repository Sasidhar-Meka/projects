import os
from cryptography.fernet import Fernet
import schedule
import time
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#For encrypting the image files in pro/images folder
def encrypt_image(image_path, encrypted_image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        encrypted_data = cipher_suite.encrypt(image_data)

    with open(encrypted_image_path, 'wb') as encrypted_image_file:
        encrypted_image_file.write(encrypted_data)

    # Delete the original image file
    os.remove(image_path)

#For keeping track of the files in the 
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
                encrypted_image_path = os.path.join(encrypted_folder_path, file)
                encrypt_image(image_path, encrypted_image_path)

        initial_files = current_files



def decrypt_image(encrypted_image_path, decrypted_image_path):
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_data = encrypted_image_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(decrypted_image_path, 'wb') as decrypted_image_file:
        decrypted_image_file.write(decrypted_data)

    
 


if __name__== "__main__":

# Example usage
 image_path = '/home/sasi/Desktop/pro1/images/Hema V.jpeg'
 encrypted_image_path = '/home/sasi/Desktop/pro1/image encrypted/Hema V.jpeg'

 schedule.every(30).seconds.do(encrypt_image(image_path, encrypted_image_path))
 while True:
    schedule.run_pending()
    time.sleep(1)



