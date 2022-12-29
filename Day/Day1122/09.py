import time
import datetime

n = 25
for k in range (1,10,1):
    print(f'{n}*{k}={n*k}')
    time.sleep(0.25)

print ('chuleok dun')
print ('jakup sigan ', datetime.datetime.now())
my = datetime.datetime.now()
print (my.strftime('working time'))