import time
from datetime import date, dateti
def eom(st):
    today=date.today()
    d= today.strftime("%b-%d-%Y")
    yea=today.strftime("%Y")
    yr=int(yea)
    mon=today.strftime("%b")
    r={}
    r['Jan']=31
    r['Mar']=31
    r['Apr']=30
    r['May']=31
    r['Jun']=30
    r['Jul']=31
    r['Aug']=31
    r['Sep']=30
    r['Oct']=31
    r['Nov']=30
    r['Dec']=31
    if((mon=='Feb') and ((yr%4==0)  or ((yr%100==0) and (yr%400==0)))):
        r['Feb']=29
    elif(mon=='Feb') :
        r['Feb']=28
    
    return r[st]

   