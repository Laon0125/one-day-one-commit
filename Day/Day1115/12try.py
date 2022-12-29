#12if.py 
kor,eng,hap,avg = 0,0,0,0
message = '안내메세지'

kor = int(input('국어입력 >>> ')) #키보드에서 숫자를 입력해도 문자 => 숫자
eng = int(input('영어입력 >>> ')) #키보드에서 숫자를 입력해도 문자 => 숫자
hap = kor + eng 
avg = hap/2

if avg >= 70 :
    message='축합격'
else:
    message='재시험'

print('국어 =', kor)
print('영어 =', eng)
print('총점 =', hap)
print('평균 =', avg)
print('결과 =', message)

print('-' * 100)
print()