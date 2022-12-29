import time
import datetime

n=7
for k in range(1,10,1):
    print(f'{n}*{k}={n*k}')
    time.sleep(0.2)

print('구구단출력끝')
print('작업시간', datetime.datetime.now())
my = datetime.datetime.now()
print(my.strftime('작업시간 %H시:%M분:%S초'))