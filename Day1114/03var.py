# 03var.py
# 변수 a,b,c, x,y,z, kor,eng,hap,avg

kor, eng, hap, avg = 0, 0, 0, 0.0

kor = 16
eng = 3
hap = kor + eng
avg = hap / 2

#각각 변수에 값 대입 = 할당
#국어 90 영어 85 총점, 평균
#//3 --> 몫
#round(avg,3) <--- 소수점 자리수

print( "-" * 100)
print('국어점수: ', kor )
print('영어점수: ', eng )
print('점수의 합: ', hap )
print('평균점수: ' , round(avg, 3 ))