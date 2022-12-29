import time
import datetime

def getDay(day):
    week=[ '월요일',  '화요일',  '수요일', '목요일', '금요일', '토요일', '일요일'  ] 
    return week[day]


c=time.localtime()
print(f'{c.tm_year}년 {c.tm_mon}월 {c.tm_mday}일 {getDay(c.tm_wday)}') #권장  




#2022년 11월 22일 화요일 
#시분초 시간구하지 마세요 

'''
week=['월요일',  '화요일',  '수요일', '목요일', '금요일', '토요일', '일요일'  ] 
    msg='요일'
    if (day==0): msg='월요일'
    elif (day==1): msg='화요일'
    elif (day==2): msg='수요일'
    elif (day==3): msg='목요일'
    elif (day==4): msg='금요일'
    elif (day==5): msg='토요일'
    elif (day==6): msg='일요일'
'''