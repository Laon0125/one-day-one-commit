# 20testif.py

# if 제어문 중첩
# if 제어믄 and 연산 if 중첩
a = 2 
b = 7
c = 1
# 숫자 3개 비교 알고리즘

if a < b and a < c and b < c:
    print(a, " ", b, " ", c)

elif a < b and a < c and b > c:
    print( a, " ", c , " ", b)

elif b < a and a < c:
    print( b, " ", a , " ", c)

elif b < c and c < a :
    print( b, " ", c , " ", a)

elif c < a and a < b :
    print( c, " ", a , " ", b)

elif c < b and b < a :
    print( c, " ", b , " ", a)
    
