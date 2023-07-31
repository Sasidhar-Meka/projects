from MyQR import myqr
import os
from datetime import date, date
import schedule
import time

def job():
 today=date.today()
 d= today.strftime("%b-%d-%Y")
 f = open('Staff.txt','r')
 lines = f.read().split("\n")
 print(lines)


 for _ in range (0,len(lines)):
    data = lines[_]+d
    version,level,qr = myqr.run(
        str(data),
        level='H',
        version=1,
        picture=str(d+'.jpg'),
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name = str(lines[_]+'.png'),
        save_dir=os.getcwd()
    )
schedule.every().seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)