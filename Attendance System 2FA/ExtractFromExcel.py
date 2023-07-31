import pandas
import schedule
import time

def bof():

 excel_data_df = pandas.read_excel('/home/sasi/Documents/records.xlsx', sheet_name='Sheet1')

 l=excel_data_df['Staff Name'].tolist()
 l1=excel_data_df['Designation'].tolist()
 l2=excel_data_df['Block'].tolist()
 l3=excel_data_df['Flat No'].tolist()
 gbo=open('designation.txt','w+')
 for i in l1:
    gbo.write(i+'\n')

 gbo.close()

 pbo=open('block.txt','w+')
 for i in l2:
    pbo.write(i+'\n')

 pbo.close()

 nbo=open('Staff.txt','w+')
 for i in l:
    nbo.write(i+'\n')

 nbo.close()

 xbo=open('flatno.txt','w+')
 for i in l3:
    xbo.write(str(i)+'\n')

 xbo.close()



schedule.every().seconds.do(bof)
while True:
    schedule.run_pending()
    time.sleep(1);

