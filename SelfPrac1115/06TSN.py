# 06TSN.py
# 즐거운 민속놀이!! 삼! 육! 구!
import time
#카운터
n = 0


while True :
    # n 을 1씩 증가시킨다
    n = n + 1 
    
    # n 이 10보다 작은경우의 로직
    if n < 10 :
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9 :
            time.sleep(0.5)
            print("짝")
            continue
        time.sleep(0.5)
        print(n)
    
    # n 이 10 보다 큰경우 두 자리를 다 새야함
    else :
        #십의자리와 일의자리
        digit10 = False
        digit1 = False
        a, b = 0,0
        #10의자리 수
        a = int(n/10)
        #1의자리수
        b = n%10
        #10의 자리가 3 6 9 인 경우
        if a == 3 or a == 6 or a == 9 :
            digit1 = True
        #1의 자리가 3 6 9 인 경우
        if b == 3 or b == 6 or b == 9 :
            digit10 = True
            
        # 둘중 하나라도 3 6 9 인경우
        if digit10 == True and digit1 == True :
            print("짝 짝")
            time.sleep(0.5)
            continue

        if digit10 == True or digit1 == True :
            time.sleep(0.5)
            print('짝')
            continue
        
        else  :
            time.sleep(0.5)
            print(n)


        

