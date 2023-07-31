from datetime import date, date
import schedule
import time
def oib():
 today=date.today()
 m= today.strftime("%b-%Y")
 d= today.strftime("%b-%d-%Y")
 nob=open(m+'Absent.txt','w+')
 nob.close()
schedule.every().seconds.do(oib)
while True:
    schedule.run_pending()
    time.sleep(1)