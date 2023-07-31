#Code for removing QR codes generated everyday
from datetime import date, date
import os
import schedule
import time
today=date.today()
d= today.strftime("%b-%d-%Y")
def jb():
 today=date.today()
 my_file = open("Staff.txt", "r")
   
 # reading the file
 data = my_file.read()
  
 # replacing end of line('/n') with ' ' and
 # splitting the text it further when '.' is seen.
 data_into_list = data.replace('', '').split("\n")
  
 # printing the data
 print(data_into_list)
 my_file.close()
 for i in data_into_list:
  os.remove("/home/sasi/Desktop/pro1/"+i+".png");

os.remove("/home/sasi/Desktop/pro1/"+d+".jpg");
schedule.every().seconds.do(jb)
while True:
    schedule.run_pending()
    time.sleep(1)