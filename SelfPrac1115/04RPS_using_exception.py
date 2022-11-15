# 04RPS_using_exception.py
'''
지금까지 만든 가위 바위 보 프로그램에
인풋제어가 없어서 다른값이 출력됏습니다
그걸 고쳐보겠습니다
'''

import random

# 사용자의 입력값을 받습니다


#예외처리

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

# 승자 변수를 생성합니다
winner = 0

# 비겻을때 
if computer_RPS_Str == player_RPS :
    winner = "없습니다!"

# 컴퓨터가 이긴경우

if computer_RPS_Str == "가위" and player_RPS == "보" :
    winner = "컴퓨터"

if computer_RPS_Str == "바위" and player_RPS == "가위" :
    winner = '컴퓨터'

if computer_RPS_Str == "보" and player_RPS == "바위" :
    winner = '컴퓨터'

# 사용자가 이긴경우

if computer_RPS_Str == "가위" and player_RPS == "바위" :
    winner = '사용자님!'

if computer_RPS_Str == "바위" and player_RPS == "보" :
    winner = '사용자님!'

if computer_RPS_Str == "보" and player_RPS == "가위" :
    winner = '사용자님!'

print("승자는~~~~~", winner)


