#Code to create a text file so that the contents of the text file can be used to create a list from which we can extarct the nnumber of days a particular staff memebr is present
from datetime import date, date
import schedule
import time
def oib():
 today=date.today()
 m= today.strftime("%b-%Y")
 d= today.strftime("%b-%d-%Y")
 zob=open(m+'Present.txt','w+')
 zob.close()
schedule.every().seconds.do(oib)
while True:
    schedule.run_pending()
    time.sleep(1)