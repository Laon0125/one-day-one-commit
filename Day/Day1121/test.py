# test.py 
#문제 1 )구구단 처리 입력받아서 함수로 구현
#문제 2 )난수이용한 로또  6개 1~45
import random
print('-' * 100)
print()

def myExit() :
    print('프로그램을 종료합니다')
    quit

def multiple(given_Number) :
    i = 1
    while i <= 9 :
        print(i * given_Number)
        i += 1

def lotto () :
    lotto = set()
    while True :
        num = random.randint(1,45)
        if len(lotto) >=6:
            break
        else :
            lotto.add(num)
    lotto_List = list(lotto)
    lotto_List.sort()
    print(lotto_List)




while True :
    print()
    print('1.구구단 2.로또 9.종료')
    user_choice = input('메뉴선택')
    if user_choice == "9" :
        myExit()
        
    elif user_choice =='1':
        gugudan_num = int(input("숫자를 입력하세요"))
        multiple(gugudan_num)
        myExit()
        

    elif user_choice == '2' :
        lotto()
        myExit()



