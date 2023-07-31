#Code for Excel sheet for the month containing the entire attendance data of each day throughout the month 
from datetime import date, date
import schedule
import time
def fib():
 today=date.today()
 m= today.strftime("%b-%Y")
 d= today.strftime("%b-%d-%Y")
 lob=open(m+'.xlsx','w+')
 lob.write("Staff Name"+'\t')
 lob.write("Block"+'\t')
 lob.write("Block where attendance was taken"+'\t')
 lob.write("Designation"+'\t')
 lob.write("Intime"+'\t')
 lob.write("Date"+'\n')
 lob.close()
schedule.every().seconds.do(fib)
while True:
    schedule.run_pending()
    time.sleep(1)


