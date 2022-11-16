#16testlotto.py

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
