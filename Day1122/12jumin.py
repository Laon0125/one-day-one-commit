jumin = "990726-3908257"
#문자열추출, list추출 동일 [시:종료+1]
#문제 고객님의 생일은 12월 26일 입니다
#문제 남자1/3  여자2/4

month = jumin[2:4]
day = jumin[4:6]
print('고객님의 생일은',month,'월',day,'일 입니다')
print(f'고객님의 생일은 {month}월 {day}일 입니다')
print('고객님의 생일은 %s월 %s일 입니다'%(month,day))
print('고객님의 생일은 {}월 {}일 입니다'.format(month, day))
print()

gender = jumin[7]
if gender=='1' or gender=='3':
    print('당신의 성별은 남자입니다')
elif gender=='2' or gender=='4':     
    print('당신의 성별은 여자입니다')
else:
    print('성별입력이 틀렸습니다 \n다시확인 정확하게 입력하세요')

print('******-', jumin[7:])