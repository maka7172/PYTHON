from package1.lineclass import Linetwo , Linethree 
# from package1.timing import *
from package1.timing import * 
import os
import datetime
os.system('cls')

date1 = datetime.datetime.now()


time1 = TimeShow(date1.hour,date1.minute,date1.second)
print (time1)
print(time1.hour_time())
print(time1.minit_time())
print(time1.secont_time())





# line1 = Linetwo(4,5,8,9)
# line2 = Linethree(4,5,8,9,12,18)
# print(line1.line_leght())
# print (line2.line_lenghs())
# print(line2.line_whight())


