from datetime import date, date
import schedule
import time
def gib():
 today=date.today()
 m= today.strftime("%b-%Y")
 d= today.strftime("%b-%d-%Y")
 kob=open(m+'A.xlsx','w')
 kob.write("Staff Name"+'\t')
 kob.write("Block"+'\t')
 kob.write("Designation"+'\t')
 kob.write("Date"+'\n')
 kob.close()
schedule.every().seconds.do(gib)
while True:
    schedule.run_pending()
    time.sleep(1)