import time
import datetime
import random

#lg.py
def gugudan() :
    n=7
    for k in range(1,10,1):
        print(f'{n}*{k}={n*k}')
        time.sleep(0.2)

print('구구단출력끝')
print('작업시간', datetime.datetime.now())
my = datetime.datetime.now()
print(my.strftime('작업시간 %H시:%M분:%S초'))

def menu () :

    noodle_list = ['너구리', '신라면', '진라면', '안성탕면', '왕뚜껑', '김치라면']
    print (random.choice(noodle_list))
    print ("-"*70)
    time.sleep(1)
    print (random.sample(noodle_list, 2))
    print (random.sample(noodle_list,len(noodle_list)))
    print ("-"*70)

def terran () :
    print ('메딕')
    print ('테란의황제')

userID = 'jin@gmail'
userPWD = '980125'