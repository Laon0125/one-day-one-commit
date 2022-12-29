import time
import datetime

def getDay():
    day_today = time.localtime()
    for i in range (0,7) :
        if i == 3 or i == 4 or i == 5 :
            continue
        
        elif i == 0 :
            print (day_today[i],' 년','\t')
        elif i == 1:
            print (day_today[i],' 월', '\t')
        elif i == 2:
            print (day_today[i],' 일', '\t')
        elif i == 6:
            if day_today[i] == 0 :
                print ('월요일', '\t')
            elif day_today[i] == 1 :
                print ('화요일', '\t')
            elif day_today[i] == 2 :
                print ('수요일', '\t')
            elif day_today[i] == 3 :
                print ('목요일', '\t')
            elif day_today[i] == 4 :
                print ('금요일', '\t')
            elif day_today[i] == 5 :
                print ('토요일', '\t')
            elif day_today[i] == 6 :
                print ('일요일', '\t')
        
getDay()
# 2022년 11월 22일 화요일