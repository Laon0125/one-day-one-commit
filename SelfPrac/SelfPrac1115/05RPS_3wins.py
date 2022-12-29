# 04RPS_using_exception.py
'''
가위 바위 보는 여윽시 삼세판!
'''

import random


# 승자 변수를 생성합니다
winner = 0

player_Win_Count = 0
computer_Win_Count = 0

# 카운터가 3이 될때까지 반복
            ########
            #질문사항#
            ########
while player_Win_Count < 3 and computer_Win_Count < 3 :

    # 사용자의 입력값을 받습니다

    while True :

        player_RPS = str(input("가위, 바위, 보 중 하나를 입력하세요. >>>"))

        if player_RPS == "가위" :
            break

        elif player_RPS == '바위' :
            break
    
        elif player_RPS == '보' :
            break
        
        else :
            print("가위, 바위, 보를 입력하지 않았습니다 ")

    # 컴퓨터의 입력을 받기위해 랜덤한 숫자를 뽑습니다.
    computer_RPS_Number = random.randint(1,3)

    # 컴퓨터가 뽑은 숫자에 따라 가위, 바위, 보 를 대입합니다
    computer_RPS_Str = 0 
    if computer_RPS_Number == 1 :
        computer_RPS_Str = "가위"

    elif computer_RPS_Number == 2 :
        computer_RPS_Str = "바위"

    elif computer_RPS_Number == 3 :
        computer_RPS_Str = "보"

    # 컴퓨터의 선택을 출력합니다
    print('컴퓨터는 ',computer_RPS_Str, '를 냈습니다!')

    # 컴퓨터와 사용자를 비교합니다 

  

    # 비겻을때 
    if computer_RPS_Str == player_RPS :
        winner = "승자가 없습니다!"

    # 컴퓨터가 이긴경우

    if computer_RPS_Str == "가위" and player_RPS == "보" :
        winner = "승자는 컴퓨터"

    if computer_RPS_Str == "바위" and player_RPS == "가위" :
        winner = '승자는 컴퓨터'

    if computer_RPS_Str == "보" and player_RPS == "바위" :
        winner = '승자는 컴퓨터'

    # 사용자가 이긴경우

    if computer_RPS_Str == "가위" and player_RPS == "바위" :
        winner = '승자는 사용자님!'

    if computer_RPS_Str == "바위" and player_RPS == "보" :
        winner = '승자는 사용자님!'

    if computer_RPS_Str == "보" and player_RPS == "가위" :
        winner = '승자는 사용자님!'

    # win count를 올린다
    if winner == '승자는 컴퓨터' :
        computer_Win_Count = computer_Win_Count + 1 

    if winner == '승자는 사용자님!' :
        player_Win_Count = player_Win_Count + 1

    # 출력 
    print("\n", winner, '  현재까지 컴퓨터', computer_Win_Count, '승, 사용자님은 ', player_Win_Count,'승' )

print("승자는~~~~~", winner)