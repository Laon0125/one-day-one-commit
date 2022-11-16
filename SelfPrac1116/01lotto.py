#1lotto.py

import random

# 로또 번호를 포함하게될 Set 생성
lotto_Number_Set = set()
lotto_Number_List = list()
lotto_Number = 0
raffle_Counter = 0

#문제 로또 6개발생 
while raffle_Counter < 6 :
    lotto_Number=random.randint(1,45)
    lotto_Number_Set.add(lotto_Number)
    raffle_Counter = len(lotto_Number_Set)

#문제 로또 6개를 적은숫자부터 소트 sort(), 알고리즘

lotto_Number_List = list(lotto_Number_Set) 
lotto_Number_List.sort()
print ("이번 회차의 로또번호는 ", lotto_Number_List)

# 플레이어가 로토번호를 선택하는 기능

lotto_Player_Set = set()
lotto_Player_List = list()
lotto_Player_Num = 0
pick_Counter = 0
flag = True
while flag :
    lotto_Player_Num = int(input("당신의 로또 번호는?"))    
    lotto_Player_Set.add(lotto_Player_Num)
    pick_Counter += 1
    if pick_Counter == 6 :
        flag = False
    else :
        pass
lotto_Player_List = list(lotto_Player_Set)
lotto_Player_List.sort()


print ("당신의 선택한 번호는", lotto_Player_List)



# 세트의 교집합 기능 사용
# 플레이어의 숫자와 컴퓨터의 숫자가 같을떄 
# 그 수를 담을 세트를 생성
same_Number_Set = set()
# 이 세트에 교집합을 넣는다
same_Number_Set = lotto_Player_Set.intersection(lotto_Number_Set)
# 겹친 숫자들을 보여준다
print('당신이 맞춘 숫자는 ',same_Number_Set,' 입니다.')
# 교집합이 들어간 세트의 길이를 담을 변수 선언
size_of_set = 0
#set의 크기를 구한다 len()사용 그 후 위 변수에 대입
size_of_set = len(same_Number_Set)
# 등수판별 다 같으면 1등 하나다르면 3등 두개다르면 4등... 
while True :
    if size_of_set > 5 :
        print("1등이십니다!!")
        break
    elif size_of_set > 4 :
        print("아쉽게도 3등이십니다!!")
        break
    elif size_of_set > 3 :
        print("4등 할빠엔 안하고 말지...")
        break
    else :
        print("ㅋㅋㅋ 탕진잼")
        break


