import qrcode  
from datetime import date, date
import schedule
import time

def jo():
 today=date.today()
 d= today.strftime("%b-%d-%Y")
 # generating a QR code using the make() function  
 qr_img = qrcode.make(d)  
 # saving the image file  
 qr_img.save(d+".jpg")  
schedule.every().seconds.do(jo)
while True:
    schedule.run_pending()
    time.sleep(1);