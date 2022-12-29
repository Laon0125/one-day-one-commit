import time
import datetime


print('작업시간', datetime.datetime.now())
print()

time.sleep(0.5)
my = datetime.datetime.now()
print(my.strftime('작업시간 %H시:%M분:%S초'))
print()

c=time.localtime()
print(c)