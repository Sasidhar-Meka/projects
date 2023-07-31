#Attendance Code QR+FACE+Security More General-Sense2
import time
import tkinter as tk
from collections import *
from datetime import date, datetime
from tkinter import *
from tkinter import Frame, messagebox, ttk
from tkinter.constants import GROOVE, RAISED, RIDGE # used to specify the type of border that will be displayed around a widget in a tkinter GUI application.
import cv2 #cv2 is a module in the OpenCV (Open Source Computer Vision) library for Python.
import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageTk
import os
from cryptography.fernet import Fernet
import schedule
#PIL is a library used for opening, manipulating, and saving different image file formats in Python.

from speech import*
from speech1 import*
import face_recognition


known_faces = []
known_names = []
staff_names_file = 'Staff1.txt'
with open(staff_names_file, 'r') as file:
    staff_names = [line.strip() for line in file]


# Read the encryption key from the key file
key_file_path = '/home/sasi/Desktop/pro1/keyfile.key'
with open(key_file_path, 'rb') as key_file:
    encryption_key = key_file.read()
    
    
cipher_suite = Fernet(encryption_key)

def decrypt_image(encrypted_image_path, decrypted_image_path):
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_data = encrypted_image_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(decrypted_image_path, 'wb') as decrypted_image_file:
        decrypted_image_file.write(decrypted_data)




# Decrypt and process image files for each staff member
for name in staff_names:
    encrypted_image_path = f'image encrypted/{name}.jpeg'
    decrypted_image_path = f'image decrypted/{name}.jpeg'

    # Decrypt the encrypted image
    decrypt_image(encrypted_image_path, decrypted_image_path)

    # Load the decrypted image file
    image = face_recognition.load_image_file(decrypted_image_path)

    # Check if any faces are detected
    face_encodings = face_recognition.face_encodings(image)
    if len(face_encodings) > 0:
        face_encoding = face_encodings[0]

        # Add face encoding and name to the respective lists
        known_faces.append(face_encoding)
        known_names.append(name)
    else:
        print(f"No faces found in the image: {decrypted_image_path}")




#creates the window object using the Tk() constructor from the tkinter library.
window = tk.Tk()
window.title(' K Apartments Attendance system')
window.geometry('900x600') 
                          
#two StringVar objects - StaffType and block - which are used to store string values                          
StaffType= tk.StringVar()      
block= tk.StringVar()


title = tk.Label(window,text="K Apartments Attendance System",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="lavender",fg="black")
title.pack(side=tk.TOP,fill=tk.X)

Manage_Frame=Frame(window,bg="lavender")
Manage_Frame.place(x=0,y=80,width=2000,height=2000)

ttk.Label(window, text = "Staff Type",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=150)
combo_search=ttk.Combobox(window,textvariable=StaffType,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('Managerial','Non-Managerial') 
combo_search.place(x=250,y=150)

ttk.Label(window, text = "Block",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=200)
combo_search=ttk.Combobox(window,textvariable=block,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=("A","B","C","D","SWIMMING POOL","BASEMENT","PLAY AREA","ENTRANCE","EXIT","General")
combo_search.place(x=250,y=200)



def checkk():
    if(StaffType.get() and block.get()):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")

exit_button = tk.Button(window,width=13, text="Submit",font=("Times New Roman", 15),command=checkk,bd=2,relief=RIDGE)
exit_button.place(x=300,y=380)

ttk.Label(window, text = "                           © K Attendance System-2023", background="lavender", foreground = "black", font = ("Times New Roman", 15)).place(x=100, y=500)


Manag_Frame=Frame(window,bg="lavender")
Manag_Frame.place(x=480,y=80,width=450,height=530)

canvas = Canvas(Manag_Frame, width = 320, height = 300,background="grey")      
canvas.pack()      
img = ImageTk.PhotoImage(Image.open("ki.png"))  
canvas.create_image(65,45, anchor=NW, image=img) 

window.mainloop()

#The GUI window is displayed using the mainloop() method of the Tk() object, which runs the event loop of the GUI application, waiting for user input and responding to events such as button clicks, key presses, and mouse movements.

cap = cv2.VideoCapture(0)
names=[]
today=date.today()
d= today.strftime("%b-%d-%Y")
m= today.strftime("%b-%Y")


#Process of creating list of satff names
my_file = open("Staff.txt", "r")
# reading the file
data = my_file.read()
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace('', '').split("\n")


#Process of creating list of flatno
my_filee = open("flatno.txt", "r") 
dataa = my_filee.read()
data_list = dataa.replace('', '').split("\n")


#Process of creating list of designation
my_filed = open("designation.txt", "r")
datad = my_filed.read()
datade = datad.replace('', '').split("\n")



#Process of creating list of block
my_filex = open("block.txt", "r")
datax = my_filex.read()
datadex = datax.replace('', '').split("\n")



di=dict(zip(data_into_list,data_list)) #Dictionary for Staff-flatno 
ei=dict(zip(data_into_list,datade)) #Dictionary for Staff-designation
fi=dict(zip(data_into_list,datadex)) #Dictionary for Staff-block

pob=open(d+'Present.txt','w+')
aob=open(d+'Absent.txt','w+')
zob=open(m+'Present.txt','a') #Appending because this is an Excel sheet that contains the entire attendance data of the staff for the month


fob=open(d+'.xlsx','w+') #Attendance for the day
fob.write("Staff Name"+'\t')
fob.write("Block"+'\t')
fob.write("Bwawt"+'\t')
fob.write("Flat No"+'\t')
fob.write("StaffType"+'\t')
fob.write("Designation"+'\t')
fob.write("In Time"+'\n')

lob=open(m+'.xlsx','a')
x=' ' 

#adds the employee's name to a list and writes their check-in time and other details to two files.
def enterData(z):   
    if z in names:
        pass
    else:
        it=datetime.now()
        names.append(z)
        z=x+str(z)
        intime = it.strftime("%H:%M:%S")
        l=list(z[2:-11])
        l.pop(0)
        l.pop(-1)
        s=''.join(l)
        if StaffType.get()=="Managerial" and ei[s]!="Manager":
            pass
        fob.write(z[3:-12]+'\t'+fi[s]+'\t'+block.get()+'\t'+di[s]+'\t'+StaffType.get()+'\t'+ei[s]+'\t'+intime+'\n')#Writing into Date Present Excel sheet
        lob.write(z[3:-12]+'\t'+fi[s]+'\t'+block.get()+'\t'+ei[s]+'\t'+intime+'\t'+d+'\n')#Writing into Month Present Excel sheet
        zob.write(z[3:-12]+'\n')#Writing into Present text file for the month
        pob.write(z[3:-12]+'\n')
    return names 

def checkData(data):
    # Check if data contains a specific date
    if d in str(data):
        if data in names:
            print('Already Present')
        else:
            print('\n'+str(len(names)+1)+'\n'+'present...')
            pod(str(data[:-11].decode()))  # Text-to-speech translation to notify the staff
            print(data)
            enterData(data)


frame_count = 0
face_match = False
start_time = None
scanning_duration = 60  # Duration of QR code scanning in seconds

while True:
    _, frame = cap.read()
    frame_count += 1

    if not face_match:
        if frame_count % 30 == 0:
            # Perform face recognition on every 30th frame
            print("Performing Face Recognition")
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(frame_rgb)
            face_encodings = face_recognition.face_encodings(frame_rgb, face_locations)

            for face_encoding in face_encodings:
                # Compare the face encoding with the known faces
                matches = face_recognition.compare_faces(known_faces, face_encoding)

                # Check if there is a match
                if True in matches:
                    print("Face Matched....")
                    face_match = True
                    start_time = time.time()
                    match_index = matches.index(True)
                    matched_name = known_names[match_index]
                    break

    else:
        elapsed_time = time.time() - start_time

        if elapsed_time <= scanning_duration:
            # Scan and decode QR code during the scanning duration
            print("QR Code Scanning")
            decoded_objects = pyzbar.decode(frame)
            for obj in decoded_objects:
                qr_coded=obj.data
                qr_code_data = obj.data[:-11].decode()
                print(qr_code_data)
                if qr_code_data == matched_name:
                    print("QR Code Matched....")
                    checkData(qr_coded)
                    break
                else:
                    yib=open(m+'Proxies.xlsx','a') #Attendance for the day
                    yib.write(matched_name+'\t'+'\t'+qr_code_data+fi[matched_name]+'\t'+block.get()+'\t'+ei[matched_name]+'\t'+d+'\n')
                    kod('Warning'+matched_name+'is attempting proxy for'+qr_code_data)  # Text-to-speech translation to notify the staff
        else:
            # Resume face recognition after the scanning duration
            face_match = False
            start_time = None

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('g'):
        cv2.destroyAllWindows()
        folder_pathd = '/home/sasi/Desktop/pro1/image decrypted'
        file_names = os.listdir(folder_pathd)

        for file_name in file_names:
          file_path = os.path.join(folder_pathd, file_name)
          if os.path.isfile(file_path):
            os.remove(file_path)
        break

cap.release()

    
fob.close() #Closing Attendance for the day Excel sheet
zob.close()
pob.close()

my_filen = open(d+"Present.txt", "r")
datan = my_filen.read()
datap = datan.replace('', '').split("\n")  

li=[]
for i in data_into_list:
    if i not in datap:
        aob.write(i+'\n')

aob.close()

my_filea = open(d+"Absent.txt", "r")
dataab = my_filea.read()
data_listab = dataab.replace('', '').split("\n")

kob=open(m+'A.xlsx','a')
nob=open(m+'Absent.txt','a')

for i in data_listab:
     if i != '':
        kob.write(i+'\t'+fi[i]+'\t'+ei[i]+'\t'+d+'\n')
        nob.write(i+'\n')
        

nob.close()


#For Number of days ABSENT Excel sheet

adma=defaultdict(int) #Dictionary for Staff-No of days Absent
my_fileabt = open(m+"Absent.txt", "r")
databt = my_fileabt.read()
data_listabt = databt.replace('', '').split("\n") #Creating a list from the Month Absent.txt file which contains the names of the staff present throughout the entire month

#For creating attendance Excel sheet for the month along with the number of days the staff was absent
kob=open(m+'Adays.xlsx','w')
kob.write("Staff Name"+'\t')
kob.write("Block"+'\t')
kob.write("Designation"+'\t')
kob.write("NodaysAbsent"+'\n')
for i in data_listabt:
    adma[i]+=1

dataabs=set(data_listabt)
dataadn=list(dataabs)
for i in dataadn:
    if i!='':
        kob.write(i+'\t'+fi[i]+'\t'+ei[i]+'\t'+str(adma[i])+'\n')




#For number of days Present Excel sheet

adm=defaultdict(int) #Dictionary for Staff-No of days Pressent
my_fileat = open(m+"Present.txt", "r")
datprt = my_fileat.read()
data_listprm = datprt.replace('', '').split("\n") #Creating a list from the Month Present.txt file which contains the names of the staff present throughout the entire month

#For creating attendance Excel sheet for the month along with the number of days the staff was present
tob=open(m+'Pdays.xlsx','w')
tob.write("Staff Name"+'\t')
tob.write("Block"+'\t')
tob.write("Block where attendance was taken"+'\t')
tob.write("Designation"+'\t')
tob.write("Nodayspresent"+'\n')
for i in data_listprm:
    adm[i]+=1

dataprs=set(data_listprm)
datapdn=list(dataprs)
for i in datapdn:
    if i!='':
        tob.write(i+'\t'+fi[i]+'\t'+block.get()+'\t'+ei[i]+'\t'+str(adm[i])+'\n')

kob.close()
lob.close() #Closing Monthly attendance excel sheet
tob.close() #Closing Monthly-Pdays attendance excel sheet


#The "Frame" and "ttk" classes for creating frames and widgets with themed styles, respectively. It also imports the "messagebox" function for displaying message boxes in the GUI.