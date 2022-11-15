#10try.py

#간단한 구구단 프로그램입니다

try : 
    dan = int(input('구구단 프로그램입니다, 숫자를 입력해주세요 >>'))
    for c in range (1, 10) :
        print(c, ' 곱하기 1 은 ', dan*c)
    
        print('{} * {} = {}'.format (dan,c,(dan*c)))
 
except  :
    pass

print("하잉")
print("빠잉")

