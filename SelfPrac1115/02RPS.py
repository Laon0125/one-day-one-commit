# 02RPS.py
# 심플한 가위 바위 보 게임입니다
# 플레이어는 가위, 바위, 보 중 하나를 입력합니다

# random 사용을 위한 import

import random

# 사용자의 입력값을 받습니다

player_RPS = str(input("가위, 바위, 보 중 하나를 입력하세요. >>>"))

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
    print("it is a draw!")

# 컴퓨터가 가위를 낸 경우

if computer_RPS_Str == "가위" :
    if player_RPS == "보" :
        print('컴퓨터가 이겻습니다.')

    elif player_RPS == "바위" :
        print('당신이 이겻습니다.')

# 컴퓨터가 바위를 낸 경우

if computer_RPS_Str == "바위" :
    if player_RPS == "가위" :
        print('컴퓨터가 이겻습니다.')

    elif player_RPS == "보" :
        print('당신이 이겻습니다.')

# 컴퓨터가 보를 낸 경우

if computer_RPS_Str == "보" :
    if player_RPS == "바위" :
        print('컴퓨터가 이겻습니다.')

    elif player_RPS == "가위" :
        print('당신이 이겻습니다.')





