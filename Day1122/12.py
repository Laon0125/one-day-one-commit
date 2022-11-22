import time

jumin = '980125-2039488'

year = int(jumin[0:2])
month = int(jumin[2:4])
day = int(jumin[4:6])
year_detect = int(jumin[7])

year = (lambda yd : year+1900 if yd < 3 else year+2000)(year_detect)

c = time.localtime()
age = c.tm_year - year

#세는나이
print (age+ 1, '살 입니다')

#만나이
if month > c.tm_mon :
    print (age-1, '살 입니다')
else :
    print (age, '살 입니다')
