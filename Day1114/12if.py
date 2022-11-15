#12if.py
#평균을 구해라!
kor, eng, hap, avg = 0, 0, 0, 0
message = '안내메세지'

kor = int(input('국어입력 >>>')) #키보드로 숫자를 입력해도 문자로 인식
eng = int(input('영어입력 >>>'))
hap = kor + eng
avg = (kor + eng)/2
print('korean = ', kor)
print('english = ', eng)
print('total = ', hap)
print("avg = ", avg)

print('-' * 100)

'''
파이썬 조건 if 
평균점수가 70점 축합격/ 0~69 재시험
'''

if avg >= 70:
    print('축 합 격')
else :
    print('하 하 하 넌 못 지 나 간 다')