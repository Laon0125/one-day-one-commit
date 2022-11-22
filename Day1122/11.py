import time
import datetime

def getDay(day):
    week = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    return week[day]
    
c = time.localtime()

print (f'{c.tm_year}년 {c.tm_mon}월 {c.tm_mday}일 {getDay(c.tm_wday)}')
