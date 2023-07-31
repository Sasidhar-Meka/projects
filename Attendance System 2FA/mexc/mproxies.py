#Code for Excel sheet for the month containing the entire attendance data of each day throughout the month 
from datetime import date, date
import schedule
import time
def yib():
 today=date.today()
 m= today.strftime("%b-%Y")
 d= today.strftime("%b-%d-%Y")
 yib=open(m+'Proxies.xlsx','w+')
 yib.write("By"+'\t')
 yib.write('For'+'\t')
 yib.write("Block"+'\t')
 yib.write("Bwpwa"+'\t')
 yib.write("Designation"+'\t')
 yib.write("Date"+'\n')
 yib.close()

schedule.every().seconds.do(yib)
while True:
    schedule.run_pending()
    time.sleep(1)