jumin = '980125-2039488'

month = jumin[2:4]
day = jumin[4:6]
print ('고객님의 생일은 ', month,'월',day,'일 입니다')
print (f'고객님의 생일은 {month}월 {day}일 입니다')
print ('고객님의 생일은  %s월 %s일 입니다'%(month, day))
print ('고객님의 생일은 {}월 {}일 입니다'.format(month,day))

def gender() :
    gender_Num = jumin[7]
    if gender_Num == '1' or gender_Num == '3':
        print ('남자')
    elif gender_Num == '2' or gender_Num == '4':
        print('여자')

gender()
