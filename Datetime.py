# from datetime import datetime
# from datetime import date
# from datetime import time

import datetime
from time import ctime

simdi=datetime.datetime.today()
# result=simdi.year()
# result=simdi.month()
# result=simdi.day()
#şeklinde devam edecektir diğer zaman parametrelerinede ulaşabiliriz
result=datetime.datetime.ctime(simdi)
result=datetime.datetime.strftime(simdi,'%Y')
result=datetime.datetime.strftime(simdi,'%d')
result=datetime.datetime.strftime(simdi,'%A')
result=datetime.datetime.strftime(simdi,'%Y %B %A %d')
print(result)

t='20 december 2022 hour 10:12:30'
# dt=datetime.datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
# # gun,ay,yil=t.split()
# print(dt)
# # print(gun)
# # print(ay)
# # print(yil)

birthday=datetime(1998,8,9,16,5,40)

result=datetime.datetime.timestamp(birthday)
print(result)
